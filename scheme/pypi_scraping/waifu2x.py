from dbM import showX, up
import pypi_get as pg
from multiprocessing import Pool, freeze_support
from endmark import windowEndMarkEx as wex
# from sub2 import timeout

# TODO: switch between different mirrors so no one will block us.
# TODO: make it sound.

def parallel(x, v, z):
    with Pool(processes=x) as pool:
        return pool.map(v, z)


def workload(meta):
    x, y = meta
    try:
        # p = timeout(timeout=35)(pg.get(y))
        p = pg.get(y)
        print("fetching success")
        up(x, p)
        # TODO: find out the cause of the freeze.
        # TODO: automatically relaunch the entire program in .cmd file.
    except:
        print("fetching error")
    return


if __name__ == "__main__":
    s = showX("projects", 0)
    print("TOTAL PENDING WORK:", len(s))
    l = wex(s, 100)
    ast = 0
    freeze_support()
    for meta in l:
        ast += len(meta)
        if ast <= 1500:
            # with parallel(len(meta), workload, meta) as locale:
            print("LOOP BEGINS HERE")
            assert len(parallel(len(meta), workload, meta)) == len(meta)
        else:
            exit()
            break
    exit()
    # TODO: find the real usage of exit()
        #     locale
        # TODO: find best scraping rate
        # TODO: autokill after 1500 samples
        # TODO: timeout in fetching the json
# for x,y in s:
#     try:
#         p = pg.get(y)
#         print("fetching success")
#         up(x, p)
#     except:
#         print("fetching error")
