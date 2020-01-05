import main
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()
	
	
	def testint(self):
            fed =  self.app.get('/mul?A=3&B=2')
            self.assertEqual(b'6.0', fed.data)
            self.assertNotEqual(b'9.0',fed.data)
        def testfloat(self):
            fed =  self.app.get('/mul?A=3.5&B=2.6')
            self.assertEqual(b'9.1', fed.data)
        def testfrac(self):
            fed =  self.app.get('/mul?A=5/3&B=2/4')
            self.assertEqual(b'0.833', fed.data)
        def testneg(self):
            fed =  self.app.get('/mul?A=8.2&B=-4.3')
            self.assertEqual(b'-35.26', fed.data)


if __name__ == '__main__':
    unittest.main()
