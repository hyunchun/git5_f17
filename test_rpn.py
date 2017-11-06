import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        # test 1
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
        
        # test 2
        try:
            result = rpn.calculate("4 5 +")
            self.assertEqual(10, result)
        except:
            print("")      
        else:
            print("failed")
        
        # test 3
        result = rpn.calculate("0 0 +")
        self.assertEqual(0, result)

    def test_subtract(self):
        # test 1
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)

        # test 2
        result = rpn.calculate("8 8 -")
        self.assertEqual(0, result)

        # test 3
        try: 
            result = rpn.calculate("8 9 -")
            self.assertEqual(1, result)
        except:
            print("")
        else:
            print("failed")

    def test_multiple_operation(self):
        # test 1
        result = rpn.calculate("5 3 - 2 +")
        self.assertEqual(4, result)
        
        # test 2
        result = rpn.calculate("0 0 + 1 + 2 + 3 -")
        self.assertEqual(0, result)
