To connect, `ssh bandit21@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.


We are told to look for cron jobs.

Cron jobs can be found in **/etc/cron.d/**.

Lets list the cronjobs from **/etc/cron.d/**.


```
bandit21@bandit:~$ ls /etc/cron.d/
cronjob_bandit15_root  cronjob_bandit22  cronjob_bandit24
cronjob_bandit17_root  cronjob_bandit23  cronjob_bandit25_root
bandit21@bandit:~$
```

Cronjobs are written to run at specified intervals. The interval could be every minute, every day, every 4 hours or any variation.


So we need to look for the cronjob of level 22 so that we can use that to get the password for level 22.


Lets print the contents of cronjob_bandit22.

```
bandit21@bandit:~$ cat /etc/cron.d/cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22 &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
bandit21@bandit:~$
```

The stars (*) represent - minute, hour, day of the month, month, day of the week.

Using these stars we can run cronjobs at any interval we want.


A site I find useful to quickly translate the cronjob interval into human readable interval is (Crontab Guru)[https://crontab.guru/].

It translate the interval from cronjob_bandit22.sh as every minute, meaning the cronjob will run every minute.


Lets print the contents of the file **/usr/bin/cronjob_bandit22.sh** as the cronjob runs it every minute.


```
bandit21@bandit:~$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:~$
```


The **cronjob_bandit22.sh** script sets the permission of the file **/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv** to read-write for user, read-only for group and read-only only for everyone else.

Then the script prints the password for bandit22 user and stores it in **/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv**.


All we would need to do is print the contents of **/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv** and we will get the password for bandit22 user.

```
bandit21@bandit:~$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
<bandit22_password>
bandit21@bandit:~$
```

With this we will get the password for the next level.