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
    pass
    urls_returned = []
    # To-do: magic happens, lord help
    return urls_returned


def get_status_code(url):
    try:
        response = requests.get(url)
        return "Requested {} and got {}".format(url, response.status_code)
    except Exception as blarg:    # add blarg to PyCharm dictionary
        print("Exception! The error is:", blarg)


def main():
    print_header()
    urls = get_urls()
    for url in urls:
        print()
        print("Handling", url)
        code = get_status_code(url)
        print()
        print("Return value is:", code)


if __name__ == '__main__':
    main()