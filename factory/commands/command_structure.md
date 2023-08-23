# Classes:

1. System command is the class that acts as the interface between the command logic and the user input/output

   - List the available commands for the os
   - Loads the commands available based on the os

2. Concrete os class:
   - For each implemented os it represents an enum of available commands, which are loaded by the system command class
