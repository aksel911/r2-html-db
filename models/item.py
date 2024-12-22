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


@dataclass
class DT_ItemAbnormalResist:
    """Data class for item abnormal resist"""
    IID: int
    IName: str
    AID: int
    ADesc: str
    AType: int
    ATypeDesc: str 
    SID: int
    SName: str
    mSPID: int
    SkillPackName: str
    SkillPackDesc: str
    mSpriteFile: str
    mSpriteX: int
    mSpriteY: int
    

@dataclass
class DT_Bead:
    """Data class for beads"""
    mBeadNo: int
    mBeadName: str
    mBeadType: int
    mBeadTypeDesc: str
    mChkGroup: str
    mPercent: float
    mApplyTarget: str
    mParamA: float
    mParamADesc: str
    mParamB: float
    mParamBDesc: str
    mParamC: float
    mParamCDesc: str
    mParamD: float
    mParamDDesc: str
    mParamE: float
    mParamEDesc: str
    mTargetIPos: str
    mProb: float
    mGroup: int
    mItemSubType: int
    mMaxHoleCount: int
    mHoleCount: int
    mHoleProb: float
    MID: int



@dataclass
class DT_ItemBeadModule:
    """Data class for beads"""
    MID: int
    MType: int
    MName: str
    MDesc: str
    MLevel: int
    MAParam: float
    MAParamName: str
    MBParam: float
    MBParamName: str
    MCParam: float
    MCParamName: str
    
    
@dataclass
class TblBeadHoleProb:
    """Data class for beads"""
    IName: str
    mMaxHoleCount: int
    mHoleCount: int
    mProb: float