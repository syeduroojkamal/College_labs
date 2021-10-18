def encrypt(plain_text, key):    
    return ''.join(chr(ord(letter) + key) for letter in plain_text) 

def main():
    plain_text = input()
    key = int(input())
    print(encrypt(plain_text, key))

if __name__ == "__main__":
    main()