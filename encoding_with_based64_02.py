import base64

def encode_data(text):
    """
    Encodes a plain text string into base64 format.
    """
    try:
        text_bytes = text.encode('utf-8')  # Convert text to bytes
        encoded_bytes = base64.b64encode(text_bytes)  # Encode to base64
        return encoded_bytes.decode('utf-8')  # Convert bytes back to string
    except Exception as e:
        return f"Error during encoding: {e}"

def decode_data(cipher_text):
    """
    Decodes a base64-encoded string back to plain text.
    """
    try:
        decoded_bytes = base64.b64decode(cipher_text)  # Decode base64 to bytes
        return decoded_bytes.decode('utf-8')  # Convert bytes back to string
    except Exception as e:
        return f"Error during decoding: {e}. Make sure it's a valid base64 string."

def main():
    """
    Main function to ask the user for input and perform encoding or decoding.
    """
    method = input("Do you want to encode or decode (e/d)? ").strip().lower()
    if method not in ['e', 'd']:
        print("Invalid choice. Please choose 'e' for encode or 'd' for decode.")
        return
    
    message = input("Enter your message: ").strip()
    
    if method == 'e':  # Encode
        result = encode_data(message)
        print(f"Encoded message: {result}")
    elif method == 'd':  # Decode
        result = decode_data(message)
        print(f"Decoded message: {result}")

if __name__ == "__main__":
    main()
