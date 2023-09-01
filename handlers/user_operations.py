import platform
from factory.commands.system_commands import SystemCommands, os_command_factory

OS = platform.platform()
OS = 'Windows'


COMMON_COMMANDS = [
    'help',
    'exit'
]


class UserUI():

    def __init__(self, system_commands=SystemCommands(os_command_factory.get_os_type_list(OS))):
        self._commands = system_commands
