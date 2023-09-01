from . import command_list
from utilities.exceptions import CommandNotFound


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
        self._commands_short = self._get_commands_short()

    def list_commands(self):
        commands = []
        for e in self._os_command_list:
            # print('E: ', e)
            for x in e.value:
                commands.append(x[0] + ' : ' + x[1])

        for c in commands:
            print(c)

        return commands
    

    def get_command(self, cmd):
        if cmd in self._commands_short:
            return cmd
        else:
            raise CommandNotFound
    
    def _get_commands_short(self):
        commands = []
        for c in self._os_command_list:
            for x in c.value:
                commands.append(x[0])

        return commands


os_command_factory = OSCommandLists()
os_command_factory.register_os_list('Windows', command_list.Windows)
