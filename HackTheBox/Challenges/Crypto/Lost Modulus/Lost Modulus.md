_Title_: Lost Modulus
_Description_: I encrypted a secret message with RSA but I lost the modulus. Can you help me recover it?

Download the zip provided and unzip using the password provided.
We will see two files - challenge.py and output.txt.
On inspecting output.txt, we will find a encrypted flag inside it which we must decrypt.
Move on towards challenge.py, we will find the code for encryption and decryption.

In the \_\_init\_\_ function, getPrime function is used, which on every run of the file, will generate random prime.
We have 5 variables - _p_, _q_, _e_, _d_, _n_. The only variable whose value we know is e. And we also know the cipher text from the output.txt file.

For decrypting the cipher text to plaintext, we will need _n_ and _d_.
Finding d will be difficult as it would require _p_ and _q_.

Reading up on _RSA_ will tell us that values of d and e should not be a small number.
Having a small number as the value of e leads to **low exponent attack**.

A good resource to know more in detail about this is [Crypto StackExchange](https://crypto.stackexchange.com/questions/6713/low-public-exponent-attack-for-rsa).

For decrypting the flag, we will use the python library _gmpy2_. This will be useful to find the cuberoot of the encrypted flag.

We already know the flag is in hex format from the code in challenge.py. We will copy only the flag value and store it in a file called flag.txt.

Our script to solve the challenge will read the flag value from flag.txt and then we will convert the flag value into an integer from hex. Using gmpy, we will find the cuberoot of the flag integer. The cuberoot will be an object returned by gmpy2's cuberoot function. So we convert it into an integer and then into hex which will make it easier to decode into string. Once decoded, we will have our flag and we will have solved the challenge.