from random import randint as rint


def make_header() -> dict:
    headers = {}

    if bool(rint(0, 1)):
        headers.update({
            'Accept-Encoding': 'gzip, deflate, br'
        })

    if bool(rint(0, 1)):
        headers.update({
            'Accept-Language': 'en-US;q=0.5,en;q=0.3'
        })

    if bool(rint(0, 1)):
        headers.update({
            'Cache-Control': 'max-age=0'
        })

    if bool(rint(0, 1)):
        headers.update({
            'DNT': '1'
        })

    if bool(rint(0, 1)):
        headers.update({
            'Upgrade-Insecure-Requests': '1'
        })

    if bool(rint(0, 1)):
        headers.update({
            'Referer': 'https://google.com'
        })

    if bool(rint(0, 1)):
        headers.update({
            'Pragma': 'no-cache'
        })

    return headers
