# github.com/03B

import httpx
from threading import Thread, active_count

from itertools import product
from string import ascii_lowercase
keywords = [''.join(i) for i in product(ascii_lowercase+"0987654321", repeat = 4)]



threads = 50

def check(username):
   try:
    if "88" not in username:
        return
    resp = httpx.get(f"https://auth.roblox.com/v1/usernames/validate?birthday=2000-01-01T00:00:00.000Z&context=Signup&username={username}")
    if " valid" in resp.text:
        print(username, "is valid.")
        open("out.txt", "a").write(f"\n{username}")
    else:
        print(username)
   except:
       check(username)



usernames = iter(keywords)

while True:
    if active_count() < threads:
        Thread(target=check, args=(next(usernames), )).start()