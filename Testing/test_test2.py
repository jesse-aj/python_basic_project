import unittest 
import test2

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(test2.add(10, 25), 35)
        self.assertEqual(test2.add(-1, 1), 0)
        self.assertEqual(test2.add(-1, -1), -2)

    def test_substract(self):
        self.assertEqual(test2.substract(10, 5), 5)
        self.assertEqual(test2.substract(-1, 1), -2)
        self.assertEqual(test2.substract(-1, -1), 0)

    def test_multiple(self):
        self.assertEqual(test2.multiple(10, 5), 50)
        self.assertEqual(test2.multiple(-1, 1), -1)
        self.assertEqual(test2.multiple(-1, -1), 1)

    def test_division(self):
        self.assertEqual(test2.division(10, 5), 2)
        self.assertEqual(test2.division(-1, 1), -1)
        self.assertEqual(test2.division(-1, -1), 1)
        self.assertEqual(test2.division(5, 2), 2.5)
         



        with self.assertRaises(ValueError):
            test2.division(10, 0)










if __name__ == "__main__":
    unittest.main(argv=[''],verbosity=2, exit=False)