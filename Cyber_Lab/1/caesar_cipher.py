def encrypt(plain_text, key):    
    return ''.join(chr(ord(letter) + key) for letter in plain_text) 

def decrypt(encrypted, key):    
    return ''.join(chr(ord(letter) - key) for letter in encrypted) 

def main():
    # Input
    plain_text = input("Enter a Message : ")
    key = int(input("Enter Secret Key : "))
    
    # Encryption
    encrypted = encrypt(plain_text, key)
    print(f'Encrypted : {encrypted}')
    
    # Decryption
    decrypted = decrypt(encrypted, key)
    print(f'Decrypted : {decrypted}')

if __name__ == "__main__":
    main()

# References 
# https://stackoverflow.com/questions/35820678/python-increment-characters-in-a-string-by-1