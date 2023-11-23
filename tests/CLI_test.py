import unittest
from custCLI.CLI import CLI, Command, Parameter, DataType


class CommandTestCase(unittest.TestCase):

    def test_test(self):
        """Test 0 multiplied by 2"""

        # 0 multiplied by 2 return 0
        result = int(0 * 2)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()