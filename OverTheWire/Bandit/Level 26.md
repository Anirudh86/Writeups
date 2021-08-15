To connect, `ssh -i <private_key_file_name> bandit26@bandit.labs.overthewire.org -p 2220`.

Ensure the permissions of the private key are set 400 or read-only for your current user.

Otherwise ssh does not utilize the private key and you are prompted for a password.

For changing permissions of the private key, use `chmod 400 <private_key_file_name>`.

After updating permissions, connect again.

After a successful connection, we are presented with a shell.

It prints some text and then the connection is closed.


Lets connect to bandit25 using ssh and to figure out what shell is used for bandit26 user.

To connect, `ssh bandit25@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with bandit25 user's shell.


The default shell to be spawned for a user on ssh connection is defined in /etc/passwd.

```
bandit25@bandit:~$ cat /etc/passwd | grep bandit26
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
```


Lets see what showtext is so that we can figure out how to use it to get the password for bandit27.

```
bandit25@bandit:~$ ls -al /usr/bin/showtext
-rwxr-xr-x 1 root root 53 May  7  2020 /usr/bin/showtext
bandit25@bandit:~$ file /usr/bin/showtext
/usr/bin/showtext: POSIX shell script, ASCII text executable
bandit25@bandit:~$ cat /usr/bin/showtext
#!/bin/sh

export TERM=linux

more ~/text.txt
exit 0
bandit25@bandit:~$
```

Close the connection to bandit25 and lets see how to persist our connection to bandit26 user.

So showtext is a shell script, which prints the text in **~/text.txt** using more and then exits.


The more command is a filter, which is useful to page through text which overflows in a screen.


Due to our default terminal height being more than the height of the text, more prints the text onto the screen and then the connection is terminated.

If we were to reduce the terminal height such that the text printed on the screen overflows, more will help us page through it, and the connection will persist.


To do so reduce the terminal height to half or less than half the default height.

After reducing the height, try connecting to bandit26 user. If the connection still terminates, try reducing the height a little more till you see something similar to `--More--(66%)` or `--More--(50%)`.


Once you see that, press **v** to enter editing mode.


Now you may resize the terminal height to a more comfortable, readable height.


After that enter `:set shell=/bin/bash`. This will set shell to bash.

Then enter `:shell` and it will spawn a bash shell for us.


Once we have a bash shell, we can list the files in the current directory.

```
bandit26@bandit:~$ ls
bandit27-do  text.txt
```

The executable bandit27-do is a setuid binary.


The setuid bit is used to indicate that when running an executable, it will set its permissions to that of the user who created it (owner), instead of setting it to the user who launched it.

Simply put, when we run the **bandit27-do** binary, we will have bandit27 user's permissions.


To get the password for bandit27, we will print the password from **/etc/bandit_pass/bandit27** using the setuid binary, **bandit27-do**.

```
bandit26@bandit:~$ ./bandit27-do 
Run a command as another user.
  Example: ./bandit27-do id
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
<bandit27_password>
```

Typing exit to close the bash shell will take you back to the more command and text.


To exit the more command and text, enter `:q!`.

You should see something similar `--More--(50%)`.

Press q and the connection should terminate.

With this we get the password to the next level.