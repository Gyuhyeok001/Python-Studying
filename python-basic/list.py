# 1.  list
list=[1,2,3,4]
print(list)

# 2.  list(다음 문장)
list=[1,2,3,4]
print(list[0]) # list[1,2,3,4]
print(list[1]) # list[1,2,3,4]

# 3.  list(list에 list)
list=[1,2,3,['a','b','c']]
print(list[0]) # 1
print(list[3]) # ['a','b','c']
print(list[3][0]) # a
print(list[3][1]) # b

# 4.  list(list slicing)
list=[1,2,3,['a','b','c']]
print(list[0:2]) # [1,2]
print(list[0:3]) # [1,2,3]
print(list[0:4]) # [1,2,3,['a','b','c']]

# 5.  list(list slicing)
list=[1,2,3,['a','b','c']]
print(list[0:3:2]) # [1,2]

# 6.  list(adding list)
a = [1,2,3]
b = [3]
print(a+b) # [1,2,3,3]
print(a*3) # [1,2,3,1,2,3,1,2,3]

# 7.  list(length of list)
a = [1,2,3]
print(len(a)) # 3
print(len(a[0:2])) # 2

# 8.  list(문자+숫자list)
a = [1,2,3]
print(str(a[0]) + "hello") # 1hello

# 9.  list(modify list)
a = [1,2,3]
a[0] = 4
print(a) # [4,2,3]

# 10. list(append list)
a = [1,2,3]
a.append(4)
print(a) # [1,2,3,4]

# 11. list(delete list)
a = [1,2,3]
del a[0]
print(a) # [2,3]

# 12. list(extend list)
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a) # [1,2,3,4,5,6]

# 13. list(sort list)
a = [3,2,1]
a.sort()
print(a) # [1,2,3]

# 14. list(reverse list)
a = [1,2,3]
a.reverse()
print(a) # [3,2,1]

# 15. list(count list)
a = [1,2,3,1]
print(a.count(1)) # 2
print(a.count(2)) # 1
print(a.count(3)) # 1

# 16. list(index list)
a = [1,2,3,1]
print(a.index(1)) # 0
print(a.index(2)) # 1
print(a.index(3)) # 2

# 17. list(insert list)
a = [1,2,3]
a.insert(0,4)
print(a) # [4,1,2,3]

# 18. list(pop list)
a = [1,2,3]
a.pop(1)
print(a) # [1,2]

# 19. list(remove list)
a = [1,2,3]
a.remove(1)
print(a) # [2,3]





