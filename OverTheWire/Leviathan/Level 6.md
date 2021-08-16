This being the first level, we are given the username and password to connect to the instance via ssh.

To connect, `ssh leviathan6@leviathan.labs.overthewire.org -p 2223`.

On being prompted for password, enter **leviathan6**.

After a successful connection, we are presented with a shell.


We are informed that the `Data for the levels can be found in the homedirectories`.

So lets list the files present in the home directory.

```
leviathan6@leviathan:~$ ls -al
total 28
drwxr-xr-x  2 root       root       4096 Aug 26  2019 .
drwxr-xr-x 10 root       root       4096 Aug 26  2019 ..
-rw-r--r--  1 root       root        220 May 15  2017 .bash_logout
-rw-r--r--  1 root       root       3526 May 15  2017 .bashrc
-r-sr-x---  1 leviathan7 leviathan6 7452 Aug 26  2019 leviathan6
-rw-r--r--  1 root       root        675 May 15  2017 .profile
```

The **leviathan6** file has the setuid bit set and it is executable.


The setuid bit allows the executable to gain the permissions of the owner instead of the user executing it.


In this case, on running the leviathan6 executable, it will gain permissions of leviathan3.


Lets run `leviathan6` and see what happens.

```
leviathan6@leviathan:~$ ./leviathan6 
usage: ./leviathan6 <4 digit code>
```

Lets try `1234` as a 4 digit code to see what happens.

```
leviathan6@leviathan:~$ ./leviathan6 1234
Wrong
```

As expected, it didn't work.

We will run ltrace on leviathan6 to see find the password it is comparing the input to.

```
leviathan6@leviathan:~$ ltrace ./leviathan6 1234
__libc_start_main(0x804853b, 2, 0xffffd784, 0x80485e0 <unfinished ...>
atoi(0xffffd8b3, 0, 0xf7e40890, 0x804862b)                               = 1234
puts("Wrong"Wrong
)                                                            = 6
+++ exited (status 0) +++
```

Leviathan6 is using atoi to convert the input string to an integer.


Let us run a simple bruteforce against levithan6 for all numbers from 0000 to 9999.

We will print the 4 digit number tried and leviathan6's output so that we will know which 4 digit code works.

```
leviathan6@leviathan:~$ for i in {0000..9999}; do echo $i `./leviathan6 $i`; done
0000 Wrong
0001 Wrong
0002 Wrong
...
...
...
7120 Wrong
7121 Wrong
7122 Wrong
^C
leviathan6@leviathan:~$
```

The execution hangs after printing `7122 Wrong` and had to stopped using `Ctrl-C`.

So 7123 must be the 4 digit code we are looking for.

We will pass 7123 directly to `leviathan6` and see what happens.

```
leviathan6@leviathan:~$ ./leviathan6 7123
$ whoami
leviathan7
```

We get shell as user leviathan7.

We can the password from `/etc/leviathan_pass/leviathan7`.

```
$ cat /etc/leviathan_pass/leviathan7
<leviathan7_password>
```

With this we get the password for the next level.

And with this all levels of leviathan have been solved.