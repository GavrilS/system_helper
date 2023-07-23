from sys import platform
import sys

# for line in sys.path:
#     print(line)

# sys.path.append('/mnt/c/Users/Gari/git/system_helper')
# sys.path.append('/mnt/c/Users/Gari/git/system_helper')


# for line in sys.path:
#     print(line)

from factory.connectors.connector_factory import ConnectorFactory

test_command = 'systemctl list-units --type=service'


def main():
    print(platform)

    connector = ConnectorFactory.get_connector()
    output, err, _ = connector.execute_command(test_command)
    print("********************")
    print('Output: ', output)
    print('********************')
    print('Error: ', err)
    print('********************')
    print('Other: ', _)



if __name__ == '__main__':
    main()
