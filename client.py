# -*- coding: utf-8 -*-
"""
Created on Sun May 24 08:31:08 2020

@author: Nicolas Xiong
"""
import socket
import time

def b2s(b):
    return str(b,'UTF-8')

def s2b(s):
    return bytes(s,'UTF-8')

if __name__=="__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('47.100.91.71', 8001))
    flag = '1'
    while True:
        time.sleep(3)
        print ('send to server with value: '+ flag)
        sock.send(s2b(flag))
        print (b2s(sock.recv(1024)))  #限制每次发送数据的大小
        flag = input("input:")
    sock.close()