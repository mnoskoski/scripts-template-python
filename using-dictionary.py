#/usr/bin/env python

## forma de ler o dictionary
usernames = {
    "user1": "marcelo",
    "user2": "noskoski",
    "user2": "noskoski2",
    "user2": "noskoski2"
}
print(usernames.items())

## forma de ler o dictionary
for user in usernames:
    print(f"usuario: {user} nome: {usernames[user]}")

del usernames["user1"]
usernames.get()
print(usernames)