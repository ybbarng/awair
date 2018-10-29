from enum import Enum


class NoValue(Enum):
    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)


class DeviceType(NoValue):
    AWAIR = 'awair'
    AWAIR_R2 = 'awair-r2'
    AWAIR_GLOW = 'awair-glow'
    AWAIR_OMNI = 'awair-omni'
    AWAIR_MINT = 'awair-mint'
