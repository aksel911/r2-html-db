# Author: Trolll, https://github.com/Trolll67, https://vk.com/trolll67
# Date: 2024-10-23
# Description: Python script to export Blender 3.6 models to FBX format
#
# License: GNU General Public License v3.0
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


from collections import defaultdict
from io import BufferedReader
import os
import struct
import sys
import bpy
from math import radians
from bpy_extras import node_shader_utils, image_utils
import logging


def setup_logging():
    logger = logging.getLogger("Blender36_ConvertLogger")
    logger.setLevel(logging.DEBUG)

    # Create handlers: one for logging to console and one for logging to a file
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("converter_blender36.log")

    # Set logging levels for handlers
    console_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for both handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

logger = setup_logging()


class BinaryReader():
	"""General BinaryReader class"""
	def __init__(self, inputFile: BufferedReader):
		self.inputFile: BufferedReader = inputFile
		self.endian = '<'
		self.debug = False
		self.mode = self.inputFile.mode if hasattr(self.inputFile, 'mode') else None

	def read_bytes(self, count) -> bytes:
		if self.mode != 'rb':
			return None
		
		data = self.inputFile.read(count)
		return data
	
	def read_int32(self) -> int:
		if self.mode != 'rb':
			return None
		
		data = self.inputFile.read(4)
		data = struct.unpack(self.endian+'i', data)[0]
		return data

	def read_string(self, limit=1000) -> str:
		if self.mode != 'rb':
			return None
		
		completed = False
		data = ''
		for i in range(limit):
			char = struct.unpack('c', self.inputFile.read(1))[0]
			if char == b'\x00' or completed == True:
				completed = True
				continue # not break to set cursor to right position

			data += char.decode('utf-8', errors='ignore')
		return data

class MeshTexture():
	def __init__(self, diffuse=None, specular=None, normal=None):
		self.diffuse = diffuse
		self.specular = specular
		self.normal = normal

class ModelMesh():
	def __init__(self):
		self.name = None
		self.texture_index = 0

class Model():
	def __init__(self, name):
		self.name = name
		self.textures = []
		self.meshes = []

def remove_materials():
	for obj in bpy.data.objects:
		if obj.type == 'MESH':
			obj.data.materials.clear()

def remove_textures():
	for img in bpy.data.images:
		bpy.data.images.remove(img)

def prepare_object(rmb_filepath, obj):
    # rotate blender model x axis 90 degrees
    obj.rotation_euler[0] = radians(90)
    # scale object
    obj.scale = (0.01, 0.01, 0.01)
    # apply transformations
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

    # Don't remove existing materials and textures
    # remove_materials()
    # remove_textures()

    # parse model
    logger.info(f"Model: {rmb_filepath}")

    model = parse_model(rmb_filepath)
    if model is None:
        logger.error(f"Model not found: {rmb_filepath}")
        return
    
    def find_mesh(name):
        for mesh in model.meshes:
            if mesh.name == name:
                return mesh
        return None
    
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH':
            mesh = obj.data
            mesh_data = find_mesh(obj.name)
            if mesh_data is not None:
                texture_data = model.textures[mesh_data.texture_index]
                add_material(mesh, texture_data)
            else:
                logger.error(f"Mesh not found data: {obj.name}")





def find_texture_file(filepath):
	if filepath is None:
		return None
		
	dirname = os.path.dirname(filepath)
	filename = os.path.basename(filepath)
	files = os.listdir(dirname)
	for file in files:
		if file.lower() == filename.lower():
			return dirname + os.sep + file
		
	return None

def get_specific_texture(base_name: str, tex_type: str) -> str:
	filename = base_name.split('.')[0]
	ext = base_name.split('.')[-1]
	filename = filename + tex_type + '.' + ext

	if os.path.exists(filename):
		return filename
	else:
		return None
	
def parse_model(filepath):
	directory = os.path.dirname(filepath)
	texture_directory = os.path.join(directory, 'texture')
	if not os.path.exists(texture_directory): 
		texture_directory = os.path.join(directory, 'textures')
		if not os.path.exists(texture_directory):
			logger.error(f"Texture directory not found: {os.path.join(directory, 'texture')}")
			return None
	
	filename = os.path.basename(filepath)
	model = Model(filename)
	with open(filepath, 'rb') as file:
		reader = BinaryReader(file)
		# skip header
		reader.read_bytes(20)
		texture_count = reader.read_int32()
		mesh_count = reader.read_int32()
		reader.read_bytes(8)

		model.textures = []
		for a in range(texture_count):
			texture = MeshTexture() 
			texname = reader.read_string(limit=260)          # 260 bytes texture 
			# fix paths
			texname = os.path.basename(texname)

			texpath = os.path.join(texture_directory, texname)
			texture.diffuse = texpath
			
			# get specular texture
			specular = get_specific_texture(os.path.join(texture_directory, texname), '_sp')
			if specular is not None:
				texture.specular = specular

			# get normal texture
			normal = get_specific_texture(os.path.join(texture_directory, texname), '_n')
			if normal is not None:
				texture.normal = normal

			model.textures.append(texture)

		model.meshes = []
		for i in range(mesh_count):
			mesh = ModelMesh()
			reader.read_bytes(8)
			mesh.name = reader.read_string(limit=64)
			reader.read_bytes(64+20+2000)
			model.meshes.append(mesh)

		logger.info(f"Textures: {len(model.textures)}")
		logger.info(f"Meshes: {len(model.meshes)}")

	return model

