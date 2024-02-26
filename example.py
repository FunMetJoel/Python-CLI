from custCLI.CLI import CLI, Command, Parameter, Option, DataType

cli = CLI(
    "Test CLI", 
    "Test CLI description"
)

def addCommand(params, options):
    if '-v' in options:
        print(f"RUN addCommand with")
        print(f"\tparams: {params}")
        print(f"\toptions: {options}")

    num1 = int(params[0])
    num2 = int(params[1])
    result = num1 + num2
    if '-v' in options:
        print(f"{num1} + {num2} = {result}")
    else:
        print(f"{result}")

cli.commands.append( Command(
    "add", 
    "adds numbers together", 
    addCommand, 
    [
        Parameter("param1", "param1 description", DataType.STRING), 
        Parameter("param2", "param2 description", DataType.INTEGER)
    ],
    [
        Option("-v", ["-verbose"], "Verbose")
    ] 
) )

def testFunction2(params):
    print("testFunction2")
    for param in params:
        print(f"\t{param.name} - {param.dataType.value} - {param.value}")

command2 = Command("test2", "test2 description", testFunction2, [Parameter("param1", "param1 description", DataType.STRING), Parameter("param2", "param2 description", DataType.INTEGER)])

def testFunction3(params):
    print("testFunction3")
    for param in params:
        print(f"\t{param.name} - {param.dataType.value} - {param.value}")

command3 = Command("test3", "test3 description", testFunction3, [Parameter("param1", "param1 description", DataType.STRING), Parameter("param2", "param2 description", DataType.INTEGER)])

cli.printHeader()

while True:
    cli.newCommand()
