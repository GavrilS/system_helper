from pypsexec.client import Client


class WindowsConnector():

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def create_connection(self):
        c = Client(self.host, username=self.user,
                   password=self.password, encrypt=False)
        c.connect()
        print("Connection set up properly!")
        return c

    def execute_command(self, command, executable='cmd.exe'):
        try:
            c = self.create_connection()
            c.create_service()
            stdout, stderr, rc = c.run_executable(
                executable, arguments=command)
            self.close_connection(c)
            return stdout, stderr, rc

        except Exception as e:
            print("Could not execute command: ", str(e))

    def close_connection(self, c):
        c.cleanup()
        c.remove_service()
        c.disconnect()
        print("Connection removed!")
