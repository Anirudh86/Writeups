
To connect, `ssh bandit4@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

Type ls to see files present in the current folder.

```
bandit4@bandit:~$ ls
inhere
```

Move into inhere directory using `cd inhere`.

List all files in the folder.

```
bandit4@bandit:~$ ls
-file00 -file02 -file04 -file06 -file08
-file01 -file03 -file05 -file07 -file09
```

We have also been told that we need to find a file with human readable data.

These levels are to meant to teach basics of linux commands.

So we can safely assume that human readable data would mean ASCII data.

There are a couple of solutions to find the file with ASCII data.

**Solution 1**

The file data checks the magic numbers of the file to determine what kind of file it is.

We can use it to find the file with only ASCII data.

```
bandit4@bandit:~$ file ./-file*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII data
./-file08: data
./-file09: data
```

There is only one file with ASCII data. We can print the contents of -file07 to get the password.

```
bandit4@bandit:~$ cat ./-file07
<bandit5_password>
```

**Solution 2**

We can print the contents of all files and filter for only printable characters.

This can be achieved using strings command.

```
bandit4@bandit:~$ cat ./-file* | strings
<bandit5_password>
```

**Solution 3**

As we know that ASCII data we need will consist of lowercase and uppercase. So we can use regex to search for it.

For searching text grep is very useful. It can be used to search for a lot of things.

But we will focus on using grep to search using regex.

To search using regex with grep, we will use -E switch.

The -H switch is used to print the filename where the match is found.

```
bandit4@bandit:~$ grep -EH "[a-zA-Z]" ./*
<bandit5_password>
```


All the solutions will print the contents of the file with ASCII data to screen and we will get the password to the next level.
