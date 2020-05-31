import main
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()
	
	def test_mul1(self):
		#case 1, A is n integer B is an integer
		solution = self.app.get('/mul?A=20&B=2')
		self.assertEqual(b'40.0', solution.data)

	def test_mul2(self):

		#case 2, A is rational number and B is rational number p/q form
		solution = self.app.get('/mul?A=3/2&B=22/4')
		self.assertEqual(b'8.25', solution.data)

	def test_mul3(self):

		#case 3, A is a float and B is a float
		solution = self.app.get('/mul?A=0.00089&B=100000.00')
		self.assertEqual(b'89.0', solution.data)

	def test_mul4(self):

		#case 4, when A is float and B is integer
		solution = self.app.get('/mul?A=22.222&B=98')
		self.assertEqual(b'2177.756', solution.data)

	def test_mul5(self):

		#case 5, when A is integer and B is float
		solution = self.app.get('/mul?A=1000&B=9.99')
		self.assertEqual(b'9990.0', solution.data)

	def test_mul6(self):

		#case 6, when A is fraction p/q and B is an integer
		solution = self.app.get('/mul?A=11&B=99')
		self.assertEqual(b'1089.0', solution.data)

	def test_mul7(self):

		#case 7, when A is an integer and B is a fraction p/q
		solution = self.app.get('/mul?A=23&B=9/13')
		self.assertEqual(b'15.923076923', solution.data)

	def test_mul8(self):

		#case 8, when A input is an alphabet(non integer) and B is integer
		solution = self.app.get('/mul?A=harish&B=22')
		self.assertEqual(b'0.0', solution.data)#non integer type considered as not valid , in this case which is zero

if __name__ == '__main__':
    unittest.main()
