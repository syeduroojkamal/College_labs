from itertools import chain
testlist = [{'a':3,'b':7},{'a':3,'b':1,'c':5},{'a':8}]
allkeys = set(chain.from_iterable(testlist))
res = [dict((key,sub.get(key,None))for key in allkeys)for sub in testlist]
print('reformed dictonaries list',str(res))