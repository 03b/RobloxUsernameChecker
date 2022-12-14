# github.com/03B

import httpx
from threading import Thread, active_count

threads = 50

def check(username):
   try:
    resp = httpx.get(f"https://auth.roblox.com/v1/usernames/validate?birthday=2000-01-01T00:00:00.000Z&context=Signup&username={username}")
    if " valid" in resp.text:
        print(username, "is valid.")
        open("out.txt", "a").write(f"\n{username}")
    else:
        print(username)
   except:
       check(username)



usernames = iter(open("usernames.txt").read().splitlines())

while True:
    if active_count() < threads:
        Thread(target=check, args=(next(usernames), )).start()
