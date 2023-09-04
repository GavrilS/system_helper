from utilities.exceptions import TooManyCommandArgs


MAX_CMD_WITH_ARGS = 2
MIN_CMD_ARGS = 1
CMD_ARGS_TEMPLATE = '--ARGS'


def split_command_args(cmd):
    split_cmd = cmd.split('--')
    if len(split_cmd) > MAX_CMD_WITH_ARGS:
        raise TooManyCommandArgs
    elif len(split_cmd) == MIN_CMD_ARGS:
        return split_cmd[0], None
    return split_cmd[0], split_cmd[1]


def format_final_command(cmd, args):
    final_cmd = cmd.replace(CMD_ARGS_TEMPLATE, args)
    return final_cmd



if __name__=='__main__':
    """
    Testing the methods for all posible cases
    """
    test_split_cmd1 = 'test command with args --arg_test'
    test_split_cmd2 = 'test command with multi args --arg1 --arg2'
    test_split_cmd3 = 'test command without args'
    test_format_cmd = ('test command --ARGS', 'test_argument')

    cmd1, args1 = split_command_args(test_split_cmd1)
    print(f"Test1: cmd1 -> {cmd1} : args1 -> {args1}")

    try:
        cmd2, args2 = split_command_args(test_split_cmd2)
        print(f"Test2: cmd2 -> {cmd2} : args2 -> {args2}")
    except TooManyCommandArgs as e:
        print('Test2 encountered an error: ', str(e))

    cmd3, args3 = split_command_args(test_split_cmd3)
    print(f"Test3: cmd3 - > {cmd3} : args3 -> {args3}")

    formatted_cmd = format_final_command(cmd=test_format_cmd[0], args=test_format_cmd[1])
    print('Test3: Formatted command -> ', formatted_cmd)
