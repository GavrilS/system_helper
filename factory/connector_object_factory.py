"""
Generic factory class for creating object to connect to a remote system. The different builder objects
represent the different os system we may want to connect to and execute remote commands on.
"""


class ConnectorObjectFactory:
    def __init__(self):
        self.builders = {}

    def register_builder(self, key, builder):
        self.builders[key] = builder

    def create(self, key, **kwargs):
        builder = self.builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)
