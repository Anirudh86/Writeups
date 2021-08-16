This being the first level, we are given the username and password to connect to the instance via ssh.

To connect, `ssh leviathan1@leviathan.labs.overthewire.org -p 2223`.

On being prompted for password, enter **leviathan1**.

After a successful connection, we are presented with a shell.


We are informed that the `Data for the levels can be found in the homedirectories`.

So lets list the files present in the home directory.

```
leviathan1@leviathan:~$ ls -al
total 28
drwxr-xr-x  2 root       root       4096 Aug 26  2019 .
drwxr-xr-x 10 root       root       4096 Aug 26  2019 ..
-rw-r--r--  1 root       root        220 May 15  2017 .bash_logout
-rw-r--r--  1 root       root       3526 May 15  2017 .bashrc
-r-sr-x---  1 leviathan2 leviathan1 7452 Aug 26  2019 check
-rw-r--r--  1 root       root        675 May 15  2017 .profile
```

The **check** file has the setuid bit set and it is executable.


The setuid bit allows the executable to gain the permissions of the owner instead of the user executing it.


In this case, on running the check executable, it will gain permissions of leviathan2.


Lets run `check` and see what happens.

We enter 1234 as a password to see what happens.

```
leviathan1@leviathan:~$ ./check
password: 1234
Wrong password, Good Bye ...
```


So check is comparing the password to a string which must be hardcoded in it.

We can use `ltrace` to see what library calls the check executable uses.

```
leviathan1@leviathan:~$ ltrace ./check
__libc_start_main(0x804853b, 1, 0xffffd794, 0x8048610 <unfinished ...>
printf("password: ")                                                     = 10
getchar(1, 0, 0x65766f6c, 0x646f6700password: 1234
)                                    = 49
getchar(1, 0, 0x65766f6c, 0x646f6700)                                    = 50
getchar(1, 0, 0x65766f6c, 0x646f6700)                                    = 51
strcmp("123", "sex")                                                     = -1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)                                     = 29
+++ exited (status 0) +++
```

The line `strcmp("123", "sex")` is where the comparison of the password takes place.

Now that we know what the password is, lets try it and see what happens.

```
leviathan1@leviathan:~$ ./check
password: sex
$ whoami
leviathan2
```

It worked and on running `whoami`, we see that we are leviathan2 user.

We can print the password for leviathan2 from `/etc/leviathan_pass/leviathan2`.

```
$ cat /etc/leviathan_pass/leviathan2
<leviathan2_pass>
```

With this we get the password for the next level.