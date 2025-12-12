import unittest
import datacamp


class Test_func(unittest.TestCase):

    def test_calcSquare(self):
        self.assertEqual(datacamp.calcSquare(3), 9)





if __name__ == "__main__":
    unittest.main(argv=[''],verbosity=2, exit=False)