import paramiko


class LinuxConnector():

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.ssh = None
        self.stdin = None
        self.stdout = None
        self.stderr = None

    def create_connection(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=self.host, username=self.user,
                        password=self.password)
            self.ssh = ssh
        except Exception as e:
            print("Couldn't set up conenction to the server: ", str(e))

    def execute_command(self, command):
        try:
            shell = self.ssh.invoke_shell()
            # shell.send(command + "\n")
            self.stdin, self.stdout, self.stderr = shell.exec_command(command)
        except Exception as e:
            print(f"Command - {command} failed:\n", str(e))

    def close_connection(self):
        try:
            self.ssh.close()
        except Exception as e:
            print('Failed to close the connection:\n', str(e))
