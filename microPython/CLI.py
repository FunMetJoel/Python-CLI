"""
This is a python library for creating a CLI with custom commands and parameters
Create by FunMetJoel
"""

import re

class DataType:
    STRING = "str"
    INTEGER = "int"
    FLOAT = "float"
    BOOLEAN = "bool"

class Parameter():
    def __init__(self, name:str, description:str, dataType:str = DataType.STRING, defaultValue = None):
        self.name = name
        self.description = description
        self.dataType = dataType
        self.defaultValue = defaultValue

class Command():
    def __init__(self, name:str, description:str, function, params:list[Parameter] = []):
        self.name = name
        self.description = description
        self.function = function
        self.params = params

    def checkParams(self, params):
        if not self.checkParamLength(params):
            return False
        if not self.checkParamDatatypes(params):
            return False
        return True
    
    def checkParamLength(self, params):
        minParams = sum(1 for param in self.params if param.defaultValue == None)
        maxParams = len(self.params)
        if len(params) < minParams:
            print("Not enouth parameters for command '" + self.name + "'")
            return False
        if len(params) > maxParams:
            print("Too many parameters for command '" + self.name + "'")
            return False
        return True

    def checkParamDatatypes(self, params):
        for i in range(len(params)):
            if self.params[i].dataType == DataType.STRING:
                continue
            elif self.params[i].dataType == DataType.INTEGER:
                try:
                    params[i] = int(params[i])
                except ValueError:
                    print("Parameter '" + str(params[i]) + "' is not a valid integer")
                    return False
            elif self.params[i].dataType == DataType.FLOAT:
                try:
                    params[i] = float(params[i])
                except ValueError:
                    print("Parameter '" + str(params[i]) + "' is not a valid float")
                    return False
            elif self.params[i].dataType == DataType.BOOLEAN:
                if params[i].lower() == "true":
                    params[i] = True
                elif params[i].lower() == "false":
                    params[i] = False
                else:
                    print("Parameter '" + str(params[i]) + "' is not a valid boolean")
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
        if not self.checkParams(params):
            return
        
        nParams = self.parceParams(params)

        for i in range(len(self.params)):
            if i >= len(nParams):
                nParams.append(self.params[i].defaultValue)
        self.function(nParams)

    def helpCommand(self):
        print(self.name, "-", self.description)
        for param in self.params:
            print("\t", param.name, "-", param.description, "(", str(param.dataType.value),")")

class CLI():
    def __init__(self, CLIname:str = "CLI", CLIdescription:str = "Command Line Interface", commands:list[Command] = []):
        self.commands = commands
        self.CLIname = CLIname
        self.CLIdescription =  CLIdescription
        self.header = """
-- """ + CLIname + """ --
""" + CLIdescription + """
        """

    def printHeader(self):
        print(self.header)

    def newCommand(self):
        self.parceCommand(input(">> "))

    def splitParams(self, command):
        params = []
        for param in re.findall(r'\"(.+?)\"|(\S+)', command):
            if param[0] != "":
                params.append(param[0])
            else:
                params.append(param[1])
        return params
    
    def parceCommand(self, command):
        basecommand = command.split(" ",1)[0]
        params = []
        if len(command.split(" ")) > 1:
            params = self.splitParams(command.split(" ",1)[1])
        if basecommand == "help":
            self.helpCommand(params)
        else:
            self.runCommand(basecommand, params)
    
    def helpCommand(self, params):
        if len(params) == 0:
            print(self.header)
            print("Commands:")
            for cmd in self.commands:
                print(cmd.name, "-", cmd.description)
        else:
            for cmd in self.commands:
                if cmd.name == params[0]:
                    cmd.helpCommand()
                    return
            print("Command '" + str(params[0]) + "' not found")

    def runCommand(self, command, params):
        for cmd in self.commands:
            if cmd.name == command:
                cmd.run(params)
                return
        print(f"Command '{command}' not found")

# How to use:
# from CLI import CLI, Command, Parameter, DataType
# 
# def testFunction(params):
#     print("testFunction")     
#     for param in params:
#         print(f"\t{param}")
#
# command1 = Command("test1", "test1 description", testFunction, [Parameter("param1", "param1 description", DataType.STRING), Parameter("param2", "param2 description", DataType.INTEGER)])
#
# def testFunction2(params):
#     print("testFunction2")
#     for param in params:
#         print(f"\t{param.name} - {param.dataType.value} - {param.value}")
#
# command2 = Command("test2", "test2 description", testFunction2, [Parameter("param1", "param1 description", DataType.STRING), Parameter("param2", "param2 description", DataType.INTEGER)])
#
# cli = CLI("Test CLI", "Test CLI description", [command1, command2])
# cli.printHeader()
#
# while True:
#     cli.newCommand()