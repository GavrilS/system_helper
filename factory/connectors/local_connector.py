import sys


class LocalConnector():

    def __init__(self):
        pass

    def execute_command(self, command):
        os = sys.platform()
        if 'linux' in os:
            self.execute_linux_command(command)
        elif 'win32' in os:
            self.execute_win_command(command)

    def execute_linux_command(command):
        pass

    def execute_win_command(command):
        pass
