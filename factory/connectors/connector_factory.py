import LinuxConnector, LocalConnector, WindowsConnector

class ConnectorFactory():

    def __init__(self):
        pass


    def get_connector(key='local', host='', user='', password=''):
        if 'local' in key.lower():
            return LocalConnector()
        elif 'windows' in key.lower():
            return WindowsConnector(host, user, password)
        else:
            return LinuxConnector(host, user, password) 
