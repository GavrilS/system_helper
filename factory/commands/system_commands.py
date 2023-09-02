from . import command_list
from utilities.exceptions import CommandNotFound

COMMON_COMMANDS = [
    'help',
    'exit'
]


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
    
    def help(self):
        self.list_commands()

    
    def exit(self):
        print('Thank you for using this application! Exiting...')
        exit()

    def run_command(self, cmd):
        pass
    

    def get_command(self, cmd):
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
        if cmd.lower() in COMMON_COMMANDS or cmd.lower() in self._commands_short:
            return (True, cmd)
        else:
            common_cmds = [x for x in COMMON_COMMANDS if x.startswith(cmd)]
            if len(common_cmds) > 0:
                return (False, common_cmds)
            regular_cmds = [x for x in self._commands_short if x.startswith(cmd)]
            if len(regular_cmds) > 0:
                return (False, regular_cmds)
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
