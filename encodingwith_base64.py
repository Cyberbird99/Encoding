"""Text encoding is the process of converting human-readable characters
into a machine-readable format. 
Base64 is a binary to a text encoding scheme that represents binary data 
in an American Standard Code for Information Interchange (ASCII) string format"""

import base64

# First make a function to convert a plain text string to bytes
# encode the plain text and change the encoded bytes back to string

def encoding_data(text):
    text = text.encode()
    cipher_text = base64.b64encode(text)
    cipher_text = cipher_text.decode()
    return cipher_text

#Decode the cipher_text
# and change the decoded bytes to string

def decoding_data(cipher_text):
    text = base64.b64decode(cipher_text)
    text = text.decode()
    return text

# Ask the user for what method to use
# and what message to put in

method = input("Do you want to encode or decode (e/d)? ")
message_text = input("Put in your message: ")

# Now call the correct method, encode or decode,
# based on the user's input (use the first letter)
if method[0] == 'e':
    print(encoding_data(message_text))
elif method[0] == 'd':
    print(decoding_data(message_text))
else:
    # If the user put another word other than encode or decode
    print("Wrong selection. Choose encode(e) or decode(d)")