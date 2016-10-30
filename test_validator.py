# tests for validator.py project

import unittest

# Make a Test class; name it the name of the thing you're testing
# We want to test the entire CLI
# an acceptance or functional test that goes end to end
# Doesn't test one individual function; but rather main()


class ValidatorProgramTests(unittest.TestCase):
    # write a test for the empty case
    def test_user_pressed_return_instead_of_entering_URLs(self):
        "Test for when user presses return or enter instead of entering a URL"
        self.fail("TODO: Finish writing your test")


if __name__ == '__main__':
    unittest.main()