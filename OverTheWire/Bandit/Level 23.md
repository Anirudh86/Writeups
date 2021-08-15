To connect, `ssh bandit23@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.


We are told to look for cron jobs.

Cron jobs can be found in **/etc/cron.d/**.

Lets list the cronjobs from **/etc/cron.d/**.


```
bandit23@bandit:~$ ls /etc/cron.d/
cronjob_bandit15_root  cronjob_bandit22  cronjob_bandit24
cronjob_bandit17_root  cronjob_bandit23  cronjob_bandit25_root
bandit23@bandit:~$
```

Cronjobs are written to run at specified intervals. The interval could be every minute, every day, every 4 hours or any variation.


So we need to look for the cronjob of level 24 so that we can use that to get the password for level 24.


Lets print the contents of cronjob_bandit24.

```
bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24
@reboot bandit23 /usr/bin/cronjob_bandit24 &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:~$
```

The stars (*) represent - minute, hour, day of the month, month, day of the week.

Using these stars we can run cronjobs at any interval we want.


A site I find useful to quickly translate the cronjob interval into human readable interval is (Crontab Guru)[https://crontab.guru/].

It translate the interval from cronjob_bandit24.sh as every minute, meaning the cronjob will run every minute.


Lets print the contents of the file **/usr/bin/cronjob_bandit24.sh** as the cronjob runs it every minute.


```
bandit23@bandit:~$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done

bandit23@bandit:~$
```


Lets understand the what this bash script does.

Firstly, it creates a variable myname to which it assigns the result of the command **whoami**.
As the cronjob runs as bandit24 user, whoami will return bandit24.

Then, it changes directory and goes into `/var/spool/$myname` which will be `/var/spool/bandit24`.


After which it runs a for loop.

The range of the for loop is the array of all files, hidden and not hidden files both.

The loop variable **i** in every iteration, holds the name of a file which is present in /var/spool/bandit24 folder.

In every iteration, it checks if the value of **i** is not **.** (used to indicate current directory) and also the value of **i** is not **..** (used to indicate parent directory).


When the if expression evaluates to true, it prints **Handling <value_of_i>**.

Then it finds the owner of the file (value of i) by using the stat command.


The stat command prints information about the metadata of the file such as size, creation, modification dates, owner, etc.


The variable owner stores the result of the stat command.

Only if the owner of the file is bandit23, it will execute the file **i** with a timeout of 60 seconds.

After 60 seconds, it will send the SIGKILL (9) signal which is specified by the -s switch.


And after the if expression, it deletes the file **i**.


So to get the password for bandit24, we will need to write a script and place it in the **/var/spool/bandit24** directory so that it is executed.

The script will be run with bandit24 user permissions. So we can copy the password from **/etc/bandit_pass/bandit24** and paste it in a file which we control.



Lets start by checking the permissions of /var/spool/bandit24 to see if we have write access.


```
bandit23@bandit:~$ ls -al /var/spool/bandit24
drwxrwx-wx 21 root bandit24 4096 Aug 12 08:32 bandit24
bandit23@bandit:~$
```

The last 3 bits of the permission has **-wx** signifying that anyone has write and execute permissions in **/var/spool/bandit24**.


Lets create our script in **/var/spool/bandit24**.
Create the script using `touch /var/spool/bandit24/<scriptname>.sh`.


Once the file is created, we need to add code into it.

To do so, we can use nano or vim. Open the file using nano or vim, and add the following lines of code.

```
#!/bin/bash

cat /etc/bandit_pass/bandit24 > /tmp/<file_name>
```

Change the permissions of the script to make sure anybody can read/write/execute the script using `chmod 777 /var/spool/bandit24/<scriptname>.sh`.


Also make sure to keep a copy of the script locally, because the script is deleted after its iteration.


Then create the file in which the password will be written using `touch /tmp/<file_name>`.

And give write permissions to anyone for the file using `chmod 777 /tmp/<file_name>`



Now wait for a minute and then print the contents of the file using cat.


```
bandit23@bandit:~$ cat /tmp/<file_name>
<bandit24_password>
```


Be sure to remove the file before closing the connection.


With this we will get the password for the next level.