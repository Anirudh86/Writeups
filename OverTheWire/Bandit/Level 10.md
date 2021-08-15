To connect, `ssh bandit10@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

List the files in the current directory using ls.

```
bandit10@bandit:~$ ls
data.txt
```

We are told that the password is base-64 encoded.

We have the base64 command which can be used to encode and decode strings.

In this case as we need to decode, we will use the -d switch.

```
bandit10@bandit:~$ base64 -d data.txt
The password is <bandit11_password>
```

With this we will get the password to the next level.