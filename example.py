from CLI import CLI, Command, Parameter, DataType

def testFunction(params):
    print("testFunction")
    for param in params:
        print(f"\t{param}")

command1 = Command("test1", "test1 description", testFunction, [Parameter("param1", "param1 description", DataType.STRING), Parameter("param2", "param2 description", DataType.INTEGER)])

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

cli = CLI("Test CLI", "Test CLI description", [command1, command2, command3])
cli.printHeader()

while True:
    cli.newCommand()
