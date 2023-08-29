from . import command_list


class OSCommandLists():

    def __init__(self):
        self._os_lists = {}


    def register_os_list(self, os_type, list):
        self._os_lists[os_type] = list


    def get_os_type_list(self, os_type):
        command_list = self._os_lists.get(os_type, None)
        if not command_list:
            raise ValueError(os_type)
        return command_list


class SystemCommands():

    def __init__(self, os_command_list):
        self._os_command_list = os_command_list

    def list_commands(self):
        # print('attr: value')
        # for attr in self._os_command_list:
        #     print(f"{attr}: {self._os_command_list.__dict__[attr]}")

        # print('Members: ')
        # for attr in self._os_command_list.__dict__['_member_names_']:
        #     print(f"{attr}: {getattr(self._os_command_list, attr)}")
        
        commands = []
        for e in self._os_command_list:
            print('E: ', e)
            for x in e.value:
                commands.append(x[0] + ' : ' + x[1])

        # commands2 = [x[0] + " : " + x[1] for x in e.value for e in self._os_command_list]
        # print('Commands2: ',commands2)
        for c in commands:
            print(c)

        return commands


os_command_factory = OSCommandLists()
os_command_factory.register_os_list('Windows', command_list.Windows)
