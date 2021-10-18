ini_string = input("Enter string : ")
print ("initial string : ", ini_string)
res1 = ''.join(c for c in ini_string if c in '0123456789')
print ("after extraction string result: ", str(res1))