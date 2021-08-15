
To connect, `ssh bandit6@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

We have been told that we need to find a file with the following conditions:
  - owned by user bandit7
  - owned by group bandit6
  - 33 bytes in size


But this time this file is not present in the home directory. It could be present anywhere on the filesystem.

To find the file, we will use the find command.

The find command has lots of useful switches. I recommend getting familiar with the find command because it is quite a versatile tool. 

The -user switch tells **find** to look for files who has user as bandit7.

The -group switch tells **find** to look for files who has group as bandit6.

The -size switch tells **find** to look for files which has the specified size, which is 33 bytes in this case.

As we are going to search all folders and files starting from the root directory (/), we are going to come across lots of folders and files which we cannot access.

This will be due to not having enough permissions as the user bandit6.

However, these errors of permission denied are not useful to us. So we will redirect the errors to /dev/null so that they are not printed on the screen.

This is achieved by redirecting the stderr to /dev/null.

```
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
```

Print the contents of the file to screen using cat.

```
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
<bandit7_password>
```

With this we will get the password to the next level.