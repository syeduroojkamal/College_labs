def encrypt(s,n):
  fence = [[] for i in range(n)]
  rail  = 0
  var   = 1

  for char in s:
    fence[rail].append(char)
    rail += var
    if rail == n-1 or rail == 0:
      var = -var

  res = ''
  for i in fence:
    for j in i:
      res += j

  return res

def decrypt(s,n):
    fence = [[] for i in range(n)]
    rail  = 0
    var   = 1

    for char in s:
        fence[rail].append(char)
        rail += var

        if rail == n-1 or rail == 0:
            var = -var

    rFence = [[] for i in range(n)]

    i = 0
    l = len(s)
    s = list(s)
    for r in fence:
        for j in range(len(r)):
            rFence[i].append(s[0])
            s.remove(s[0])
        i += 1

    rail = 0
    var  = 1
    r = ''
    for i in range(l):
        r += rFence[rail][0]
        rFence[rail].remove(rFence[rail][0])
        rail += var

        if rail == n-1 or rail == 0:
            var = -var
    return r

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

# References 
# http://github.com/CrypTools/RailfenceCipher