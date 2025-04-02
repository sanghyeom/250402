1
i = 'x'

zoo = ('python','elephant','penguin')

print(zoo)
print(zoo[2])
#indexError:tuple index out of range
# print(zoo[3])

#TypeError: tuple indices must be integers or slices, not str
#print(zoo['c'])

#TypeError: tuple indices must be integers or slices, not str
#print(zoo[i])

#TypeError: 'tuple' object does not support item assignment 
#zoo[0] = 'lion'
sigleton = ('lion', )

print(type(sigleton))

# 패킹, 언패킹

numbers = 1, 2, 3
print(numbers)

i1 = numbers[0]
i2 = numbers[1]
i3 = numbers[2]

#갯수가맞으면 매칭됨

#ValueError: not enough values to unpack (expected 4, got 3
i1, i2, i3 = numbers