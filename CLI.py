from enum import Enum

class DataTypes(Enum):
    STRING = "str"
    INTEGER = "int"
    FLOAT = "float"
    BOOLEAN = "bool"

class Parameter():
    def __init__(self, name:str, description:str, dataType:DataTypes = DataTypes.STRING):
        self.name = name
        self.description = description
        self.dataType = dataType

class Command():
    def __init__(self, name:str, description:str, function, params:list[Parameter] = []):
        self.name = name
        self.description = description
        self.function = function
        self.params = params

    def run(self):
        self.function(self.params)

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
                cmd.run()
                return
        print(f"Command '{command}' not found")


if __name__ == '__main__':

    def test(input):
        print("Functie is gerunt:", input)

    cmd = Command("TEST", "test command", test, [Parameter("paramTest", "test parameter", DataTypes.STRING)])
    
    cli = CLI(commands=[cmd])
    cli.printHeader()
    while True:
        cli.newCommand()