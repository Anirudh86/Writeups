To connect, `ssh bandit20@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

We list the files in the current directory.

```
bandit20@bandit:~$ ls
suconnect
bandit20@bandit:~$ ls -al suconnect
-rwsr-x--- 1 bandit21 bandit20 12088 May  7  2020 suconnect
```

We find an executable by the name of suconnect. And we are told it has the setuid bit set.

We can see the setuid bit in the permissions. For the user permissions, instead of **rwx**, we can see **rws**. The **s** bit is the setuid bit.

The setuid bit is used to indicate that when running an executable, it will set its permissions to that of the user who created it (owner), instead of setting it to the user who launched it.

Simply put, when we run the **suconnect** binary, we will have bandit21 user's permissions.

We are also told that to run the suconnect binary, we need to pass a port number as argument.

And on running the suconnect binary, it will try connecting the specified port and it will read a line from the connection.

If the line it reads from the connection matches the current level's password, it will print the next level's password.


We will need to set up a service listening on a port, which when connected to will send back the password to the current level.

To do so we will nc. And to ensure nc runs in the background, we will use **&** operator.

The -l switch tells nc to start the listening mode. And the -p switch tells nc to use the port specified to listen.

```
bandit20@bandit:~$ echo <bandit20_password> | nc -lp <port_number> &
[1] <process_number>
bandit20@bandit:~$
```

Now that we a service running on a port, lets run the suconnect binary and pass the port number we gave nc.

```
bandit20@bandit:~$ ./suconnect <port_number>
Read: <bandit20_password>
Password matches, sending next password
<bandit21_password>
bandit20@bandit:~$
```

With this we will get the password for the next level.