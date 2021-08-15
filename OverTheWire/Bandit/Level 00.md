This being the first level, we are given the username and password to connect to the instance via ssh.

To connect, `ssh bandit0@bandit.labs.overthewire.org -p 2220`.

On being prompted for password, enter **bandit0**.

After a successful connection, we are presented with a shell.

Type ls to see files present in the current folder.

```
bandit0@bandit:~$ ls
readme
```

Print the contents of the readme file on the screen using cat.
```
bandit0@bandit:~$ cat readme
```

With this we get the password for the next level.