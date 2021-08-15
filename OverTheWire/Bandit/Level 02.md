To connect, `ssh bandit2@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

Type ls to see files present in the current folder.

```
bandit2@bandit:~$ ls
spaces in this filename
```

If we try `cat spaces in this filename`, it won't work because the spaces makes cat think there are 4 files to print from. But it's just one file with the name **spaces in this filename**.

There are two possible solutions to print the contents of the file **spaces in this filename** to screen.

**Solution 1**

We can escape each space character by adding \ character before it.

```
bandit2@bandit:~$ cat spaces\ in\ this\ filename
```

**Solution 2**

We can surround the filename with quotes.

```
bandit2@bandit:~$ cat "spaces in this filename"
```

Both solutions will print the contents of the **-** file to screen and we will get the password to the next level.
