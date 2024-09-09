#118 pascals triangle 

#Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

#In Pascal's triangle, each number is the sum of the two numbers directly above it.

# solution :

# 1. create a list of lists called result
# 2. iterate through the range of numRows
# 3. create a row list with 1 as the first element 
# 4. iterate through the range of 1 to i 
# 5. append the sum of the previous row's j-1 and jth element to the row list 
# 6. append the row list to the result list 
# 7. return the result list

numArrays=5
result =[]

for i in range(numArrays):
    row=[1]
    for j in range(1,i):
        row.append(result[i-1][j-1]+result[i-1][j])
    if i>0:
        row.append(i)
    result.append(row)
print(result)


numArrays=5
result =[]

for i in range(numArrays):
    row=[1]
    for j in range(1,i):
        row.append(result[i-1][j-1]+result[i-1][j])
    if i>0:
        row.append(1)
    result.append(row)
print(result)