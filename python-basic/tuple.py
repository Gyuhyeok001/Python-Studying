# 1. tuple
t1 = ()
t2 = (1, 2, 3)
print(t2)

# 2. tuple(delete)
#t3 = (1, 2, 3)
#del t3[0]  # TypeError: 'tuple' object doesn't support item deletion

# 3. tuple(index)
t4 = (1, 2, 3)
print(t4[0])  # 1
print(t4[1])  # 2

# 4. tuple(slicing)
t5 = (1, 2, 3, 4, 5)
print(t5[0:3])  # (1, 2, 3)
print(t5[1:])  # (2, 3, 4, 5)

# 5. tuple(length)
t6 = (1, 2, 3)
print(len(t6))  # 3

# 6. tuple(concat)
t7 = (1, 2, 3)
t8 = (4, 5, 6)
t9 = t7 + t8
print(t9)  # (1, 2, 3, 4, 5, 6)

# 7. tuple(multiply)
t10 = (1, 2, 3)
t11 = t10 * 3
print(t11)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 8. tuple(count)
t12 = (1, 2, 3, 1, 2, 3)
print(t12.count(1))  # 2
print(t12.count(2))  # 2
print(t12.count(3))  # 2

# 9. tuple(index)
t13 = (1, 2, 3, 1, 2, 3)
print(t13.index(1))  # 0
print(t13.index(2))  # 1

