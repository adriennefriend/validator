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
        with patch('builtins.input', side_effect=['']):
            with redirect_stdout(StringIO()) as fake_output:
                main()
        self.assertEqual(fake_output.getvalue(), "Wait a sec! I think you forgot to enter something.")


if __name__ == '__main__':
    unittest.main()


# make the tests fail in an aspirational way :D
