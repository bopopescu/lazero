import re
from endmark import windowConv

# TODO: fuzzy search
# TODO: interpret user's mood and intention

def ranker(a, b):
    return len(re.findall(r'{}'.format(re.escape(b))), a)


def listRanker(a, b):
    return [(x, ranker(a, x)) for x in b]


def possibleRanker(a, b, window_size):
    b0 = windowConv(b, window_size)
    b1 = listRanker(a, b0)
    return b1


def possibleWindowSize(b, sigma):
    assert sigma<1 and sigma >0
    b0 = len(b)
    b1 = round(b0 * sigma)
    b2 = list(range(b1, b0 + 1))
    return b2


def ranky(a, b, sigma):
    return [possibleRanker(a,b,x) for x in possibleWindowSize(b,sigma)]