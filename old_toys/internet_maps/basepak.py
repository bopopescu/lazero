import requests
import traceback


def getPic(a, b, c):
    try:
        assert type(a) == int and a >= 0 and a <= 10
        assert type(b) == int and b >= 0 and b <= 1024
        assert type(c) == int and c >= 0 and c <= 1024
        # d=(a,b,c)
        # d=list(map(str,d))
        r = "https://d2h9tsxwphc7ip.cloudfront.net/{}/{}%20{}.png".format(
            a, b, c)
        r = requests.get(r)
        r = r.content
        return r
    except:
        e = traceback.format_exc()
        print(e)
        return None


def getRange(a):
    a = 2**a
    return [(x, y) for x in range(a) for y in range(a)]
    # it should be preconfigured.
