# 1. class - calculator
result = 0
def add(number):
    global result
    result += number
    return result

def subtract(number):
    global result
    result -= number
    return result

def multiply(number):
    global result
    result *= number
    return result

print(add(10))        # Output: 10
print(add(5))         # Output: 15
print(subtract(5))   # Output: 10
print(multiply(2))   # Output: 20

# 2. class - calculator with two values (so inefficient to use as a calculator)
result1 = 0
result2 = 0
def add1(number):
    global result1
    result1 += number
    return result1

def add2(number):
    global result2
    result2 += number
    return result2

print(add1(10))        # Output: 10
print(add1(5))         # Output: 15
print(add2(20))        # Output: 20
print(add2(10))        # Output: 30

# 3. class - calculator with class
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, number):
        self.result += number
        return self.result

    def subtract(self, number):
        self.result -= number
        return self.result

    def multiply(self, number):
        self.result *= number
        return self.result

#클래스 정의 바깥에서 객체 생성
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(10))        # Output: 10
print(cal1.add(5))         # Output: 15
print(cal2.add(20))        # Output: 20
print(cal2.add(10))        # Output: 30

# 4. class basic
class man:
    pass

james = man()
mike = man()

# 5. class with four functions calculator
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    def subtract(self):
        result = self.first - self.second
        return result
    def multiply(self):
        result = self.first * self.second
        return result
    def divide(self):
        result = self.first / self.second
        return result

a = FourCal()
a.setdata(4, 2)
print(a.first)
print(a.second)
print(a.add())
print(a.subtract())
print(a.multiply())
print(a.divide())

b = FourCal()
b.setdata(10, 5)
print(b.first)
print(b.second)
print(b.add())
print(b.subtract())
print(b.multiply())
print(b.divide())

# 6. class with four functions calculator with constructor
class FourCal2:
    def __init__(self, first, second): #constructor
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    def subtract(self):
        result = self.first - self.second
        return result
    def multiply(self):
        result = self.first * self.second
        return result
    def divide(self):
        result = self.first / self.second
        return result
    
a = FourCal2(4, 2)
print(a.first)
print(a.second)

# 7. class with four functions calculator with constructor and inheritance
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    def subtract(self):
        result = self.first - self.second
        return result
    def multiply(self):
        result = self.first * self.second
        return result
    def divide(self):
        result = self.first / self.second
        return result
    
class HighFourCal(FourCal):
    def power(self):
        result = self.first ** self.second
        return result
    
class LowFourCal(FourCal):
    def divide(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
    
a = LowFourCal(4, 0)

print(a.divide())  # Output: 0