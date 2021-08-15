
To connect, `ssh bandit7@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

List the files in the current directory using ls.

```
bandit7@bandit:~$ ls
data.txt
```

We have been told that the password is next to the word **millionth**.

To search for strings in files, we can use the grep command.

```
bandit7@bandit:~$ grep "millionth" ./data.txt
millionth <bandit8_password>
```

With this we will get the password to the next level.