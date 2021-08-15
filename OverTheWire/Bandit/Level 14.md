To connect, `ssh bandit14@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

For this level, we need to send the password of the current level to a service running on port 30000.

And in response, the service will send the password for the next level.

A handy tool to connect to services, either locally or remotely, is nc also known as netcat.

It can setup TCP connections, send UDP packets, listen on ports and much more. I recommend reading the  man page for nc.

To send data to the service on port 30000, we will pipe the data from echo to nc.

```
bandit14@bandit:~$ echo <bandit14_password> | nc localhost 30000
Correct!
<bandit15_password>

bandit14@bandit:~$
```

With this we will get the password to the next level.
