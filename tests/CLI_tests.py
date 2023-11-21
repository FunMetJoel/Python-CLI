import unittest
from custCLI import CLI, Command, Parameter, DataType


class CommandTestCase(unittest.TestCase):

    def testFunction(params):
        print("testFunction")
        for param in params:
            print(f"\t{param}")

    def setUp(self):
        self.multiplication = Command("test1", "test1 description", self.testFunction, [Parameter("param1", "param1 description", DataType.STRING), Parameter("param2", "param2 description", DataType.INTEGER)])

    def test_test(self):
        """Test 0 multiplied by 2"""

        # 0 multiplied by 2 return 0
        result = (0 * 2)
        self.assertEqual(result, 0)