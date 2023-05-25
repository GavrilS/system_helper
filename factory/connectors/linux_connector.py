import paramiko


class LinuxConnector():

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def create_connection(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.host, username=self.user,
                    password=self.password)
        # self.ssh = ssh
        print("Connection created!")
        return ssh

    def execute_command(self, command):
        try:
            ssh = self.create_connection()
            shell = ssh.invoke_shell()
            # shell.send(command + "\n")
            stdin, stdout, stderr = shell.exec_command(command)
            self.close_connection(ssh)
            return stdout, stderr, stdin
        except Exception as e:
            print(f"Command - {command} failed:\n", str(e))

    def close_connection(self, ssh):
        ssh.close()
        print('Connection closed!')
