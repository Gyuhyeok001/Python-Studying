# variable
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))

# variable(a == b)
a = [1, 2, 3]
a = b
print(id(a))
print(id(b))

# variable(a is b)
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))

# variable(a is b)
a = [1, 2, 3]
b = a
a[0] = 100
print(a)
print(b)

# variable(slicing)
a = [1, 2, 3]
b = a[:]
a[0] = 100
print(a)
print(b)

# variable(copy)
a = [1, 2, 3]
b = a.copy()
print(a)
print(b)

# variable(switch)
a = 1
b = 2
ex = a
a = b
b = ex
print(a)
print(b)

# variable(switch)
a = 1
b = 2
a, b = b, a
print(a)
print(b)