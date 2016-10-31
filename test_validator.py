# tests for validator.py project

import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO
from textwrap import dedent

from validator import main, validate_urls

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
        aspirational_printed_output = dedent("""\
            C'mon let's check some urls

            Hey, type some comma-separated urls! > http://httpbin.org/status/404

            Handling http://httpbin.org/status/404

            Return value is: Requested http://httpbin.org/status/404 and got 404\n""")
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


class ValidateUrlsTests(unittest.TestCase):

    def test_passed_in_empty_list(self):
        "Passed in empty list and got empty list right back"
        self.assertEqual(validate_urls([]), [])

    def test_passed_in_a_single_success_url(self):
        "Passed in a single successful url and since we don't care about those, doesn't give anything"
        self.assertEqual(validate_urls(["http://httpbin.org/status/200"]), [])

    def test_passed_in_a_single_properly_formatted_failing_url(self):
        "Passed in a single failing url, successfully"
        pass   # To-do: fix this test
        # self.assertEqual(validate_urls(["http://httpbin.org/status/410"]),
        #                ("http://httpbin.org/status/410", "410: Gone"))

    def test_passed_in_two_success_urls(self):
        "Passed in two successful urls and since we don't care about those, doesn't give anything"
        self.assertEqual(validate_urls(["http://httpbin.org/status/200", "http://httpbin.org/status/200"]), [])

    def test_passed_in_two_properly_formatted_failing_urls(self):
        "This should do what it says"
        pass   # To-do: write this test

# How will you know when to stop testing? Ask yo friends in QA

if __name__ == '__main__':
    unittest.main()