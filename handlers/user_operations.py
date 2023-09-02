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


    def help(self):
        self._commands.list_commands()

    
    def exit(self):
        print('Thank you for using this application! Exiting...')
        exit()

    def get_input(self):
        cmd = input('>>>')
        pass


    def _verify_input(self, cmd):
        """
        Check if provided command matches common commands or any of the regular os commands. Three cases:
            1. Command matches completely -> return command and execute it
            2. Command is not completed but matches one or more of the given commands up to that point:
                - send the user a reply his command is partially matching existing command(s) and print them
                - assign a value based on order to each partial match - the user can select the number to 
                quickly get the desired command; if not he can try a different command
            3. No match -> run the help command to assist user

            Return values:
                1. (True, <matching command>)
                2. (False, <list of partially matched commands>)
                3. (False, None)
        """
        if cmd.lower() in COMMON_COMMANDS or cmd.lower() in self._commands._commands_short:
            return (True, cmd)
        else:
            pass
