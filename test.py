import main
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

      def test_div1(self):
		#case 1, A is n integer B is an integer
		solution = self.app.get('/div?A=20&B=2')
		self.assertEqual(b'10.0', solution.data)

	def test_div2(self):

		#case 2, A is rational number and B is rational number p/q form
		solution = self.app.get('/div?A=3/2&B=22/4')
		self.assertEqual(b'0.2727272727272727', solution.data)

	def test_div3(self):

		#case 3, A is a float and B is a float
		solution = self.app.get('/div?A=0.089&B=102.22')
		self.assertEqual(b'0.0008706711015456858', solution.data)

	def test_div4(self):

		#case 4, when A is float and B is integer
		solution = self.app.get('/div?A=22.222&B=98')
		self.assertEqual(b'0.22675510204081634', solution.data)

	def test_div5(self):

		#case 5, when A is integer and B is float
		solution = self.app.get('/div?A=10&B=2.2')
		self.assertEqual(b'4.545454545454546', solution.data)

	def test_div6(self):

		#case 6, when A is fraction p/q and B is an integer
		solution = self.app.get('/div?A=12&B=100')
		self.assertEqual(b'0.12', solution.data)

	def test_div7(self):

		#case 7, when A is an integer and B is a fraction p/q
		solution = self.app.get('/div?A=12&B=2/3')
		self.assertEqual(b'18.0', solution.data)

	def test_div8(self):

		#case 8, when A input is an alphabet(non integer) and B is integer
		solution = self.app.get('/div?A=harish&B=12')
		self.assertEqual(b'0.0', solution.data)#non integer type considered as not valid , in this case which is zero

	def test_div9(self):

		#case 9, when A input is an integer and B input is an alphabet
		solution = self.app.get('/div?A=22&B=kumar')
		self.assertEqual(b'None', solution.data)
		#when one input is alphabet and other input be any number, whether rational , integer, fraction ultimately the result will be the input which was an integer

if __name__ == '__main__':
    unittest.main()
