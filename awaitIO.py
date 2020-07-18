import asyncio
import time
import termios
import fcntl
import tempfile

async def run(cmd):
    # await asyncio.sleep(1)
    stdin=tempfile.TemporaryFile("w+b")
    proc = await asyncio.create_subprocess_shell(
        cmd,stdin=stdin.fileno(),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    # proc.stdin.write(b"junk\n")
    c=b"junk\n"
    # must be a file.
    # fucking shit?
    for char in c:
        fcntl.ioctl(stdin, termios.TIOCSTI, char)
    # proc.stdin.
    # await proc.stdin.drain()
    # print(type(proc.stdin),dir(proc.stdin))
    # proc.stdin.write_eof()
    # # fucking shit.
    # not really useful.
    # proc.stdin.drain()
    # EOF can kill any shell. but return won't.
    # proc.stdin.close()
    # print(dir(proc.stdin))
    stderr = await proc.stderr.read()
    # correctly handled?
    print(stderr)
    # same here.
    proc.stdin.write(b"\njunkfile\n")
    # proc.stdin.
    proc.stdin.write_eof()
    # nothing here. shit man.
    # we can try a crack here.
    # the ultimate crack.
    # not really useful.
    # proc.stdin.drain()
    # proc.stdin.close()
    # print(dir(proc.stdin))
    stderr = await proc.stderr.read()
    print(stderr)
    # stdout, stderr = await proc.communicate()
    # print(f'[{cmd!r} exited with {proc.returncode}]')
    # if stdout:
    #     print(f'[stdout]\n{stdout.decode()}')
    # if stderr:
    #     print(f'[stderr]\n{stderr.decode()}')

asyncio.run(run('bash'))
print("AHEAD OF TIME")