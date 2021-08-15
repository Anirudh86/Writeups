To connect, `ssh bandit15@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

For this level, we need to send the password of the current level to a service running on port 30001.

And in response, the service will send the password for the next level.

But this time, we use send the password over ssl.

Setting up a SSL session over nc is a tedious task.
Fortunately, we have a tool which will handle this for us - openssl.

Openssl has a command, **s_client** which we will use to help us set up a SSL session.

The -connect switch tells s_client to make a connection to the specified host and port.

Once a session has been established, we will paste the current level's password and in response we will get the next level's password.

```
bandit15@bandit:~$ openssl s_client -connect localhost:30001
CONNECTED(00000003)
....
....
....
---
<bandit15_password>
Correct!
<bandit16_password>

closed
bandit15@bandit:~$
```

With this we will get the password to the next level.