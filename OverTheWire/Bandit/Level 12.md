To connect, `ssh bandit12@bandit.labs.overthewire.org -p 2220`.

On being prompted for a password, enter the password found from the previous level.

After a successful connection, we are presented with a shell.

List the files in the current directory using ls.

```
bandit12@bandit:~$ ls
data.txt
```

Print the contents of data.txt to screen.

```
bandit12@bandit:~$ cat data.txt
00000000: 1f8b 0808 0650 b45e 0203 6461 7461 322e  .....P.^..data2.
00000010: 6269 6e00 013d 02c2 fd42 5a68 3931 4159  bin..=...BZh91AY
...
...
...
00000240: 7426 072f fc28 ab05 9603 b3fc 5dc9 14e1  t&./.(......]...
00000250: 4242 393c 7320 98f7 681d 3d02 0000       BB9<s ..h.=...
```

This is a hexdump. We will need to reverse it to recreate the file it was originally.

But first, create a directory in /tmp folder to work in using mkdir command.

Replace the __folder\_name__ with any name of your choice.

```
bandit12@bandit:~$ mkdir /tmp/<folder_name>

```

Copy the hexdump file (data.txt) into the newly created folder using cp command.

And change current directory to the newly created folder using cd.

```
bandit12@bandit:~$ cp data.txt /tmp/<folder_name>
bandit12@bandit:~$ cd /tmp/<folder_name>
bandit12@bandit:/tmp/<folder_name>$
```

Now, to reverse a hexdump, we will use xxd.

Xxd is useful to make a hexdump and to reverse it. We will use its -r switch to reverse the hexdump.

Print the hexdump using cat and pass the output to xxd using the pipe operator (|). After which, redirect, using the redirection operator (>), xxd's output to a file with the name of your choice.

```
bandit12@bandit:/tmp/<folder_name>$ cat data.txt | xxd -r > <file_name>
```

To find what the type of file is, use the file command.

```
bandit12@bandit:/tmp/<folder_name>$ file <file_name>
<file_name> gzip compressed data, was "data2.bin", last modified: Thu May 7 18:14:30 2020, max compression, from Unix
```

We find that the file is a **gzip** compressed file. To unzip a **gzip** compressed file, we can gunzip or zcat.

We will use zcat, because at the time of writing this, gunzip was not available on this level's system.

Zcat will decompress the file and we will redirect the output using **>** to another file.

We will also run file on the decompressed file to determine its file type.

```
bandit12@bandit:/tmp/<folder_name>$ mv <file_name> <file_name>.gz
bandit12@bandit:/tmp/<folder_name>$ zcat <file_name>.gz > <another_file_name>
bandit12@bandit:/tmp/<folder_name>$ file <another_file_name>
<another_file_name>: bzip2 compressed data, block size = 900k
```

This decompressed file is a bzip2 compressed file.

We were told that the file is compressed multiple times.

So, till we don't find a plain-text file, each time we decompress the file, the output will another file compressed using a different or the same compression

We will use the file command after each decompression, to ascertain how to decompress the file and to stop when we reach a plain-text file.

And we will rename the file to add the appropriate extension.

To decompress bzip2 file, we will bzip2 command.

The -d switch tells bzip2 to decompress the file, and the -k switch is used to ensure the original zip file is not removed after being decompressed.

```
bandit12@bandit:/tmp/<folder_name>$ mv <another_file_name> <another_file_name>.bz2
bandit12@bandit:/tmp/<folder_name>$ bzip2 -d -k <another_file_name>.bz2
bandit12@bandit:/tmp/<folder_name>$ file <another_file_name>
<another_file_name> gzip compressed data, was "data4.bin", last modified: Thu May 7 18:14:30 2020, max compression, from Unix
```

We get another gzip file to decompress. We will use zcat as we have done before.

```
bandit12@bandit:/tmp/<folder_name>$ mv <another_file_name> <another_file_name>.gz
bandit12@bandit:/tmp/<folder_name>$ zcat <another_file_name> > <file_name>
bandit12@bandit:/tmp/<folder_name>$ file <file_name>
<file_name>: POSIX tar archive (GNU)
```

On decompressing the gzip file, we get a tar file.

To decompress a tar file, we will use the tar command.

The -x switch is used to tell tar to decompress or extract the contents of the file. And the -f switch tells tar to use the archive file specified.


```
bandit12@bandit:/tmp/<folder_name>$ mv <file_name> <file_name>.tar
bandit12@bandit:/tmp/<folder_name>$ tar -xf <file_name>.tar
data5.bin
bandit12@bandit:/tmp/<folder_name>$ file data5.bin
<data5.bin>: POSIX tar archive (GNU)
```

Further decompressions will be one of gzip, bzip2 or tar. We know the commands to use.

So we will keep using the commands according to specified compression used.

```
bandit12@bandit:/tmp/<folder_name>$ mv data5.bin <file_name>.tar
bandit12@bandit:/tmp/<folder_name>$ tar -xf <file_name>.tar
data6.bin
bandit12@bandit:/tmp/<folder_name>$ file data6.bin
<data6.bin>: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/<folder_name>$
bandit12@bandit:/tmp/<folder_name>$
bandit12@bandit:/tmp/<folder_name>$ mv data6.bin <file_name>.bz2
bandit12@bandit:/tmp/<folder_name>$ bzip2 -d -k <file_name>.bz2
bandit12@bandit:/tmp/<folder_name>$ file <file_name>
<file_name>: POSIX tar archive (GNU)
bandit12@bandit:/tmp/<folder_name>$
bandit12@bandit:/tmp/<folder_name>$
bandit12@bandit:/tmp/<folder_name>$ mv <file_name> <file_name>.tar
bandit12@bandit:/tmp/<folder_name>$ tar -xf <file_name>.tar
data8.bin
bandit12@bandit:/tmp/<folder_name>$ file data8.bin
<file_name> gzip compressed data, was "data9.bin", last modified: Thu May 7 18:14:30 2020, max compression, from Unix
bandit12@bandit:/tmp/<folder_name>$
bandit12@bandit:/tmp/<folder_name>$
bandit12@bandit:/tmp/<folder_name>$ mv data9.bin <file_name>.gz
bandit12@bandit:/tmp/<folder_name>$ zcat <file_name>.gz > <another_file_name>
bandit12@bandit:/tmp/<folder_name>$ file <another_file_name>
<another_file_name>: ASCII text
bandit12@bandit:/tmp/<folder_name>$ cat <another_file_name>
<bandit12_password>
```

Before exiting this level, change to the home directory (~) and then remove the folder which was created.

```
bandit12@bandit:/tmp/<folder_name>$ cd ~
bandit12@bandit:/tmp/<folder_name>$ rm -rf /tmp/<folder_name>
```

With this we will get the password to the next level.
