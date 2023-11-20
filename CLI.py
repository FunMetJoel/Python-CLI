from enum import Enum

class DataType(Enum):
    STRING = "str"
    INTEGER = "int"
    FLOAT = "float"
    BOOLEAN = "bool"

class Parameter():
    def __init__(self, name:str, description:str, dataType:DataType = DataType.STRING):
        self.name = name
        self.description = description
        self.dataType = dataType

class Command():
    def __init__(self, name:str, description:str, function, params:list[Parameter] = []):
        self.name = name
        self.description = description
        self.function = function
        self.params = params

    def checkParams(self, params):
        for i in range(len(params)):
            if self.params[i].dataType == DataType.STRING:
                continue
            elif self.params[i].dataType == DataType.INTEGER:
                try:
                    params[i] = int(params[i])
                except ValueError:
                    print(f"Parameter '{params[i]}' is not a valid integer")
                    return False
            elif self.params[i].dataType == DataType.FLOAT:
                try:
                    params[i] = float(params[i])
                except ValueError:
                    print(f"Parameter '{params[i]}' is not a valid float")
                    return False
            elif self.params[i].dataType == DataType.BOOLEAN:
                if params[i].lower() == "true":
                    params[i] = True
                elif params[i].lower() == "false":
                    params[i] = False
                else:
                    print(f"Parameter '{params[i]}' is not a valid boolean")
                    return False
        return True

    def parceParams(self, params):
        for i in range(len(params)):
            if self.params[i].dataType == DataType.STRING:
                continue
            elif self.params[i].dataType == DataType.INTEGER:
                params[i] = int(params[i])
            elif self.params[i].dataType == DataType.FLOAT:
                params[i] = float(params[i])
            elif self.params[i].dataType == DataType.BOOLEAN:
                if params[i].lower() == "true":
                    params[i] = True
                elif params[i].lower() == "false":
                    params[i] = False
        return params

    def run(self, params):
        if len(params) != len(self.params):
            print(f"Wrong number of parameters for command '{self.name}'")
            return
        
        if not self.checkParams(params):
            return
        
        self.function(self.parceParams(params))

    def helpCommand(self):
        print(f"{self.name} - {self.description}")
        for param in self.params:
            print(f"\t{param.name} - {param.description} ({param.dataType.value})")

class CLI():
    def __init__(self, CLIname:str = "CLI", CLIdescription:str = "Command Line Interface", commands:list[Command] = []):
        self.commands = commands
        self.CLIname = CLIname
        self.CLIdescription =  CLIdescription
        self.header = f"""\n-- {CLIname} --\n{CLIdescription}\n"""

    def printHeader(self):
        print(self.header)

    def newCommand(self):
        self.parceCommand(input(">> "))
    
    def parceCommand(self, command):
        basecommand = command.split(" ")[0]
        params = command.split(" ")[1:]
        if basecommand == "help":
            self.helpCommand(params)
        else:
            self.runCommand(basecommand, params)
    
    def helpCommand(self, params):
        if len(params) == 0:
            print(self.header)
            print("Commands:")
            for cmd in self.commands:
                print(f"\t{cmd.name} - {cmd.description}")
        else:
            for cmd in self.commands:
                if cmd.name == params[0]:
                    cmd.helpCommand()
                    return
            print(f"Command '{params[0]}' not found")

    def runCommand(self, command, params):
        for cmd in self.commands:
            if cmd.name == command:
                cmd.run(params)
                return
        print(f"Command '{command}' not found")
