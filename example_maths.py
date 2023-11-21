from custCLI.CLI import CLI, Command, Parameter, DataType

def addFunction(params):
    print(f"Adding {params[0]} and {params[1]} gives {params[0] + params[1]}")

addCommand = Command("add", "Adds two numbers", addFunction, [Parameter("num1", "First number", DataType.FLOAT), Parameter("num2", "Second number", DataType.FLOAT)])

def subFunction(params):
    print(f"Subtracting {params[0]} and {params[1]} gives {params[0] - params[1]}")

subCommand = Command("sub", "Subtracts two numbers", subFunction, [Parameter("num1", "First number", DataType.FLOAT), Parameter("num2", "Second number", DataType.FLOAT)])

def mulFunction(params):
    print(f"Multiplying {params[0]} and {params[1]} gives {params[0] * params[1]}")

mulCommand = Command("mul", "Multiplies two numbers", mulFunction, [Parameter("num1", "First number", DataType.FLOAT), Parameter("num2", "Second number", DataType.FLOAT)])

def divFunction(params):
    print(f"Dividing {params[0]} and {params[1]} gives {params[0] / params[1]}")

divCommand = Command("div", "Divides two numbers", divFunction, [Parameter("num1", "First number", DataType.FLOAT), Parameter("num2", "Second number", DataType.FLOAT)])

def powFunction(params):
    print(f"{params[0]} to the power of {params[1]} gives {params[0] ** params[1]}")

powCommand = Command("pow", "Raises a number to a power", powFunction, [Parameter("num1", "Number", DataType.FLOAT), Parameter("num2", "Power", DataType.FLOAT)])

def sqrtFunction(params):
    print(f"The square root of {params[0]} is {params[0] ** 0.5}")

sqrtCommand = Command("sqrt", "Finds the square root of a number", sqrtFunction, [Parameter("num1", "Number", DataType.FLOAT)])

commands = [addCommand, subCommand, mulCommand, divCommand, powCommand, sqrtCommand]

cli = CLI("Maths CLI", "A CLI for doing maths", commands)
cli.printHeader()

while True:
    cli.newCommand()
    