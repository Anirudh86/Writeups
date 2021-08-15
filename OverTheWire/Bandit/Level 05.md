
To connect, `ssh bandit5@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

Type ls to see files present in the current folder.

```
bandit5@bandit:~$ ls
inhere
```

Move into inhere directory using `cd inhere`.

List all files in the folder.

```
bandit5@bandit:~$ ls
maybehere00 maybehere04 maybehere08 maybehere12 maybehere16
maybehere01 maybehere05 maybehere09 maybehere13 maybehere17
maybehere02 maybehere06 maybehere10 maybehere14 maybehere18
maybehere03 maybehere07 maybehere11 maybehere15 maybehere19
```

We have also been told that we need to find a file with the following conditions:
  - human readable data (ASCII data)
  - 1033 bytes in size
  - not executable


These levels are to meant to teach basics of linux commands.

So we can safely assume that human readable data would mean ASCII data.

To find the file with the given parameters, we will use the find command.

The find command has lots of useful switches. I recommend getting familiar with the find command because it is quite a versatile tool. 

The -size switch specifies the size of the file. The **c** after the size indicates it is in bytes. Other supported characters for sizes can be found in the man page for find.

The -executable switch checks if the file has executable permission. As we want the file which is not executable we will add a negation operator (!) before it.

```
bandit5@bandit:~$ find . -size 1033c \! -executable
./inhere/maybehere07/.file2
```

There is only one file which has size 1033 bytes and is not executable. We can print the contents of maybehere07/.file2 to get the password.

```
bandit5@bandit:~$ cat ./inhere/maybehere07/.file2
<bandit6_password>
```

Had there been more than one file which had size 1033 bytes and not executable, then we would filter out the file we want using the **file** command.

We can do that using the -exec switch of the find command.

With this we will get the password to the next level.