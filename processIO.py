import asyncio
# import threading
import multiprocessing
# import time
# import termios
# import fcntl
# import tempfile
# pretend to be a terminal.
import time
import subprocess
import os
# write some env to it. both os and popen.
os.environ['TERM'] = 'xterm'
def run(cmd):
    # await asyncio.sleep(1)
    # just render it into something else.
    # stdin=tempfile.TemporaryFile("w+b")
    proc = subprocess.Popen(
        cmd,stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    # proc.stdin.write(b"junk\n")
    def readline(a,b):
        while True:
            buff=a.readline()
            print(b+buff)
    multiprocessing.Process(target=readline,args=(proc.stdout,b"stdout: ")).start()
    multiprocessing.Process(target=readline,args=(proc.stderr,b"stderr: ")).start()
    # start another shit.
    # read what?
    # when it is dead, it goes crazy. so share the namespace please?
    # not gonna start.
    ik=5
    x=["links","elinks","vim","ps","sed"]
    while ik>0:
        proc.stdin.write(x[ik-1].encode()+b"\n")
        proc.stdin.flush()
        ik-=1
        time.sleep(1)
    proc.kill()
    # does not affect?
    # how comes.
    # set the overall value into something else?
    print("_EOL_")
    # or multiprocessing works the same?
    # stdout, stderr = await proc.communicate()
    # print(f'[{cmd!r} exited with {proc.returncode}]')
    # if stdout:
    #     print(f'[stdout]\n{stdout.decode()}')
    # if stderr:
    #     print(f'[stderr]\n{stderr.decode()}')
# somewhat works.
if __name__ == "__main__":
    multiprocessing.freeze_support()
    run('bash')
    print("AHEAD OF TIME")