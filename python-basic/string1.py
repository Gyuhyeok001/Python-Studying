# 1. word
a = "Life is too short"
print(a) # Life is too short
print(type(a)) # <class 'str'>

# 2. word(다음 문장)
a = "Life is too short \n you need python"
print(a) # Life is too short    

# 3. word(같은 문장 점프)
a = "Life is too short \t you need python"
print(a) # Life is too short    

# 4. word(multi line string)
a = """
Life is too short
you need python
""" 
print(a) # Life is too short

# 5. word(문자열 연산)
a = "Life is too short"
b = "you need python"
print(a + b) # Life is too shortyou need python
print(a * 2) # Life is too shortLife is too short  
print(a[0]) # L (첫단어가 항상 0)
print(a[1]) # i
print(a[2]) # f
print(a[3]) # e
print(a[-4]) #

# 6. word(문자열 길이)
a = "Life is too short"
print(len(a)) # 17

# 7. word(문자열 슬라이싱)
a = "Life is too short"
print(a[0:4]) # Life
print(a[0:5]) # Life
print(a[0:6]) # Life i
print(a[0:7]) # Life is

# 8. word(문자열 슬라이싱)
a = "Life is too short"
print(a[:2]) # Life
print(a[::2]) # Life

# 9. word(문자열 슬라이싱 나누기)
a = "20010331Rainy"
print(a[:8]) # 20010331
print(a[8:]) # Rainy
print(a[8:12]) # Rainy

# 10. word(pithon 고치기)
a = "pithon"
print(a[0:1] + "y" + a[2:]) # python
