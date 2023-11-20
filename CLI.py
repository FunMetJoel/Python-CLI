class CLI():
    def __init__(self, CLIname:str = "CLI", CLIdescription:str = "Command Line Interface"):
        self.commands = []
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
        print(basecommand,":", params)

class Command():
    def __init__(self, name:str, description:str, function, params:list = []):
        self.name = name
        self.description = description
        self.function = function
        self.params = params

    def run(self):
        self.function(self.params)

class Parameter():
    def __init__(self, name:str, description:str, dataType:str = "str"):
        self.name = name
        self.description = description
        self.dataType = dataType

if __name__ == '__main__':
    cli = CLI()
    cli.printHeader()
    cli.newCommand()