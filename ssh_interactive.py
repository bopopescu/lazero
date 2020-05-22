import paramiko
import time
private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')#使用目标的私钥来登录
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#ssh.connect(hostname='127.0.0.1',port=22,username='root',pkey=private_key)

#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接服务器
ssh.connect(hostname='127.0.0.1', port=22, username='test', password='test')
# it is my system password after all.

#cmd = 'yes'
#stdin, stdout, stderr = ssh.exec_command(cmd)
remote_conn = ssh.invoke_shell()
# nothing is like this.
#remote_conn.send("python\n")
# what about errors?
time.sleep(2)
# you even have that shell thing!
#remote_conn.send("yes\n")
# yes! it does matters.
# by the way, I fucking hate shell command typing. It is awful.
# what about networking and GUI clicking?
# same to me! ok?
output=remote_conn.recv(1000)
#remote_conn.send("happybirthday\n")
remote_conn.send("msfconsole\n")
# time.sleep(20)
# what is going on?
# just to check.
# it is working, after all.
# may miss a bit?
# you should get that thing!
# no error! strange thing!
# there should be error.
# no respond! how about python?
# why you have to wait
# sleep for a while?
timeall=100
while timeall>=0:
    output = remote_conn.recv(1000)
# i want to see some web repl.
#result = stdout.read()
#while not stdout.channel.exit_status_ready():
#    # Only print data if there is data to read in the channel
#    if stdout.channel.recv_ready():
#        rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
#        if len(rl) > 0:
            # Print data from stdout
#            print(stdout.channel.recv(1024),)
            # this is not good.
#if not result:
# search for possible errors!
# errors are sweet?
# it is all connected.
# does the order matters?
    print(output.decode())
    # code is intepretable for shell but no unicode support?
#    print(output)
    # what is the color?
    # check it?
    time.sleep(0.1)
    timeall-=1
# do we really know it is repl?
# never mind. we can do manual debugging from now on.
#    result = stderr.read()
ssh.close()

#print(result.decode())
