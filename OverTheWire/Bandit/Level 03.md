To connect, `ssh bandit3@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

Type ls to see files present in the current folder.

```
bandit3@bandit:~$ ls
```

With `ls`, hidden files/folders are not shown.

In linux, a file/folder is hidden by adding **.** before the name. For example, to hide a file named **file1**, we will rename it to **.file1** and it will be hidden.

To show hidden files, ls has a switch, which is **-a**.

```
bandit3@bandit:~$ ls -a
.hidden
```

Print the contents of the file **.hidden** to screen using cat.

```
bandit3@bandit:~$ cat .hidden
```

With this, we will get the password to the next level.