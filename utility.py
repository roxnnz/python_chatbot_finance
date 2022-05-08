import re


def isRegexPass(targetDOB):
    dd_mm_yyyy_search = re.compile(
        "^(3[01]|[12][0-9]|0?[1-9])/(1[0-2]|0?[1-9])/(?:[0-9]{2})?[0-9]{2}$")

    return dd_mm_yyyy_search.match(targetDOB)
