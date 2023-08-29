from sys import platform
import sys
import platform
from factory.commands.system_commands import SystemCommands, os_command_factory

OS = platform.platform()
OS = 'Windows'

print('OS: ', OS)

# exit()

# for line in sys.path:
#     print(line)

# sys.path.append('/mnt/c/Users/Gari/git/system_helper')
# sys.path.append('/mnt/c/Users/Gari/git/system_helper')
sys.path.append('C:\\Users\\Gari\\git\\system_helper')


for line in sys.path:
    print(line)

from factory.connectors.connector_factory import ConnectorFactory

# test_command = 'systemctl list-units --type=service'
# test_command = 'net start'
# test_command = 'sc query state= all'
test_command = 'powershell -Command Get-Service'


def main():
    # print(platform)

    # connector = ConnectorFactory.get_connector()
    # # connector = ConnectorFactory.get_connector(key='windows', host='172.29.224.1', user='Gari', password='qwerty')
    # # connector = ConnectorFactory.get_connector(key='windows', host='172.29.224.1', user='Gari', password='')
    # output, err, _ = connector.execute_command(test_command)
    # print("********************")
    # print('Output: ', output)
    # print('********************')
    # print('Error: ', err)
    # print('********************')
    # print('Other: ', _)

    # with open('core\\test\\service_state.txt', 'w') as f:
    #     f.write('Command output:' + '*'*40)
    #     f.write(str(output))
    #     f.write('Command error:' + '*'*40)
    #     f.write(str(err))
    #     f.write('Extra:' + '*'*40)
    #     f.write(str(_))

    os_command_list = os_command_factory.get_os_type_list(OS)
    system_commands = SystemCommands(os_command_list)
    print('1 Added the relevant classes')
    system_commands.list_commands()
    print('2. After showing commands')




if __name__ == '__main__':
    main()
