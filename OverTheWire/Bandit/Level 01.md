To connect, `ssh bandit1@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

Type ls to see files present in the current folder.

```
bandit1@bandit:~$ ls
-
```

If we try `cat -`, it won't work because passing only **-** makes **cat** believe we are passing a flag/switch to it.

There are two possible solutions to print the contents of the file **-** to screen.

**Solution 1**

We can pass the file name a relative path from the current directory.

```
bandit1@bandit:~$ cat ./-
-
```

**Solution 2**

We can print the contents of all files in current directory. This will work for now as there is only one not hidden file in the current directory.

```
bandit1@bandit:~$ cat ./*
-
```

Both solutions will print the contents of the **-** file to screen and we will get the password to the next level.
