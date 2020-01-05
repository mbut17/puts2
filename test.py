import main
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()
        
        def testint(self):
            fed =  self.app.get('/sub?A=4&B=10')
            self.assertEqual(b'-6.0', fed.data)
            self.assertNotEqual(b'6.0',fed.data)
        def testfloat(self):
            fed = self.app.get('/sub?A=3.5&B=7.5')
            self.assertEqual(b'-4.0', fed.data)
            self.assertNotEqual(b'-1',fed.data)
        def testfrac(self):
            fed =  self.app.get('/sub?A=7/5&B=4/3')
            self.assertEqual(b'-0.067', fed.data)
        def testneg(self):
            fed =  self.app.get('/sub?A=2.3&B=-3.3')
            self.assertEqual(b'5.6', fed.data)
        

if __name__ == '__main__':
    unittest.main()
