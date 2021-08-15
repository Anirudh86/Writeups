To connect, `ssh bandit25@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

Lets list the files in the current directory.

```
bandit25@bandit:~$ ls
bandit26.sshkey
```


Lets print the contents of this private key so that we use it connect to the next level.

```
bandit25@bandit:~$ cat bandit26.sshkey
-----BEGIN RSA PRIVATE KEY-----
....
....
....
-----END RSA PRIVATE KEY-----
bandit25@bandit:~$
```

Instead of a password, we are presented with a private key. Copy and paste this private key in a file to use it to connect to the next level.