strs = ["eat","tea","tan","ate","nat","bat"]
d = {}
for s in strs:
    order = ''.join(sorted(s))     #it will sort the string and join it to make a string again sorted will do like that ['a','e','t'] then with join it will make 'aet'   the main idea of this is to make a key for the dictionary..
    # print(order)
    # print(d)
    if order not in d:         #if order is not in d then add it to d with key as order and value as s in list  form   {'aet':['eat']} 
        d[order] = [s]
    else:
        d[order].append(s)    #if order is already in d then append the s to the value of that key in d {'aet':['eat','tea','ate']}
    # print(d)
    # print()
print(list(d.values()))


# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

