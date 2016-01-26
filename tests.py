import unittest

class Test_Assignment_01(unittest.TestCase):
    """
    Below are a series of tests, some of which will fail.

    Automated testing will be performed when you submit a
    Pull Request and any time that you make any future
    modification to the file.

    If you get stuck, launch a Python interpreter (Python,
    iPython, or Jupyter Notebook) and copy a small block of
    code.

    For example, if the test reads:

    x = 'abcde'
    self.assertEqual(4, len(x))

    and you are unsure what len(x) might return, you can
    execute:

    >>> x = 'abcde'
    >>> len(x)
    5

    in any of the above interpreters.
    """
    
    def setUp(self):
        """
        Code called before every other test is run.
        """
        pass
    
    def test_assert_truth(self):
        """
        A test that will pass.
        """
        self.assertTrue(True)

    def test_assert_truth_with_a_message(self):
        """
        A test that will fail.
        """
        self.assertFalse(False, 'This should fail, please fix it.')

    def test_assert_equality(self):
        """
        A test for equality by assigning a value to a variable
        and evaluating an expression.
        """
        expected_value = 2
        truth_value = 1 + 1
        self.assertEqual(expected_value, truth_value)

    def test_what_are_these_types(self):
        """
        A test to know what the types of the previous fixes were
        """
        self.assertFalse(False, bool)

    def test_assert_string(self):
        """
        A test for evaluating an expression
        """
        my_string = 'Hello World'
        my_string_length = len(my_string)  # The expression
        self.assertEqual(11, my_string_length)

    def test_big_integers(self):
        """
        A test to explore notation of big integers.
        """
        x = 42000
        self.assertTrue(isinstance(x, int))

    def test_bigger_integers(self):
        """
        A test for bigger, or smaller integers
        """
        big = 1000000
        self.assertEqual(big, 1000000)
        self.assertTrue(type(big), int)

        small = .00001
        self.assertEqual(small, 0.00001)
        self.assertTrue(type(small), int)

    def test_type_conversion(self):
        """
        A series of tests to validate type conversion operations
        """
        i = 1
        self.assertTrue(type(i) == int)
        self.assertTrue(isinstance(i, int))  # These lines do the same type checking
        i = float(i)
        self.assertTrue(isinstance(i, float))
        i = str(i)
        self.assertFalse(type(i) == int)

    def test_type_conversion2(self):
        """
        A poorly named function to test converting strings to numeric types
        """
        k = "123"
        self.assertIsInstance(k, str)  # New assertion type that shortens previous calls
        k = float(k)
        self.assertEqual(123, k)  # Hmmm, note how this equality works across types

    def test_type_conversion_gotcha(self):
        """
        A test to show how rounding can get you
        """
        j = 3.9999
        self.assertTrue(int(j), int)
        self.assertEqual(int(j), 3)

    def tearDown(self):
        """
        Code called after ever other test is run.
        """
        pass

if __name__ == '__main__':
    unittest.main()
