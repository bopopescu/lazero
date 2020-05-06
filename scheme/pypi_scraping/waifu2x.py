from dbM import showX, up
import pypi_get as pg
from multiprocessing import Pool, freeze_support
from endmark import windowEndMarkEx as wex

# TODO: switch between different mirrors so no one will block us.
def parallel(x, v, z):
    with Pool(processes=x) as pool:
        return pool.map(v, z)


def workload(meta):
    x, y = meta
    try:
        p = pg.get(y)
        print("fetching success")
        up(x, p)
    except:
        print("fetching error")
    return


if __name__ == "__main__":
    s = showX("projects", 0)
    l = wex(s, 10)
    freeze_support()
    for meta in l:
        parallel(len(meta), workload, meta)
# for x,y in s:
#     try:
#         p = pg.get(y)
#         print("fetching success")
#         up(x, p)
#     except:
#         print("fetching error")
