def encrypt(plain_text, key):    
    return ''.join(chr(ord(letter) + key) for letter in plain_text) 

def decrypt(plain_text, key):    
    return ''.join(chr(ord(letter) - key) for letter in plain_text) 

def main():
    # Input
    plain_text = input("Enter a Message : ")
    key = int(input("Enter Secret : "))
    
    # Encryption
    encrypted = encrypt(plain_text, key)
    print(f'Encrypted : {encrypted}')
    
    # Decryption
    decrypted = decrypt(encrypted, key)
    print(f'Decrypted : {decrypted}')

if __name__ == "__main__":
    main()