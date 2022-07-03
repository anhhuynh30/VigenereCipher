alphabet = "abcdefghijklmnopqrstuvwxyz"

message = "craking vigenere cipher with python is fun!"
keyword = "python"

# Function to code a plaintext message into Vigenere Cipher:
def coder(message, keyword):
	# First, combine message and keyword to make a keystring for the message:
    keyword_index = 0
    key_string = ""
    for i in range(0,len(message)):
        if message[i] in alphabet:
            key_string += keyword[keyword_index]
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            key_string += message[i]
    
	# Then coded the message by combining the index of each letter in the message and keystring:
    cipher = ""
    for i in range(0,len(message)):
        if message[i] in alphabet:
            message_index = alphabet.index(message[i])
            keystring_index = alphabet.index(key_string[i])
            cipher += alphabet[(message_index + keystring_index) % len(alphabet)]
        else:
            cipher += message[i]
    
    return cipher

vigenere_cipher = coder(message,keyword)
print(f"Vigenere Cipher : {vigenere_cipher}")

# Function to decode Vigenere Cipher into plaintext message
def decoder(cipher, keyword):
	# First, combine cipher and keyword to make a keystring for the cipher:
    keyword_index = 0
    key_string = ""
    for i in range(0,len(cipher)): 
        if cipher[i] in alphabet:
            key_string += keyword[keyword_index]
            keyword_index = (keyword_index + 1) % len(keyword)    
        else:
            key_string += cipher[i]
    # Then decode the cipher by subtracting the index of each letter in the letter to the keystring:
    decoded_msg = ""
    for i in range(0,len(cipher)):
        if cipher[i] in alphabet:
            cipher_index = alphabet.index(cipher[i])
            keystring_index = alphabet.index(key_string[i])
            decoded_msg += alphabet[(cipher_index - keystring_index) % len(alphabet)]
        else:
            decoded_msg += cipher[i]
    return decoded_msg

plaintext_message = decoder(vigenere_cipher,keyword)
print(f"Translated Message: {plaintext_message}")
