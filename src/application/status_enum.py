from enum import Enum
from typing import List, TypeVar

StatusEnum = TypeVar("StatusEnum")


class StatusEnum(str, Enum):
    ENABLED = "enabled"
    DISABLED = "disabled"
    INVALID = ""

    @classmethod
    def get_members_values(cls) -> List[str]:
        return [cls[v.upper()] for v in cls._member_map_.values() if v.value]

    @classmethod
    def get_members_keys(cls) -> List[str]:
        return [k for k in cls._member_map_.keys() if cls[k]]

    @classmethod
    def _missing_(cls, value: str) -> StatusEnum:
        value = value.upper().strip()

        if value not in cls._member_map_:
            return cls.INVALID

        return cls[value]
