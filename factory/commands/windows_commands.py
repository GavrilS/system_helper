from enum import Enum

class Windows(Enum):
    
    SERVICES = [
        'get all services',
        'get service',
        'get services sorted by status',
        'get non-default windows services'
    ]
    SYSTEM_RESOURCES = [
        'get resources',
        'get memory',
        'get cpu'
    ]
    PROCESSES = [
        'get processes',
        'list processes by priority',
        'show process owner'
    ]
    NETWORK = [
        'get network configs'
    ]


    @classmethod
    def list_commands(cls):
        pass
