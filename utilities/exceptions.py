CMD_ARGS_ERROR = 'Too many arguments were passed for this command! Ask for help to see how the command is used!'

class CommandNotFound(Exception):
    """
    Exception raised for non-existing command passed by the user.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="The command does not exist!"):
        self.message = message
        super().__init__(self.message)



class TooManyCommandArgs(Exception):
    """
    Exception raised when too many commands arguments are passed to a command.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message=CMD_ARGS_ERROR):
        self.message = message
        super().__init__(self.message)
        