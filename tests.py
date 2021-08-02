from unittest.mock import patch
import unittest

from password_generator_2 import ask_user, password_generator

class PasswordsTestCase(unittest.TestCase):

    def test_get_input_processed_input_correctly(self):
        user_input = ["7"]
        expected_input = 7
        with patch('builtins.input', side_effect=user_input):
            user_in = ask_user()
        self.assertEqual(user_in, expected_input)

    def test_answer(self):
        expected_pass_len = 7
        with patch('builtins.input'):
            gen = password_generator(7)
        self.assertEqual(len(gen), expected_pass_len)


if __name__ == '__main__':
    unittest.main()
