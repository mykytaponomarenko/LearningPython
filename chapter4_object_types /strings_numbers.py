#Types of Seqences: strings, lists, tuples 

#Strings (immutable)
spam = 'Spam' 
print(spam)
print('span length is ' + str(len(spam)))

idx = 0
print('spam item #' + str(idx) + ' is ' + spam[idx]) 
idx = 3
print('spam item #' + str(idx) + ' is ' + spam[idx])

print(spam[-1]) # By using Python index backwarding we print last item
print(spam[-2]) # Negative index is added to the string's size so it is same as :
print(spam[len(spam) - 2])

print("\n")

# Concatenation
print(spam + 'xyz')
print(spam * 8)

print("\n")

# Slicing
print(spam[1:3]) # Slice of spam from offsets 1 throgh 2 (not 3)
# In a slice, the left bound defaults to zero, and the right bound defaults to the length of the sequence being sliced
print(spam[1:])
print(spam[0:3])
print(spam[:3])
print(spam[:-1])
print(spam[:])

print("\n")

#String methods
print(spam)
print(spam.find('pa'))
print(spam.find('is_not_there'))
print(spam.replace('pa', 'xyz'))

print("\n")

#Numbers (immutable), math and random
import math
print(math.pi)
print(str(math.sqrt(85)) + "\n")

import random
print(random.random)
print(random.choice([1,2,3,4]))

print("\n")

# More String Methods
line = 'aaa, bbb, cc, d'
test = line.split(',') # split with delimiter into list of substrings
print(test[0])
print(spam.upper())
print(spam.isalpha()) # Content test - characters in a string are alphabetic (letters) or not
print(spam.isdigit())

line = 'aaa, bbb, cc, d\n'
print(line)
line = line.rstrip() # Remove whitespace chars on the rigth
print(line)

print("\n")
# String formatting
option_one = '%s, eggs and %s' % ('text1', 'text2')
print(option_one)
option_two = '{0}, eggs and {1}'.format('text3', 'text4')
print(option_two)
print('%s, %s' % (spam, line))
print('{0}, {1}'.format(spam, line))
