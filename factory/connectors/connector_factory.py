from factory.connectors.linux_connector import LinuxConnector
from factory.connectors.windows_connector import WindowsConnector
from factory.connectors.local_connector import LocalConnector

class ConnectorFactory():

    def __init__(self):
        pass


    def get_connector(key='local', host='', user='', password=''):
        if 'local' in key.lower():
            return LocalConnector()
        elif 'windows' in key.lower():
            return WindowsConnector(host, user, password)
        elif 'linux' in key.lower():
            return LinuxConnector(host, user, password) 
