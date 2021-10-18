def midmerge(st,wrd):
  return s[:len(st)//2] + wrd + s[len(st)//2:]
s=input("enter the string")
wd=input("enter the word")
print(midmerge(s,wd))