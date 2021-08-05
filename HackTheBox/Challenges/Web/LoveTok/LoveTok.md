_Title_: **LoveTok**
_Description_: True love is tough, and even harder to find. Once the sun has set, the lights close and the bell has rung... you find yourself licking your wounds and contemplating human existence. You wish to have somebody important in your life to share the experiences that come with it, the good and the bad. This is why we made LoveTok, the brand new service that accurately predicts in the threshold of milliseconds when love will come knockin' (at your door). Come and check it out, but don't try to cheat love because love cheats back. 💛

Launch the instance and download the file provided. A password will also be shown which will be useful to unzip the downloaded zip.
On visiting the instance url, we are greeted with the following website.
![[Screenshot 1.png]]
Lets start with checking the source code of the webpage.
In the source code, we find two js files, main.js and koulis.js. We can also see that the timer counting down in the web page, is in a span tag with id as time. This might be useful later.
![[Screenshot 2.png]]
Going through the js files we find,
  - main.js has the countdown logic which is seen on main page
  - koulis.js has a function for rendering a meme and some text on canvas. it says its not part of the challenge

The js files were a deadend. However, in the source of web page, we find the button **Nahh doesn't work for me** which on clicking adds a parameter **format** to the URL.
![[Screenshot 3.png]]
On clicking the button, we notice the count down time changes and the format parameter gets added to the URL.

On changing the value of format parameter from r to a, we can see that the time printed shows **pm** (or it could show **am** depending on the time of the instance).
![[Screenshot 4.png]]
This confirms that the value of format parameter is being used to format a random date and display it.
This can be further confirmed by using **dmy** as value of format
![[Screenshot 5.png]]

We also have the zip that we had downloaded. Upon unzipping it using the password provided, we are presented with a few files and folders.
The flag file that we find is a deadend (this was obvious).
On inspecting the **entrypoint.sh** file, we can see that the flag file is renamed to flag appended with random characters. This means that everytime we restart the instance, the flag file will have a new name. Also the location of the flag file is the root directory. This will be important later when we need to read the flag file.

Moving onto the challenge folder, we inspect the index.php file. We don't need to read or understand the complete file. The important line is the line which states that when a browser visits the root path of the URL, the server will pass control to the TimeController file.

Based on the name, TimeController should be in controllers folder.
On inspecting TimeController.php, we see that only a single function index has been defined.
The index function checks if the parameter format is present in the URL
	- if present, it extracts and returns the value of the format parameter
	- if not present, it returns the default value as **r**
The variable format after being assigned a value, is passed to an object of TimeModel.

Going by the name, TimeModel should be present in the models folder.
On inspecting TimeModel.php, we see two functions being defines - \_\_construct and getTime.
On creation of a object, the constructor of that class is called. So we can safely assume that \_\_construct must be called. In \_\_construct, we see a function addslashes being used.
This function is used to escape any single or double quotes in the variable format. This would mean that if we pass any quotes in our payload it will be escaped and the payload won't execute as desired.

Lets come back to bypassing addslashes function in a moment.
Moving onto the second function getTime, we see that the date is formatted according to the format specified. But all of this is done in eval.
This is our attack vector. Eval is an unsafe function because it will execute any code passed to it. This can lead to code injection.
We need to pass our payload from the format parameter, and it will executed by eval and its output will be returned to us.

For the value of format to be executed before being formatted by date function, we need it to be executed and the output of the execution should be concatenated. One technique of expression being executed before being concatenated is by using \${}. By placing our payload between the brackets, it will executed and its value will concatenated.
Lets try listing all the files in the current directory. We can use echo or print to get the output of the `ls` command. But if we pass `ls` in quotes to print, then it won't work.
In linux command line, we can wrap our commands in backticks (\`\`) and it will execute.
So trying the same in php results in wrapping `ls` with backticks (\`\`) and then passing it to print.
The payload will be ``${print(`ls`)}``. This will also bypass addslashes as we have no single or double quote in our payload. The URL will be ``http://<instance IP and Port>/?format=${print(`ls`)}``
![[Screenshot 6.png]]
It worked. We can see the names of the folders and files matching those that we extracted from the zip.

For finding the flag there are two techniques:
  1. Find the name of the flag by listing folders and files in root directory. Then print contents of flag file.
  2. Print contents of files in root directory starting with flag using regex `flag*`.

_Technique 1 :_
We know that the flag is in the root folder. So lets try listing all files in the root folder to find the name of the flag file. We will replace `ls` with `ls /` in the payload. The URL will be  ``http://<instance IP and Port>/?format=${print(`ls /`)}``
![[Screenshot 7.png]]
The flag file is **flag2yGnq**. But it will be different every time the instance is run.
For printing the flag, we can use the cat command. Change `ls /` to `cat /flag2yGnq` in the payload. And the flag will be printed. URL will be ``http://<instance IP and Port>/?format=${print(`cat /flag2yGnq`)}``

_Technique 2 :_
In case we want to skip the step of finding out the name of the flag file, we use `cat /flag*` to print the contents of the file(s) starting with the word flag. URL will be ``http://<instance IP and Port>/?format=${print(`cat /flag*`)}``

Using either technique, we will be able to view the flag and solve the challenge.