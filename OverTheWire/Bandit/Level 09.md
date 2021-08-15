
To connect, `ssh bandit9@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

List the files in the current directory using ls.

```
bandit9@bandit:~$ ls
data.txt
```

We have been told the following things about the password:
  - it is one of the few human readable strings (ASCII data).
  - it is preceded by several "**=**" characters.

To find readable strings in a file, we can use the **string** command.

After finding only the human readable strings, we need to filter out to find the password. We can use the grep command to search for strings containing atleast two "**=**".

```
bandit9@bandit:~$ strings data.txt | grep "=="
========== the*2i"4
========== password
Z)========== is
&========== <bandit10_password>
```

With this we will get the password to the next level.