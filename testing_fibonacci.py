import unittest

from fibonacci import fibonacci

class testFibonacci(unittest.TestCase):
    def test_del_0(self):
        resultado = fibonacci(0)
        self.assertEqual(resultado,0)

    def test_del_1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado,1)
    
    def test_del_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado,1)

    def test_del_3(self):
        resultado = fibonacci(3)
        self.assertEqual(resultado,2)

    def test_del_5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado,5)

    def test_del_6(self):
        resultado = fibonacci(6)
        self.assertEqual(resultado,8)

    def test_del_14(self):
        resultado = fibonacci(14)
        self.assertEqual(resultado,377)
    
    def test_del_20(self):
        resultado = fibonacci(20)
        self.assertEqual(resultado,6765)

    



unittest.main()