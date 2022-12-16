#  github.com/03B | made with hate
#  12-14-22 // Please credit me if you use this in a program/product of yours, thanks.

import time
start = time.time()
import socket
import ssl
import threading
import random
import itertools


timeout = False
usernames = open("usernames.txt").read().splitlines()

def check(username):
  try:
    while timeout == True:
        time.sleep(0.5)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = ssl.wrap_socket(s)
    ssl_sock.connect(('auth.roblox.com', 443))
    ssl_sock.send(
      b'GET /v1/usernames/validate?birthday=2000-01-01T00:00:00.000Z&context=Signup&username='
      + username.encode() +
      b' HTTP/1.1\r\nHost: auth.roblox.com\r\nConnection: close\r\n\r\n')
    data = ssl_sock.recv(1024)
    ssl_sock.close()
  #  print(data)
    if b'valid' in data:
      print(f"\033[32m{username} is available.\033[0m")
      open("out.txt", "a").write(f"\n{username}")
      return
    else:
      print(f"\033[31m{username} is not available.\033[0m")
  except Exception as e:
    check(username)
    timeoutstart()


def main():
  for username in usernames:
    time.sleep(0.01)
    threading.Thread(target=check, args=(username, )).start()


if __name__ == '__main__':
  main()
  while True:
    if threading.active_count() == 1:
      end = time.time()
      print(
        f" checked {str (len (usernames ) )} usernames in { str( end - start )[ :4 ]} seconds. "
      )
      
      main()
