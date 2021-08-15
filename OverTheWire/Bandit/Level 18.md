To connect, `ssh bandit18s@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

And immediately the connection is closed with the word **ByeBye!** displayed.

We are told that the **.bashrc** has been edited. And that the password for the next level is in a readme file in the home directory.

The **.bashrc** file is used to customize how the bash terminal looks and behaves.

When ssh establishes a connection, the bash shell is spawned.

So before the bash shell is spawned, we can execute a command using a psuedo terminal on establishing a connection. After executing the command, the bash shell will be spawned and the connection will closed.

To execute a command using a psuedo terminal, -t switch is used.

```
root@kali:~$ ssh bandit18s@bandit.labs.overthewire.org -p 2220 -t "ls"
....
....
....
readme
ByeBye!
....
root@kali:~$ ssh bandit18s@bandit.labs.overthewire.org -p 2220 -t "cat readme"
....
....
...
<bandit19_password>
ByeBye!
....
root@kali:~$
```

With this we will get the password for the next level.