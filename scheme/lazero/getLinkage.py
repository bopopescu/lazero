# TODO: implement raw things and arbitrary tests.
import re
def around(a, b):
  build = r'[^{}]+{}[^{}]+'.format(
      *[re.escape(b) for x in range(3)])
  return re.findall(build,a)
