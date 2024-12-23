from dataclasses import dataclass
from typing import Dict

@dataclass
class Monster:
    """Data class for monsters"""
    MID: int
    MName: str
    MClass: int
    MLevel: int
    MHP: int
    MMP: int
    MExp: int
    mRaceType: int
    mIsShowHp: bool
    MChaotic: int
    mDetectTransF: bool
    mDetectTransP: bool
    mDetectChao: int
    mIsResistTransF: bool

    def to_dict(self) -> Dict:
        """Convert monster to dictionary with formatted fields"""
        return {
            "MID": self.MID,
            "MName": self.MName.replace('/n', ' '),
            "MClass": self.MClass,
            "MLevel": self.MLevel,
            "MHP": self.MHP,
            "MMP": self.MMP,
            "mExp": self.MExp,
            "mRaceType": self.mRaceType,
            "mIsShowHp": 'Да' if self.mIsShowHp else 'Нет',
            "MChaotic": self.MChaotic,
            "mDetectTransF": 'Да' if self.mDetectTransF else 'Нет',
            "mDetectTransP": 'Да' if self.mDetectTransP else 'Нет',
            "mDetectChao": self.mDetectChao,
            "mIsResistTransF": 'Да' if self.mIsResistTransF else 'Нет'
        }


@dataclass
class DT_MonsterResource:
    """Data class for monster resources"""
    RFileName: str

@dataclass
class DT_MonsterAbnormalResist:
    """Data class for monster abnormal resist"""
    MID: int
    MName: str
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
class DT_MonsterAttributeAdd:
    AID: int
    AType: int
    AName: str
    ALevel: int
    ADiceDamage: int
    ADamage: int
    
    
@dataclass
class DT_MonsterAttributeResist:
    AID: int
    AType: int
    AName: str
    ALevel: int
    ADiceDamage: int
    ADamage: int
    


@dataclass
class DT_MonsterProtect:
    SID: int
    ProtectSID: int
    SName: str
    SLevel: int
    SDPV: int
    SMPV: int
    SRPV: int
    SDDV: int
    SMDV: int
    SRDV: int

@dataclass
class DT_MonsterSlain:
    SID: int
    SType: int
    SName: str
    SLevel: int
    SHitPlus: int
    SDDPlus: int
    SRHitPlus: int
    SRDDPlus: int