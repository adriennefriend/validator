"""current working copy
write a function that returns URLS that are bad
need to return a list containing info about the URLs and
the status of each URL

MUST HAVES:
1) Track changes locally with git
2) Push code to a public GitHub repo
3) Include a README with a) instructions for running your code and tests
4) Functionally, program MUST:
- accept a list of URLs and return a subset of those links that are either
written incorrectly or do not return a success status code, along with a
way to identify what was wrong with each link.
"""

import requests


def print_header():
    # a function that shows a header
    print("---------------------------------")
    print("   C'mon let's check some urls   ")
    print("---------------------------------")
    print()


def get_urls():
    # returns the list of URLs
    print("Hey, type some comma-separated urls!")
    url = input("... ")
    urls_entered = url.split(",")
    print(urls_entered)   # debugging aid for my sake :)
    return urls_entered


def get_status_code(url):
    try:
        response = requests.get(url)
        return "Requested {} and got {}".format(url, response.status_code)
    except Exception as blarg:    # add blarg to PyCharm dictionary
        print("Exception! The error is:", blarg)


def display_results(collected_urls):
    # Prints a summary at the bottom
    # Not strictly necessary, can be commented out
    print()
    print("------------------------------------------------------------")
    print()
    print("Summary")
    print()
    print("What we tried:", collected_urls)
    print()
    print("Hope this was helpful!")
    print()


def main():
    print_header()
    urls = get_urls()
    collected_results = []
    for url in urls:
        print()
        print("Handling", url)
        code = get_status_code(url)
        collected_results.append(code)
        print()
        print("Return value is:", code)
        # print("return value of get_status_code is:", code)
    display_results(collected_results)    # not strictly necessary, can be commented out
    return collected_results              # not strictly necessary, can be commented out


if __name__ == '__main__':
    main()