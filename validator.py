# MUST HAVES:
# 1) Track changes locally with git
# 2) Push code to a public GitHub repo
# 3) Include a README with a) instructions for running your code and tests
# 4) Functionally, program MUST:
# - accept a list of URLs and return a subset of those links that are either
# written incorrectly or do not return a success status code, along with a
# way to identify what was wrong with each link

import requests


def print_header():
    # a function that shows a header
    print("C'mon let's check some urls")
    print()


def get_urls():
    # returns the list of URLs
    url = input("Hey, type some comma-separated urls! > ")
    urls_entered = url.split(",")
    return urls_entered


def validate_urls(urls):
    """ Return information about each URL that cannot be fetched.
    Return format is list of tuples [("http://some/invalid/url", status_code, message)]
    where first element is the URL that caused the error,
    status_code is either 1) a non-200 HTTP status code, or 2) None
    and message is a string describing the problem """
    urls_returned = []
    for url in urls:
        try:
            code = get_status_code(url)
            if code != 200:
                urls_returned.append((url, code, "Is a non-200 result code"))
        except Exception as blarg:
                urls_returned.append((url, None, str(blarg)))
    return urls_returned


def get_status_code(url):
    """Return to an earlier version of this function that focuses on
    making a request to a given URL and simply returning the HTTP response code"""
    response = requests.get(url)
    print(response.status_code)   # for debugging purposes
    return response.status_code


def main():
    print_header()
    urls = get_urls()
    error_info = validate_urls(urls)
    print(error_info)


if __name__ == '__main__':
    main()