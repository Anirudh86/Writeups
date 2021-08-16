This being the first level, we are given the username and password to connect to the instance via ssh.

To connect, `ssh leviathan0@leviathan.labs.overthewire.org -p 2223`.

On being prompted for password, enter **leviathan0**.

After a successful connection, we are presented with a shell.


We are informed that the `Data for the levels can be found in the homedirectories`.

So lets list the files present in the home directory.

```
leviathan0@leviathan:~$ ls -a
total 24
drwxr-xr-x  3 root       root       4096 Aug 26  2019 .
drwxr-xr-x 10 root       root       4096 Aug 26  2019 ..
drwxr-x---  2 leviathan1 leviathan0 4096 Aug 26  2019 .backup
-rw-r--r--  1 root       root        220 May 15  2017 .bash_logout
-rw-r--r--  1 root       root       3526 May 15  2017 .bashrc
-rw-r--r--  1 root       root        675 May 15  2017 .profile
```

The **.backup** folder looks interesting. Lets see what it contains.

```
leviathan0@leviathan:~$ cd .backup
leviathan0@leviathan:~/.backup$ ls
bookmarks.html
```

Lets try searching for **leviathan1** in bookmarks.html.

```
leviathan0@leviathan:~/.backup$ grep leviathan1 bookmarks.html
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is <leviathan1_password>" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```

With this we get the password for the next level.