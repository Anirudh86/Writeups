To connect, `ssh bandit32@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

We are told that everything in this shell becomes uppercase.

```
WELCOME TO THE UPPERCASE SHELL
>> ls
sh: 1: LS: not found
>>
```

We can see that `ls` became `LS`. Unless we get a normal shell without using characters from a-z or A-Z, our commands won't work.


Luckily, we can spawn a normal shell without using characters from a-z or A-Z.


The `$0` variable is a special variable in shell. Its value is the path to the current shell.

As it doesn't contain any characters from a-z or A-Z, it will execute and it will spawn a normal shell.

```
>> $0
$ echo $0
sh
$ whoami
bandit33
$
```

We ran `whoami` to check which user we are in our newly spawned shell. And we are bandit33 user.

We can now print the password to bandit33 level from **/etc/bandit_pass/bandit33**.


```
$ cat /etc/bandit_pass/bandit33
<bandit33_password>
$exit
>>
```

To exit from uppercase shell, press Ctrl+C.


With this we will get the password for the next level