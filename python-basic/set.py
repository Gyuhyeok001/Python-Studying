# set
s1 = set([1, 2, 3, 4, 5])
print(type(s1))

s1 = {1, 2, 3, 4, 5}
print(s1)

s1 = {"nice"}
print(s1)

# set with list
s1 = set([1, 2, 3, 4, 5])
l1 = list(s1)
print(l1)

# set with tuple
s1 = set((1, 2, 3, 4, 5))
t1 = tuple(s1)
print(t1)

# set (교집합)
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = s1 & s2
print(s3)

# set (합집합)
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = s1 | s2
print(s3)

# set (차집합)
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = s1 - s2
print(s3)

# set (add) // one by one adding
s1 = {1, 2, 3, 4, 5}
s1.add(6)
print(s1)

# set (remove)
s1 = {1, 2, 3, 4, 5}
s1.remove(3)
print(s1)

# set (update) // several adding
s1 = {1, 2, 3, 4, 5}
s2 = {6, 7, 8}
s1.update(s2)
print(s1)

# set (discard) // remove without error
s1 = {1, 2, 3, 4, 5}
s1.discard(3)
print(s1)

# set (list중복제거)
l1 = [1, 2, 3, 4, 5, 1, 2, 3]
l1 = set(l1)
print(l1)


