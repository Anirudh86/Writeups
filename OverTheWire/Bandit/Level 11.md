To connect, `ssh bandit11@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

List the files in the current directory using ls.

```
bandit11@bandit:~$ ls
data.txt
```

We are told that all the letters have been rotated 13 positions.

This means, a -> n, b -> o, c -> p.

And n -> a, b -> o, c -> p.

The same holds true for uppercase characters, that is, A to Z.


As there are 26 letters and the letters have been rotated 13 positions, rotating them 13 positions again will bring them back to their original position.

So if we rotate all characters in the string 13 positions, we will get the original message back.

To do so, we will first print the characters from data.txt and pass them to tr command using the pipe command.

The tr command is used to translate or delete characters. We will use to replace characters for rotating them 13 poisitions.

And to do so, we will use simple regex.

Tr will map each character in the first argument to each character in the second argument.

So A,B,C,...K,L,M maps to N,O,P...X,Y,Z and N,O,P maps to A,B,C...K,L,M.

Same will follow for lower case.

```
bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
The password is <bandit11_password>
```

With this we will get the password to the next level.