# method to convert char to ascii
def convertToAscii(char):
    return ord(char)

# method to revert ascii to char
def convertToChar(ascii):
    return chr(ascii)

# encrypt text method
def encrypt_text(string, shift_count):
    encrypted_text = ""
    for s in string:
        encrypted_text+=convertToChar(convertToAscii(s) + shift_count)
    return encrypted_text

# decrypt text method      
def decrypt_text(string, shift_count):
    decrypted_text = ""
    for s in string:
        decrypted_text+=convertToChar(convertToAscii(s) - shift_count)
    return decrypted_text

