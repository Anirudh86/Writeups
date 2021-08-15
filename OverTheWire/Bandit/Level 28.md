To connect, `ssh bandit28@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.


We have to clone a git repository and look for the password in that.


Git is a version control tool. It was created by the creator of Linux.

It is very useful to know the basics of git.


Continuing onto the current challenge, lets start by creating a directory in the **/tmp** folder and change the current directory to the newly created folder.

```
bandit28@bandit:~$ mkdir /tmp/<folder_name>
bandit28@bandit:~$ cd /tmp/<folder_name>
bandit28@bandit:/tmp/<folder_name>$
```


Now we will clone the git repository using the git clone command.

On being prompted for a password, enter the current level's password.

```
bandit28@bandit:/tmp/<folder_name>$ git clone ssh://bandit28-git@localhost/home/bandit28-git/repo
Cloning into 'repo'...
Could not create directory '/home/bandit28/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:<sha256_hash>.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit28/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit28-git@localhost's password: 
remote: Counting objects: 9, done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 9 (delta 2), reused 0 (delta 0)
Receiving objects: 100% (9/9), done.
Resolving deltas: 100% (2/2), done.
bandit28@bandit:/tmp/<folder_name>$ 
```

On successfully cloning the git repository, a folder will be created with the name repo.

We will change directory into that using cd.

```
bandit28@bandit:/tmp/<folder_name>$ ls
repo
bandit28@bandit:/tmp/<folder_name>$ cd repo
bandit28@bandit:/tmp/<folder_name>/repo$
```


On listing the files in the directory we will find a README file.

Lets print the contents of the README file.

```
bandit28@bandit:/tmp/<folder_name>/repo$ ls
README
bandit28@bandit:/tmp/<folder_name>/repo$ cat README
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx
bandit28@bandit:/tmp/<folder_name>/repo$ 
```

We see that the credentials are not shown. Maybe they were removed.

To confirm this, we will check the commits made.


The -n switch tells git log the number of commits to show, with the most recent being shown first.

```
bandit28@bandit:/tmp/<folder_name>/repo/$ git log -n 10
commit edd935d60906b33f0619605abd1689808ccdd5ee
Author: Morla Porla <morla@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    fix info leak

commit c086d11a00c0648d095d04c089786efef5e01264
Author: Morla Porla <morla@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    add missing data

commit de2ebe2d5fd1598cd547f4d56247e053be3fdc38
Author: Ben Dover <noone@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    initial commit of README.md
bandit28@bandit:/tmp/<folder_name>/repo/$ 

```

We can see the commit before the current commit has the message **add missing data**.
And the current commit has the message **fix info leak**.


So let us see what were the contents of README file at commit **add missing data**.


To move to a different commit, we use the git checkout command and we pass the commit has as an argument.

The commit hash for **add missing data** is **c086d11a00c0648d095d04c089786efef5e01264**.


```
bandit28@bandit:/tmp/<folder_name>/repo$ git checkout c086d11a00c0648d095d04c089786efef5e01264
Note: checking out 'c086d11a00c0648d095d04c089786efef5e01264'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at c086d11... add missing data
bandit28@bandit:/tmp/<folder_name>/repo$ cat README.md 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: <bandit29_password>

bandit28@bandit:/tmp/<folder_name>/repo$ 
```



We get the password for the next level.

Before exiting, make sure to remove the folder created.

```
bandit28@bandit:/tmp/<folder_name>/repo$ cd ~
bandit28@bandit:~$ rm -rf /tmp/<folder_name>
```

With this we find the password for the next level.