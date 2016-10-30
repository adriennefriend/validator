# tests for validator.py project

import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO

from validator import main

# Make a Test class; name it the name of the thing you're testing
# We want to test the entire CLI
# an Acceptance or functional test that goes end to end
# Doesn't test one individual function; but rather main()


class ValidatorProgramTests(unittest.TestCase):
    # write a test for the empty case
    def test_user_pressed_return_instead_of_entering_URLs(self):
        "Test for when user presses return or enter instead of entering a URL"
        what_is_printed_to_user = self.run_program(user_entered_input="")
        aspirational_printed_output = "Wait a sec! I think you forgot to enter something."
        self.assertEqual(what_is_printed_to_user, aspirational_printed_output)

    def test_user_entered_a_well_formed_URL_that_returns_a_bad_status_code(self):
        "It does what we called it."
        what_is_printed_to_user = self.run_program(user_entered_input="http://httpbin.org/status/404")
        aspirational_printed_output = "Error: 404: NOT FOUND"
        self.assertEqual(what_is_printed_to_user, aspirational_printed_output)

    def run_program(self, user_entered_input):
        "Run program with user-provided input and return printed output "
        with patch('builtins.input', side_effect=[user_entered_input]):
            with redirect_stdout(StringIO()) as fake_output:
                main()
        return fake_output.getvalue()


if __name__ == '__main__':
    unittest.main()


# make the tests fail in an aspirational way :D