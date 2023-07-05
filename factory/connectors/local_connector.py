import subprocess


class LocalConnector():

    def __init__(self):
        pass

    def execute_command(self, command):
        command_args = command.split(' ')
        result = subprocess.run(command_args, capture_output=True, text=True)
        return result.stdout, result.stderr, ''
