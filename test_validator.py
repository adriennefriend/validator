# tests for validator.py project

import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO
from textwrap import dedent

from validator import main

# Make a Test class; name it the name of the thing you're testing
# We want to test the entire CLI
# an Acceptance or functional test that goes end to end
# Doesn't test one individual function; but rather main()


class ValidatorProgramTests(unittest.TestCase):
    # write a test for the empty case
    def test_user_entered_letter_a_instead_of_entering_URLs(self):
        "Test for when user enters the letter a instead of URLs"
        what_is_printed_to_user = self.run_program(user_entered_input="a")
        aspirational_printed_output = dedent("""\
            C'mon let's check some urls

            Hey, type some comma-separated urls! > a

            Handling a
            Exception! The error is: Invalid URL 'a': No schema supplied. Perhaps you meant http://a?

            Return value is: None\n""")
        self.assertEqual(what_is_printed_to_user, aspirational_printed_output)

    def test_user_entered_a_well_formed_URL_that_returns_a_bad_status_code(self):
        "It does what we called it."
        what_is_printed_to_user = self.run_program(user_entered_input="http://httpbin.org/status/404")
        aspirational_printed_output = "Error: 404: NOT FOUND"
        self.assertEqual(what_is_printed_to_user, aspirational_printed_output)

    def run_program(self, user_entered_input):
        "Run program with user-provided input and return printed output "
        def fake_input(prompt):
            print(prompt + user_entered_input)
            return user_entered_input
        with patch('builtins.input', fake_input):
            with redirect_stdout(StringIO()) as fake_output:
                main()
        return fake_output.getvalue()


if __name__ == '__main__':
    unittest.main()