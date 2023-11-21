from custCLI.CLI import CLI, Command, Parameter, DataType

def addFunction(params):
    print("Adding " + str(params[0]) + ", and " + str(params[1]) + " gives " + str(params[0] + params[1]))

addCommand = Command("add", "Adds two numbers", addFunction, [Parameter("num1", "First number", DataType.FLOAT), Parameter("num2", "Second number", DataType.FLOAT)])

def subFunction(params):
    print("Subtracting " + str(params[0]) + ", and " + str(params[1]) + " gives " + str(params[0] - params[1]))

subCommand = Command("sub", "Subtracts two numbers", subFunction, [Parameter("num1", "First number", DataType.FLOAT), Parameter("num2", "Second number", DataType.FLOAT)])

def mulFunction(params):
    print("Multiplying " + str(params[0]) + " and " + str(params[1]) + " gives " + str(params[0] * params[1]))

mulCommand = Command("mul", "Multiplies two numbers", mulFunction, [Parameter("num1", "First number", DataType.FLOAT), Parameter("num2", "Second number", DataType.FLOAT)])

def divFunction(params):
    print("Dividing " + str(params[0]) + " and " + str(params[1]) + " gives " + str(params[0] / params[1]))

divCommand = Command("div", "Divides two numbers", divFunction, [Parameter("num1", "First number", DataType.FLOAT), Parameter("num2", "Second number", DataType.FLOAT)])

def powFunction(params):
    print(str(params[0]) + " to the power of " + str(params[1]) + " gives " + str(params[0] ** params[1]))

powCommand = Command("pow", "Raises a number to a power", powFunction, [Parameter("num1", "Number", DataType.FLOAT), Parameter("num2", "Power", DataType.FLOAT)])

def sqrtFunction(params):
    print("The square root of " + str(params[0]) + " is " + str(params[0] ** 0.5))

sqrtCommand = Command("sqrt", "Finds the square root of a number", sqrtFunction, [Parameter("num1", "Number", DataType.FLOAT)])

commands = [addCommand, subCommand, mulCommand, divCommand, powCommand, sqrtCommand]

cli = CLI("Maths CLI", "A CLI for doing maths", commands)
cli.printHeader()

while True:
    cli.newCommand()
    