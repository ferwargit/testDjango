x = [0,1,2,3,4,5,6,7,8,9,10]
# [start:stop]
print(x[:])
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(x[2:])
# [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(x[:5])
# [0, 1, 2, 3, 4]
# [start:stop:step]
print(x[::2])
# [0, 2, 4, 6, 8, 10]
print(x[-1])
# 10
print(x[-4:])
# [7, 8, 9, 10]
print(x[:-4])
# [0, 1, 2, 3, 4, 5, 6]

# slice(start:stop:step)
y = slice(1,3)
print(x[y])
# [1, 2]