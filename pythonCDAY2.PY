# L = [1,3,4,5, 'epita']

# # L.append(10.)

# del L[3]
# # print(L)

# L = [1,3,4,5, 'epita']

# L.extend(["epita"])
# # print(L)
# L = [1,3,4,5, 'epita']

# L.extend([0,1])
# print(L)

# l = [1, 3, 4, 5, 'epita', 0, 1]

# l[-1]
# l = [1, 3, 4, 5, 'epita', 0, 1]
def add_one(x):
    res = x + 1
    return res
x_old = 2
x_new = add_one(x_old)
print(x_new)
