To connect, `ssh bandit29@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.


We have to clone a git repository and look for the password in that.


Git is a version control tool. It was created by the creator of Linux.

It is very useful to know the basics of git.


Continuing onto the current challenge, lets start by creating a directory in the **/tmp** folder and change the current directory to the newly created folder.

```
bandit29@bandit:~$ mkdir /tmp/<folder_name>
bandit29@bandit:~$ cd /tmp/<folder_name>
bandit29@bandit:/tmp/<folder_name>$
```


Now we will clone the git repository using the git clone command.

On being prompted for a password, enter the current level's password.

```
bandit29@bandit:/tmp/<folder_name>$ git clone ssh://bandit29-git@localhost/home/bandit29-git/repo
Cloning into 'repo'...
Could not create directory '/home/bandit29/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:<sha256_hash>.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit29/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit29-git@localhost's password: 
remote: Counting objects: 16, done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 16 (delta 2), reused 0 (delta 0)
Receiving objects: 100% (16/16), done.
Resolving deltas: 100% (2/2), done.
bandit29@bandit:/tmp/<folder_name>$ 
```

On successfully cloning the git repository, a folder will be created with the name repo.

We will change directory into that using cd.

```
bandit29@bandit:/tmp/<folder_name>$ ls
repo
bandit29@bandit:/tmp/<folder_name>$ cd repo
bandit29@bandit:/tmp/<folder_name>/repo$
```


On listing the files in the directory we will find a README file.

Lets print the contents of the README file.

```
bandit29@bandit:/tmp/<folder_name>/repo$ ls
README
bandit29@bandit:/tmp/<folder_name>/repo$ cat README
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>
bandit29@bandit:/tmp/<folder_name>/repo$ 
```

The README says no passwords in production. Maybe they have a separate development branch.


Lets list the different branches this repository has.

```
bandit29@bandit:/tmp/<folder_name>/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
```

We can see a branch called origin/dev

The **remotes/** prefix shows that the branch doesn't exist locally.

Lets shift to that branch and see if we can find the password.


```
bandit29@bandit:/tmp/<folder_name>/repo$ git checkout origin/dev
Note: checking out 'origin/dev'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at bc83328... add data needed for development
bandit29@bandit:/tmp/<folder_name>/repo$ ls
code  README.md
bandit29@bandit:/tmp/<folder_name>/repo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <bandit30_password>

bandit29@bandit:/tmp/<folder_name>/repo$ 
```

We get the password for the next level.

Before exiting, make sure to remove the folder created.

```
bandit29@bandit:/tmp/<folder_name>/repo$ cd ~
bandit29@bandit:~$ rm -rf /tmp/<folder_name>
```

With this we find the password for the next level.