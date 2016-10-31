# tests for validator.py project

import unittest

from validator import validate_urls


class ValidateUrlsTests(unittest.TestCase):

    def test_passed_in_empty_list(self):
        """Passed in empty list and got empty list right back"""
        self.assertEqual(validate_urls([]), [])

    def test_passed_in_a_single_success_url(self):
        """Passed in a single successful url and since we don't care about those, doesn't give anything"""
        self.assertEqual(validate_urls(["http://httpbin.org/status/200"]), [])

    def test_passed_in_a_single_properly_formatted_failing_url(self):
        """Passed in a single failing url, successfully"""
        self.assertEqual(validate_urls(["http://httpbin.org/status/410"]),
                        [("http://httpbin.org/status/410", 410, "Is a non-200 result code")])

    def test_passed_in_two_success_urls(self):
        """Passed in two successful urls and since we don't care about those, doesn't give anything"""
        self.assertEqual(validate_urls(["http://httpbin.org/status/200", "http://httpbin.org/status/200"]), [])

    def test_passed_in_two_properly_formatted_failing_urls(self):
        self.assertEqual(validate_urls(["http://httpbin.org/status/404", "http://httpbin.org/status/500"]),
                         [("http://httpbin.org/status/404", 404, "Is a non-200 result code"),
                          ("http://httpbin.org/status/500", 500, "Is a non-200 result code")])

    def test_passed_in_a_single_invalid_url(self):
        """Invalid URLs have a special return format"""
        self.assertEqual(validate_urls(["http://???"]),
                        [("http://???", None, "Invalid URL 'http://???': No host supplied")])


# How will you know when to stop testing? Ask yo friends in QA, keep reading, and play, play, play.

if __name__ == '__main__':
    unittest.main()