L= [2,4,3,5,6,7,1,2,3]
s = []
s.append(sum([i for i in L if i%2 == 0]))
s.append(sum([i for i in L if i%2 != 0]))
print(s)