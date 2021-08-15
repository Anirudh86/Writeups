To connect, `ssh bandit16@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

We need to find an open port between 31000 and 32000 which has a ssl service running on it.

To find open ports on machine, we will use nmap.

Nmap is a very versatile tool. Infact, there is a whole book written on nmap.

For our use case, we only need to find open ports between 31000 and 32000 and figure out which service is running on it.

The -p switch will tell nmap the port range we want to scan.
And -sV switch will tell nmap to try and identify the service running on the port if it is open.

```
bandit16@bandit:~$ nmap -sV localhost -p 31000-32000

Starting Nmap 7.40 ( https://nmap.org )
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00022s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE     VERSION
31046/tcp open  echo
31518/tcp open  ssl/echo
31691/tcp open  echo
31790/tcp open  ssl/unknown
31960/tcp open  echo
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port31790-TCP:V=7.40%T=SSL%I=7%D=8/14%Time=61175FC7%P=x86_64-pc-linux-g
....
....
....
SF:\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 88.13 seconds
bandit16@bandit:~$
```

Nmap tells us that there are 5 ports - 31046, 31518, 31691, 31790, 31960 - which it found open.

Out of these, only 31691 and 31790 have a ssl service running.

Nmap also shows us the response it got when trying to identify the ssl service on port 31790. The response has words like wrong and password.

Lets try connecting to 31790 first.

We will use openssl and its s_client command to establish a ssl connection to 31790 port.

On successfully establishing a connection, we will enter the current_level's password and in response we should get the next level's password.

```
bandit16@bandit:~$ openssl s_client -connect localhost:31790
CONNECTED(00000003)
....
....
....
---
<bandit16_password>
Correct!
-----BEGIN RSA PRIVATE KEY-----
....
....
....
-----END RSA PRIVATE KEY-----

closed
bandit16@bandit:~$
```

Instead of a password, we are presented with a private key. Copy and paste this private key in a file to use it to connect to the next level.