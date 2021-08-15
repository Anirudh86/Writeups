To connect, `ssh bandit13@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

List the files in the current directory using ls.

```
bandit13@bandit:~$ ls
sshkey.private
```

The sshkey.private is the private key from the public-private key pair.
Instead of using passwords, we can generate and use private keys to connect using ssh.

Lets connect to bandit14 over localhost using this ssh private key.

The -i switch tells ssh to use the private key, passed as argument, for authentication.

Once we connect successfully, we get shell as user bandit14.

Now we can get the password to bandit14 by printing the password from /etc/bandit_pass/bandit14.

```
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost
...
...
...
bandit14@bandit:~$ whoami
bandit14
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
<bandit15_password>
```

You might have to type **exit** twice to close the connection completely.

The first **exit** will close the connection to bandit14 user and the second will close the connection to bandit13 user.

With this we will get the password to the next level.