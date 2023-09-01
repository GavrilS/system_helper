

class CommandNotFound(Exception):
    """
    Exception raised for non-existing command passed by the user.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="The command does not exist!"):
        self.message = message
        super().__init__(self.message)
        