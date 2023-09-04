import sys

# exit()

# for line in sys.path:
#     print(line)

# sys.path.append('/mnt/c/Users/Gari/git/system_helper')
sys.path.append('C:\\Users\\Gari\\git\\system_helper')

from handlers.user_operations import UserUI

# for line in sys.path:
#     print(line)


def main():
    user_ui = UserUI()
    flag = True
    while flag:
        user_ui.get_input()
    




if __name__ == '__main__':
    main()
