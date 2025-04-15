def add_one(x):
    """this function increments by 1 the variable x"""
    x = x + 1
    return x

x_old = 2 
x_new = add_one(x_old)
print(x_new)