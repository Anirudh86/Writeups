To connect, `ssh bandit19@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

We list the files in the current directory.

```
bandit19@bandit:~$ ls
bandit20-do
bandit19@bandit:~$ ls -al bandit20-do
-rwsr-x--- 1 bandit20 bandit19 7296 May  7  2020 bandit20-do
```

We find an executable by the name of bandit20-do. And we are told it has the setuid bit set.

We can see the setuid bit in the permissions. For the user permissions, instead of **rwx**, we can see **rws**. The **s** bit is the setuid bit.

The setuid bit is used to indicate that when running an executable, it will set its permissions to that of the user who created it (owner), instead of setting it to the user who launched it.

Simply put, when we run the **bandit20-do** binary, we will have bandit20 user's permissions.

We can try this with a simple **whoami** command.

```
bandit19@bandit:~$ ./bandit20-do
Run a command as another user.
  Example: ./bandit20-do id
bandit19@bandit:~$ ./bandit20-do whoami
bandit20
bandit19@bandit:~$ 
```

If the executable didn't have the setuid bit set, then whoami would have returned bandit19 because we are currently bandit19 user.

But because of the setuid bit set, on running whoami, we are shown that we are bandit20 user.


So lets print the password of bandit20 from **/etc/bandit_pass/bandit20**, as the only users who can access that file are - bandit20 and root.

```
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
<bandit20_password>
bandit19@bandit:~$
```

With this we will get the password for the next level.