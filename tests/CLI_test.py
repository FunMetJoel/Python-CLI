import unittest
from custCLI.CLI import CLI, Command, Parameter, DataType


class CommandTestCase(unittest.TestCase):

    def checkParamsTrue_test(self):
        addFunction = lambda params: print(f"Adding {params[0]} and {params[1]} gives {params[0] + params[1]}")
        addCommand = Command("add", "Adds two numbers", addFunction, [Parameter("num1", "First number", DataType.FLOAT), Parameter("num2", "Second number", DataType.FLOAT)])
        result = addCommand.checkParams([1, 2])
        self.assertEqual(result, True)
    
    def checkParamsFalse_test(self):
        addFunction = lambda params: print(f"Adding {params[0]} and {params[1]} gives {params[0] + params[1]}")
        addCommand = Command("add", "Adds two numbers", addFunction, [Parameter("num1", "First number", DataType.FLOAT), Parameter("num2", "Second number", DataType.FLOAT)])
        result = addCommand.checkParams(["1", "2"])
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()