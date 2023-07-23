# system_helper

A tool to help clean and control the operating system.

1. Build the connector class:

- multiple cases for wether the remote system is linux, windows or other; we can use the factory method with a common interface to give us the required implementation for the system we are trying to connect to
- factory method in python example: https://realpython.com/factory-method-python/


2. Make a list of commands to:
    - list available services/processes on the target machine and what resources are they using
    - determine which are set to start on start-up
    - make a list of which are necessary for the os to run normally
    - create models for the different commands based on use case and os
    - automate the usage of the model in the application
