import main
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

        def testint(self):
            fed =  self.app.get('/div?A=7&B=5')
            self.assertEqual(b'1.4', fed.data)
            self.assertNotEqual(b'0.0256',fed.data)
        def testfloat(self):
            fed =  self.app.get('/div?A=3.5&B=8.4')
            self.assertEqual(b'0.417', fed.data)
        def testfrac(self):
            fed =  self.app.get('/div?A=2/3&B=3/3')
            self.assertEqual(b'0.667', fed.data)
        def testneg(self):
            fed =  self.app.get('/div?A=5.4&B=-3.3')
            self.assertEqual(b'-1.636', fed.data)
        def testzerodiv(self):
            fed = self.app.get('/div?A=3/0&B=9')
            self.assertEqual(b'None',fed.data)

if __name__ == '__main__':
    unittest.main()
