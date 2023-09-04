import platform
from factory.commands.system_commands import SystemCommands, os_command_factory
from utilities.exceptions import CommandNotFound

OS = platform.platform()
OS = 'Windows'


class UserUI():

    def __init__(self, system_commands=SystemCommands(os_command_factory.get_os_type_list(OS))):
        self._commands = system_commands

    def get_input(self):
        cmd = input('>>>')
        result = None
        try:
            status, res, argument = self._commands.get_command(cmd)
        except CommandNotFound:
            print('Command does not exists! Here is a list of the available commands:')
            self._commands.help()
            return None
        if status:
            if 'help' in res:
                self._commands.help()
            elif 'exit' in res:
                self._commands.exit()
            else:
                full_command = self._commands._get_full_command(res)
                result = self._commands.run_command(full_command, argument)
                print('Result is: \n', result)
        else:
            print('The command you entered matches a few possible commands: ')
            for c in res:
                print(c)

