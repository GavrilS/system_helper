from pypsexec.client import Client


class WindowsConnector():

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.c = None
        self.stdout = None
        self.stderr = None
        self.rc = None

    def create_connection(self):
        try:
            c = Client(self.host, username=self.user,
                       password=self.password, encrypt=False)
            c.connect()
            self.c = c
            print("Connection set up properly!")
        except Exception as e:
            print("Exception is ", str(e))

    def execute_command(self, command, executable='cmd.exe'):
        c = self.c
        if not c:
            print("Connection was not set properly!")
            return None
        try:
            c.create_service()
            self.stdout, self.stderr, self.rc = c.run_executable(
                executable, arguments=command)

        except Exception as e:
            print("Could not execute command: ", str(e))
