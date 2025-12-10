import unittest



def sum(a,b):
    return a + b

class SumTest(unittest.TestCase):
    
    #Arrang can be here so it can be used for multiple classes
    def setUp(self):
        print("SETUP Called...")
        self.a = 10
        self.b = 20
    def tearDown(self):
        self.a = 0
        self.b = 0
        print("TEARDOWN CALLED")
       

    def test_sum_func1(self):
        print("TEST - 1 Called...")
        #Act
        results = sum(self.a,self.b)

        #Assert
        self.assertEqual(results, self.a + self.b)
        

    def test_sum_func2(self):
        print("TEST - 2 Called...")
        #Act
        results = sum(self.a,self.b)

        #Assert
        self.assertEqual(results, self.a + self.b)
        







if __name__ == "__main__":
    unittest.main()
    


