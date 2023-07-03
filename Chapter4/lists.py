# Grow & Shrink (Append & Pop)
L = [1, 'spam', 3.33]
print('L length is ' + str(len(L)))
print(L[0])
print(L[:-1])
print(L + [4, 'five', 6.66])

print("\n-------------------")

L.append(4) # Growing by adding an object at the end of list
print(L)

L.pop(0) # Shrinking by deleting an item from position
print(L)
del L[0] # Same as pop ^
print(L)

print("\n-------------------")

# Sorting
M = ['bb', 'aa', 'cc']
M.sort()
print(M)
M.reverse()
print(M)

print("\n-------------------")

# Nesting

M = [[1,2, 3], # Code can span lines if bracketed
    [4, 5, 6],
    [7, 8, 9], [5,6,8,9] # 2 list items on same line works
     ]

print(M)
print(M[1]) # Get row 2
print(M[1][2]) # Get row 2, then get item 3 within the row
print("\n-------------------")

"""This matrix structure works for small-scale tasks, but for more serious use NumPy system. NumPy has been said
to turn Python into the equivalent of a free and more powerful version of the Matlab system"""

# Comprehensions
col = [row[2] for row in M] # Collects the items in clmn []
print(col)
col2 = [r[2] for r in M] # row and 4 are variable name for looping construct with expression => list comprehension
print(col2)

print([r[0] + 1 for r in M]) # incremented each item in col 2

print('-------')
print([row[1] for row in M if row[1] % 2 == 0]) #filters out odd items

diag = [M[i][i] for i in [0,1,2]] # Collect a diagonal from our matrix : M[0][0], M[1][1], and M[2][2]
print(diag)

doubles = [c * 2 for c in 'spam'] # Repats chars in string
print(doubles)

