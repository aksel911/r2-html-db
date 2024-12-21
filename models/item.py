from dataclasses import dataclass
from os.path import splitext
from flask import current_app

@dataclass
class DT_Item:
    """Data class for items"""
    IID: int
    IName: str
    IDesc: str
    IWeight: float
    IUseClass: str
    IType: int
    IMaxBeadHoleCount: int
    ITermOfValidity: int

    def __post_init__(self):
        self.IUseClass = f"{current_app.config['GITHUB_URL']}class/{self.IUseClass}.png"

@dataclass
class DT_ItemResource:
    """Data class for item resources"""
    ROwnerID: int
    RFileName: str
    RPosX: int
    RPosY: int

    def __post_init__(self):
        self.RFileName = splitext(self.RFileName)[0]
        self.file_path = (
            f"{current_app.config['GITHUB_URL']}"
            f"{self.RFileName}_{self.RPosX}_{self.RPosY}.png"
        )
        
@dataclass
class TblSpecificProcItem:
    """Data class for TblSpecificProcItem"""
    mIID: int
    IName: str
    mProcNo: int
    mProcDesc: str
    mAParam: int
    mAParamDesc: str
    mBParam: int
    mBParamDesc: str
    mCParam: int
    mCParamDesc: str
    mDParam: int
    mDParamDesc: str
