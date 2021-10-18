# initializing dictionary
test_dict = {
    1: "Geeksforgeeks",
	2: "best for", 
    3: "all geeks"
}
print("The original dictionary is : " + str(test_dict))
limit = 4

chunks = (sub[idx: idx + limit] for sub in test_dict.values() for idx in range(0, len(sub), limit))
res = {key: val for key, val in enumerate(chunks, 1)}

print("The extracted values : " + str(res))