def add_material(mesh, texture_data):
    logger.info(f"Setting up material for mesh: {mesh.name}")
    mat_name = f'{mesh.name}_mat'

    blend_mat = bpy.data.materials.new(name=mat_name)
    blend_mat.use_nodes = True
    nodes = blend_mat.node_tree.nodes
    links = blend_mat.node_tree.links
    
    # Clear default nodes
    nodes.clear()

    # Create main nodes
    principled_bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    output_node = nodes.new('ShaderNodeOutputMaterial')
    
    # Link main nodes
    links.new(principled_bsdf.outputs['BSDF'], output_node.inputs['Surface'])

    if texture_data:
        # Add diffuse texture
        diffuse = find_texture_file(texture_data.diffuse)
        if diffuse is not None:
            tex_image = nodes.new('ShaderNodeTexImage')
            tex_image.image = image_utils.load_image(diffuse, check_existing=True)
            links.new(tex_image.outputs['Color'], principled_bsdf.inputs['Base Color'])
            
            # Add UV mapping
            uv_node = nodes.new('ShaderNodeUVMap')
            links.new(uv_node.outputs['UV'], tex_image.inputs['Vector'])
            
        # Add normal map
        normal = find_texture_file(texture_data.normal)
        if normal is not None:
            normal_tex = nodes.new('ShaderNodeTexImage')
            normal_tex.image = image_utils.load_image(normal, check_existing=True)
            
            normal_map = nodes.new('ShaderNodeNormalMap')
            links.new(normal_tex.outputs['Color'], normal_map.inputs['Color'])
            links.new(normal_map.outputs['Normal'], principled_bsdf.inputs['Normal'])
            
            # UV mapping for normal
            uv_node = nodes.new('ShaderNodeUVMap')
            links.new(uv_node.outputs['UV'], normal_tex.inputs['Vector'])
            
        # Add specular map
        specular = find_texture_file(texture_data.specular)
        if specular is not None:
            spec_tex = nodes.new('ShaderNodeTexImage')
            spec_tex.image = image_utils.load_image(specular, check_existing=True)
            links.new(spec_tex.outputs['Color'], principled_bsdf.inputs['Specular'])
            
            # UV mapping for specular
            uv_node = nodes.new('ShaderNodeUVMap')
            links.new(uv_node.outputs['UV'], spec_tex.inputs['Vector'])

    # Set material settings
    principled_bsdf.inputs['Specular'].default_value = 0.5
    principled_bsdf.inputs['Roughness'].default_value = 0.5

    # Add material to mesh
    if mesh.materials:
        mesh.materials[0] = blend_mat
    else:
        mesh.materials.append(blend_mat)



def export_fbx(output):
    # select all objects
    bpy.ops.object.select_all(action='SELECT')
    # export selected objects to fbx with embedded textures
    bpy.ops.export_scene.fbx(
        filepath=output,
        check_existing=False,
        use_selection=True,
        path_mode='COPY',  # This will copy textures
        embed_textures=True,  # This will embed textures in the FBX
        use_custom_props=True,
        bake_anim=True,  # Enable animation export
        bake_anim_use_all_bones=True,
        bake_anim_use_nla_strips=True,
        bake_anim_use_all_actions=True,
        add_leaf_bones=False,
        use_metadata=True
    )

def parse_arguments():
    parsed_args = defaultdict(list)
    args = sys.argv[1:]

    if '--' in args:
        start_index = args.index('--') + 1
    else:
        start_index = len(args)

    i = start_index
    while i < len(args):
        if args[i].startswith('-'):
            if i + 1 < len(args) and not args[i + 1].startswith('-'):
                parsed_args[args[i]].append(args[i + 1])
                i += 2
            else:
                parsed_args[args[i]].append(None)
                i += 1
        else:
            i += 1
    
    return parsed_args['--out'][0], parsed_args['--rmb'][0]

def get_active_space_view3d(context: bpy.types.Context) -> bpy.types.SpaceView3D:
	if context.space_data and context.space_data.type == 'VIEW_3D':
		space = context.space_data
		if isinstance(space, bpy.types.SpaceView3D):
			if space.type == 'VIEW_3D':
				return space

	for area in context.screen.areas:
		if isinstance(area, bpy.types.Area):
			if area.type == 'VIEW_3D':
				space = area.spaces.active
				if isinstance(space, bpy.types.SpaceView3D):
					if space.type == 'VIEW_3D':
						return space

	return None

def enable_shading():
	space = get_active_space_view3d(bpy.context)
	if space:
		space.shading.type = 'MATERIAL'

def main():
	# get selected object
	obj = bpy.context.scene.objects[0]
	if obj == None:
		logger.error("No object selected")
		return
	
	blend_file_path = bpy.data.filepath
	blend_file_name = bpy.path.basename(blend_file_path)

	output, rmb_filepath = parse_arguments()
	if not os.path.exists(output):
		os.makedirs(output)

	# prepare object
	prepare_object(rmb_filepath, obj)
	
	# export object to fbx
	export_filepath = os.path.join(output, blend_file_name.replace(".blend", ".fbx"))
	export_fbx(export_filepath)

	# NOTE: Extra logic here to resave blend file with shading enabled
	enable_shading()
	bpy.ops.wm.save_mainfile()
	bpy.ops.wm.quit_blender()

if __name__ == '__main__':
	main()