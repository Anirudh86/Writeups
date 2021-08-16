This being the first level, we are given the username and password to connect to the instance via ssh.

To connect, `ssh leviathan4@leviathan.labs.overthewire.org -p 2223`.

On being prompted for password, enter **leviathan4**.

After a successful connection, we are presented with a shell.


We are informed that the `Data for the levels can be found in the homedirectories`.

So lets list the files present in the home directory.

```
leviathan4@leviathan:~$ ls -al
total 24
drwxr-xr-x  3 root root       4096 Aug 26  2019 .
drwxr-xr-x 10 root root       4096 Aug 26  2019 ..
-rw-r--r--  1 root root        220 May 15  2017 .bash_logout
-rw-r--r--  1 root root       3526 May 15  2017 .bashrc
-rw-r--r--  1 root root        675 May 15  2017 .profile
dr-xr-x---  2 root leviathan4 4096 Aug 26  2019 .trash
```

The **.trash** folder looks interesting. Lets see what it contains.


```
leviathan4@leviathan:~$ cd .trash
leviathan4@leviathan:~/.trash$ ls -al
total 16
dr-xr-x--- 2 root       leviathan4 4096 Aug 26  2019 .
drwxr-xr-x 3 root       root       4096 Aug 26  2019 ..
-r-sr-x--- 1 leviathan5 leviathan4 7352 Aug 26  2019 bin

```

The **bin** file has the setuid bit set and it is executable.


The setuid bit allows the executable to gain the permissions of the owner instead of the user executing it.


In this case, on running the bin executable, it will gain permissions of **leviathan5**.


Lets run `bin` and see what happens.

```
leviathan4@leviathan:~$ ./bin
01010100 01101001 01110100 01101000 00110100 01100011 01101111 01101011 01100101 01101001 00001010
```

This is binary output.

Lets convert it to ASCII.

I use a handy tool [CyberChef](https://gchq.github.io/CyberChef/) to do the conversion.

On converting to ASCII, we get the password for the next level.