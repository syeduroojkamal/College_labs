t = [('P',89,'A'), ('Z',15,'C'), ('A',25,'R'), ('T',95,'E')]

o = [25, 95, 89, 15]
print(sorted(t, key = lambda i:o.index(i[1])))