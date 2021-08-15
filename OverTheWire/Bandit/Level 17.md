To connect, `ssh -i <private_key_file_name> bandit17@bandit.labs.overthewire.org -p 2220`.

Ensure the permissions of the private key are set 400 or read-only for your current user.

Otherwise ssh does not utilize the private key and you are prompted for a password.

For changing permissions of the private key, use `chmod 400 <private_key_file_name>`.

After updating permissions, connect again.

After a successful connection, we are presented with a shell.

List the files in the current directory.

```
bandit17@bandit:~$ ls
passwords.new  passwords.old
bandit17@bandit:~$
```

There are two files - passwords.new and passwords.old.

We are told that the only line that changed from passwords.old to passwords.new is the password.

So if we are able to compare the files line by line, we will find the only line which differs in both files.

To compare two or more files, there is handy tool called diff.

```
bandit17@bandit:~$ diff passwords.old passwords.new 
42c42
< w0Yfolrc5bwjS4qw5mq1nnQi6mF03bii
---
> <bandit18_password>
bandit17@bandit:~$ 

```
From passwords.old, the line which differs starts with **<**.

And from passwords.new, the line which differs starts with **>**.

With this we will get the password for the next level.