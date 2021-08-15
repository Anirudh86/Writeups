To connect, `ssh bandit22@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.


We are told to look for cron jobs.

Cron jobs can be found in **/etc/cron.d/**.

Lets list the cronjobs from **/etc/cron.d/**.


```
bandit22@bandit:~$ ls /etc/cron.d/
cronjob_bandit15_root  cronjob_bandit22  cronjob_bandit24
cronjob_bandit17_root  cronjob_bandit23  cronjob_bandit25_root
bandit22@bandit:~$
```

Cronjobs are written to run at specified intervals. The interval could be every minute, every day, every 4 hours or any variation.


So we need to look for the cronjob of level 23 so that we can use that to get the password for level 23.


Lets print the contents of cronjob_bandit23.

```
bandit22@bandit:~$ cat /etc/cron.d/cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23 &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh &> /dev/null
bandit22@bandit:~$
```

The stars (*) represent - minute, hour, day of the month, month, day of the week.

Using these stars we can run cronjobs at any interval we want.


A site I find useful to quickly translate the cronjob interval into human readable interval is (Crontab Guru)[https://crontab.guru/].

It translate the interval from cronjob_bandit23.sh as every minute, meaning the cronjob will run every minute.


Lets print the contents of the file **/usr/bin/cronjob_bandit23.sh** as the cronjob runs it every minute.


```
bandit22@bandit:~$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
bandit22@bandit:~$
```

The **cronjob_bandit23.sh** script creates a variable **myname** and assigns it the result of the command `whoami`.

After which it creates a variable **mytarget**.

The script passes **I am user $myname** to md5sum via the pipe operator, while replacing $myname with its value.

The md5sum command computes the md5 hash of string passed to it.

And the result is then passed to the cut command.

The cut command is to split strings using the specified characters. The -f switch tells cut to print only those substrings which occur in the positions specified (it starts indexing from 1 and not from 0).


The cut command will return the md5 hash to mytarget variable.


When the script is run, the script has the permissions of bandit23 user.

So **whoami** command will return **bandit23**


The value of mytarget variable will be the output of `echo I am user bandit23 | md5sum | cut -d ' ' -f 1`. Try it for yourself to see the output.


Then the script prints the password of bandit23 from /etc/bandit_pass/bandit23 and stores it in /tmp/<value of mytarget variable>.


All we need to do is, print the contents of /tmp/<value of mytarget variable> and we will get the password for bandit23 user.

```
bandit22@bandit:~$ cat /tmp/<value of mytarget variable>
<bandit23_password>
bandit22@bandit:~$
```

With this we will get the password for the next level.