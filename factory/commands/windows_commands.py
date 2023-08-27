from enum import Enum

class Windows(Enum):
    
    SERVICES = [
        ('get all services', '--'),
        ('get service', '--'),
        ('get services sorted by status', '--'),
        ('get non-default windows services', '--')
    ]
    SYSTEM_RESOURCES = [
        ('get resources', '--'),
        ('get memory', '--'),
        ('get cpu', '--')
    ]
    PROCESSES = [
        ('get processes', '--'),
        ('list processes by priority', '--'),
        ('show process owner', '--')
    ]
    NETWORK = [
        ('get network configs', '--')
    ]


    @classmethod
    def list_commands(cls):
        # print('attr: value')
        # for attr in cls.__dict__:
        #     print(f"{attr}: {cls.__dict__[attr]}")

        # print('Members: ')
        # for attr in cls.__dict__['_member_names_']:
        #     print(f"{attr}: {getattr(cls, attr)}")
        
        commands = []
        for e in cls:
            print('E: ', e)
            for x in e.value:
                commands.append(x[0] + ' : ' + x[1])

        # commands2 = [x[0] + " : " + x[1] for x in e.value for e in cls]
        # print('Commands2: ',commands2)
        for c in commands:
            print(c)

        return commands
