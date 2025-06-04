#Exception handling structure
#Try: sentence that may cause an error
#Except: code that runs if an error occurs
#els
#Finally: code that runs no matter what

# 1. try and except
try:
    print(10 / 0)   
except ZeroDivisionError:
    print("You can't divide by zero!")

# 2. may error
try:
    a = [1, 2, 3]
    print(a[5])
    4/0
except ZeroDivisionError:
    print("You can't divide by zero!")
except IndexError:
    print("Index out of range!")

# 3. else
try:
    a = 10/2
    print(a)

except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    a >= 0
    print("Division successful!")

# 4. error_pass.py
try:
    f = open("없는파일", 'r')
except FileNotFoundError:
    pass

print("안녕")

# 5. make error
class Myerror(Exception):
    def __str__(self):
         return "not acceptable nickname"

def say_nick(nick):
    if nick == 'handsome':
        raise Myerror()
    print(nick)

try:
    say_nick("handsome")
    say_nick("cool")
except Myerror as e:
    print(e)






