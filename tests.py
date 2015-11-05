import unittest

class Test_Assignment_01(unittest.TestCase):
    
    def setUp(self):
        """
        Code called before every other test is run.
        """
        pass
    
    def test_pass(self):
        """
        A test that will pass.
        """
        self.assertTrue(True)

    def test_fail(self):
        """
        A test that will fail.
        """
        self.assertFalse(True)

    def tearDown(self):
        """
        Code called after ever other test is run.
        """
        pass

if __name__ == '__main__':
    unittest.main()
