'''age1, age2, age3 = input('enter 3 values separated with comma: ').split(',')
print(age1 , age2, age3)


# calculate avg number from one input

numbers = input('your numbers:').split()

sum = 0
for n in numbers:
    sum += int(n)

avg = sum / len(numbers)
print(avg)
'''

# print values shifted
#  
a, b, c = 12.34, 234.39, 444.34

print(f'a = {a:>15}')
print(f'b = {b:>25}')
print(f'c = {c:>35}')