# 1. word format(number)
a = "I eat %d apples." % 3
print(a) # I eat 3 apples.

# 2. word format(string)
a = "I eat %s apples." % "five"
print(a) # I eat five apples.

# 3. word format(float)
a = "I eat %f apples." % 3.14
print(a) # I eat 3.140000 apples.

# 4. word format(소수점)
a = "I eat %10.4f apples." % 3.1432425
print(a) # I eat 3.14 apples.

# 5. word format(문자열 2개)
a = "I eat %s apples and %s oranges." % ("five", "ten")
print(a) # I eat five apples and ten oranges.  

# 7. word format(문자열 random)
a = "He is %s years old and my name is %s." % (22, "Lee")
print(a) #  He is 22 years old and my name is

# 8. word format(문자열 바로 대입)
a = "I eat {0} apples.".format(3)
print(a) # I eat 3 apples.

# 9. word format(문자열 바로 대입)
a = "I eat {0} apples.".format("five")
print(a) # I eat five apples.

# 10. word format(문자열 바로 대입)
a = "I eat {0} apples.".format(3.14)
print(a) # I eat 3.14 apples.

# 11. word format(문자열 바로 2개 대입)
a = "I eat {0} apples and {1} oranges.".format("five", "ten")
print(a) # I eat five apples and ten oranges.

# 12. word format(문자열 practice)
a = "I love palying {0} and {1} with friends." .format("basketball", "swimming")
print(a) # I love palying basketball and swimming with friends.

# 12. word format(문자열 practice2)
number = 3
sports1 = "basketball"
sports2 = "swimming"
a = "I love palying {0} and {1} with {2}\tfriends." .format(sports1, sports2, number)
print(a) # I love palying basketball and swimming with friends.

# 13. word format(문자열 practice3)
sports1 = "basketball"
sports2 = "swimming"
a = "I love palying {0} and {1} with {number}\tfriends." .format(sports1, sports2, number=5)
print(a) # I love palying basketball and swimming with friends.

# 14. word format(문자열 정렬)
a = "I eat {0:<10} apples.".format(3)
print(a) # I eat 3         apples.
a = "I eat {0:>10} apples.".format(3)
print(a) # I eat         3 apples.
a = "I eat {0:^10} apples.".format(3)
print(a) # I eat    3     apples.
a = "I eat {0:=^10} apples.".format(3)
print(a) # I eat ===3==== apples.
a = "I eat {0:!^10} apples.".format(3)
print(a) # I eat !!!3!!!! apples.

# 15. word format(문자열 표현)
a = 1.23456 
print ("{0:10.2f}" .format(a)) 

# 16. word format(문자열 표현)
print("{{ and }}".format())

# 17. word format(문자열 f 표현)
name = "Lee"
age = 22
a = f"Hello, my name is {name} and I am {age} years old."
print(a) # Hello, my name is Lee and I am 22 years old.

# 18. word format(문자열 세기)
a = "apple"
print(a.count("a")) # 1
print(a.count("p")) # 2

# 19. word format(문자열 위치)
a = "apple"
print(a.find("a")) # 0
print(a.find("p")) # 1
print(a.find("e")) # 4

# 20. word format(문자열 위치)
a = "apple"
print(a.index("a")) # 0
print(a.index("p")) # 1

# 21. word format(문자열 삽입)
a = "apple"
print(",".join(a)) # a,p,p,l,e

# 22. word format(문자열 대문자)
a = "apple"
print(a.upper()) # APPLE
print(a.lower()) # apple   
print(a.capitalize()) # Apple

# 23. word format(문자열 공백지우기)
a = "   apple   "
print(a.strip()) # apple
print(a.lstrip()) # apple
print(a.rstrip()) # apple

# 24. word format(문자열 바꾸기)
a = "my life is over"
print(a.replace("my", "your")) # your life is over

# 25. word format(문자열 나누기)
a = "my life is over"
print(a.split()) # ['my', 'life', 'is', 'over']
print(a.split(" ")) # ['my', 'life', 'is', 'over']
print(a.split("l")) # ['my ', 'ife is over']git reset HEAD~1
