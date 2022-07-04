**Vigenère Cipher**

Unlike **Caesar Cipher** which was a monoalphabetic substitution cipher, **Vigenère Cipher** is a polyalphabetic substitution cipher. A polyalphabetic cipher is any cipher based on substitution, using multiple substitution alphabets. In other words, instead of having a single offset/shift applied to every letter as in **Caesar Ciper**, the **Vigenère Cipher** has a different offset for each individual letter.The value of the offset for each letter is determined by a given *keyword*. The *keyword* is a word or phrase that is repeated as many times as required to encipher a message.

For example, given the *message* as *BARRY IS THE SPY* and the *keyword* as *DOG*, we have the following:

Message:				B  A  R  R  Y   I  S   T  H  E   S  P  Y

Keystring:				D  O  G  D  O   G  D   O  G  D   O  G  D

Resulting place value:	4  14 23 20 38  14 21  33 13 7   32 21 27

Vigenère Cipher:		E  O  X  U  M   O  V   H  N  H   G  V  B


