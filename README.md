
# Video Ciphering Algorithm

Security is a very big concern with Digital Systems in
Today's world. This projects aims to develop a Video Ciphering 
Algorithm which can safeguard our Videos. Not only Videos,
we can safeguard any sort of file format with the help of this Algorithm.


# Terminology 

Encryption: The process by which we can convert the input to a format which 
is not usable.

Decryption: The process by which we can convert the encrypted data back to original
input format.

Key: Key helps us in encryption and decryption. We can either have same 
key for both encryption and decryption or different keys for encryption and 
decryption.

Public Key Cryptography: When we have same key for both Encryption and Decryption,
it is called Public Key Cryptography. Example: DES, AES etc.

Private Key Cryptography: When we have different keys for Encryption and Decryption,
it is termed as Private Key Cryptography. Ex: RSA.

# Our Algorithm

We have gone for Public key Cryptography i.e. we will have same 
key for both encryption and decryption. 

We exploit the XOR operator to do encryption and decryption for us.

XOR:

Input:   1  0  1  1

Key:     0  1  0  1

Output:  1  1  1  0

So, we get the Decrypted output as 1 1 1 0.

If we want to restore it simply XOR the Decrypted Output back with the key.


Input:  1 1 1 0

Key:    0 1 0 1

Output: 1 0 1 1

The output is our original input back.

# Navigation

Cipher: Module containing class for encryption and decryption.

logger: Module containing Logger class which helps us in logging.

main.py: main script for the complete program.



## Screenshots
![App Screenshot](screenshots/Before%20Encrypting.JPG?raw=true)

Before Encrypting, the video is visible.


===================================================================================================================================


![App Screenshot](screenshots/encrypting%20the%20file.JPG?raw=true)

Encrypting the file, doing at the command line right now. In future, will create a complete application for the same.



===================================================================================================================================


![App Screenshot](screenshots/after%20encrypting.JPG?raw=true)

After Encrypting, the video is not watchable anymore.


===================================================================================================================================

![App Screenshot](screenshots/decrypting%20wrong%20key.JPG?raw=true)

Decrypting with the wrong key, the video should not be watchable still.

===================================================================================================================================


![App Screenshot](screenshots/unsuccessful%20decryption%20due%20to%20wrong%20key.JPG?raw=true)

Video still not watchable, as the key that we entered was wrong.

===================================================================================================================================

![App Screenshot](screenshots/right%20key.JPG?raw=true)

Decrypting with the right key.

===================================================================================================================================

![App Screenshot](screenshots/decrypting%20right%20key.JPG?raw=true)

Video is watchable now.
