_Title_: Emdee five for life

_Description_: Can you encrypt fast enough?

Launch the instance and visit the instance ip given.
On visiting the site, we are greeted with the following page.

![Screenshot 1.png](Screenshot%201.png)

We are given a string to hash using MD5. Lets hash the string and submit the result to see what happens.

For computing a hash online, a good and versatile tool is [CyberChef](https://gchq.github.io/CyberChef/).
Once we get the hashed value from CyberChef, we paste it into the text box and submit it.
On submission, we are shown another string to hash and that we were too slow.

![Screenshot 2.png](Screenshot%202.png)

Looks like we will need to write a script to make the request, hash the string value and submit it for us to be fast enough.

Let's start by inspecting the source code of this page.

![Screenshot 3.png](Screenshot%203.png)

In the source code, we see that the string value is in a **h3** tag. And for submitting a response, we need to make a post request with the key **hash** and its value the hash we will compute.
We will use python and its libraries - requests, re and hashlib.

The steps we will follow in the script are:
  - Make a GET request to the instance ip
  - Remove html tags using regex so that only text remains
  - Extract the string value by splitting the text on **string** as that is the word before the string to be hashed in the source code of the html page.
  - Compute the MD5 hash of the string to be hashed
  - Make a POST request to the instance ip and send the hashed value with the key **hash** as data
  - Print the response to screen and get the flag

Once we write and run our script, we will get the flag.
  
And we solve this challenge.
