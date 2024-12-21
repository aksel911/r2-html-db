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