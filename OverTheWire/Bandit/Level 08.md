
To connect, `ssh bandit8@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

List the files in the current directory using ls.

```
bandit8@bandit:~$ ls
data.txt
```

We have told that the password is the only line occuring once in data.txt.

So we can safely assume that every other line in data.txt atleast occurs twice.

To find the line which occurs once, we will need to sort the data and then remove all lines which occur more than once.

Sorting the data ensures that the lines which occur more than once are grouped together, hence making it easier to remove.

Fortunately, we have our work cut out for us as there are commands specifically for these tasks - **sort** and **uniq**.

The sort command, as the name suggests will sort the file in lexicographically ascending order.

The uniq command can be used to find or omit repeated lines. In this case we want to omit the repeated lines, so we will use the -u switch with it.

```
bandit8@bandit:~$ sort data.txt | uniq -u
<bandit9_password>
```

With this we will get the password to the next level.