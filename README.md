**Vigenère Cipher**

Unlike **Caesar Cipher** which was a monoalphabetic substitution cipher, **Vigenère Cipher** is a polyalphabetic substitution cipher. A polyalphabetic cipher is any cipher based on substitution, using multiple substitution alphabets. In other words, instead of having a single offset/shift applied to every letter as in **Caesar Ciper**, the **Vigenère Cipher** has a different offset for each individual letter.The value of the offset for each letter is determined by a given *keyword*. The *keyword* is a word or phrase that is repeated as many times as required to encipher a message.

Sources: [Vigenère Cipher](https://www.geeksforgeeks.org/vigenere-cipher/)

For example, given the *message* as *BARRY IS THE SPY* and the *keyword* as *DOG*, we have the following:

Message:				B  A  R  R  Y   I  S   T  H  E   S  P  Y

Keystring:				D  O  G  D  O   G  D   O  G  D   O  G  D

Resulting place value:	4  14 23 20 38  14 21  33 13 7   32 21 27

Vigenère Cipher:		E  O  X  U  M   O  V   H  N  H   G  V  B

The alphabet has 26 letters starting with A, which has an index of 0 and ending with Z, which has the index of 25.

So, in the above example, if we shift *B* (index of 1) with *D* (index of 3), it will give us an index value of **1+3 = 4** which is letter *E*. Similarly, when we shift *A* (index of 0) with *O* (index of 14) we will get the index of **0+14 = 14**, which is letter *O*, and so forth. Since there is only 26 letters in the alphabet, therefore, for the cases that have **resulting place value larger than 26** we need to use modulus *%* to find the place value. For example, when shifting *Y* (index of 24) with *O* (index of 14), we will get the letter *M* since **(24+14) % 26 = 12**. The letter that has the index of 12 is *M*.

In this project, I will write two functions named **coder** and **decoder** to encrypt and decrypt the messages, respectively.