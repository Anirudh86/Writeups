To connect, `ssh bandit27@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.


We have to clone a git repository and look for the password in that.


Git is a version control tool. It was created by the creator of Linux.

It is very useful to know the basics of git.


Continuing onto the current challenge, lets start by creating a directory in the **/tmp** folder and change the current directory to the newly created folder.

```
bandit27@bandit:~$ mkdir /tmp/<folder_name>
bandit27@bandit:~$ cd /tmp/<folder_name>
bandit27@bandit:/tmp/<folder_name>$
```


Now we will clone the git repository using the git clone command.

On being prompted for a password, enter the current level's password.

```
bandit27@bandit:/tmp/<folder_name>$ git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
Cloning into 'repo'...
Could not create directory '/home/bandit27/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:<sha256_hash>.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit27-git@localhost's password: 
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (3/3), done.
bandit27@bandit:/tmp/<folder_name>$ 
```

On successfully cloning the git repository, a folder will be created with the name repo.

We will change directory into that using cd.

```
bandit27@bandit:/tmp/<folder_name>$ ls
repo
bandit27@bandit:/tmp/<folder_name>$ cd repo
bandit27@bandit:/tmp/<folder_name>/repo$
```


On listing the files in the directory we will find a README file.

Lets print the contents of the README file.

```
bandit27@bandit:/tmp/<folder_name>/repo$ ls
README
bandit27@bandit:/tmp/<folder_name>/repo$ cat README
The password to the next level is: <bandit28_password>
bandit27@bandit:/tmp/<folder_name>/repo$ 
```

We get the password for the next level.

Before exiting, make sure to remove the folder created.

```
bandit27@bandit:/tmp/<folder_name>/repo$ cd ~
bandit27@bandit:~$ rm -rf /tmp/<folder_name>
```

With this we find the password for the next level.