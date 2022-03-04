
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

![Before Encrypting](SCREENSHOTS/Before Encrypting.JPG)

