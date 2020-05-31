import main
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()
        
       def test_sub1(self):
		#case 1, A is n integer B is an integer
		solution = self.app.get('/sub?A=6&B=2')
		self.assertEqual(b'4.0', solution.data)

	def test_sub2(self):

		#case 2, A is rational number and B is rational number p/q form
		solution = self.app.get('/sub?A=3/2&B=1/2')
		self.assertEqual(b'1.0', solution.data)

	def test_sub3(self):

		#case 3, A is a float and B is a float
		solution = self.app.get('/sub?A=10.2&B=1.002')
		self.assertEqual(b'9.198', solution.data)

	def test_sub4(self):

		#case 4, when A is float and B is integer
		solution = self.app.get('/sub?A=22.222&B=2')
		self.assertEqual(b'20.222', solution.data)

	def test_sub5(self):

		#case 5, when A is integer and B is float
		solution = self.app.get('/sub?A=12&B=1.111')
		self.assertEqual(b'10.889', solution.data)

	def test_sub6(self):

		#case 6, when A is fraction p/q and B is an integer
		solution = self.app.get('/sub?A=1/2&B=12')
		self.assertEqual(b'-11.5', solution.data)

	def test_sub7(self):

		#case 7, when A is an integer and B is a fraction p/q
		solution = self.app.get('/sub?A=3&B=2/10')
		self.assertEqual(b'2.8', solution.data)
)
        

if __name__ == '__main__':
    unittest.main()
