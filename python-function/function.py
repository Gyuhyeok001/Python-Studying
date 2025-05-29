#function 1
def add(a,b):
    return a + b
print(add(1,2))

#function 2
def say():
    return"hi"
print(say())

#function 3
def add(a,b):
    print("the sum of %d,%d is %d" % (a,b,a+b))
a = add(1,2)
print(a)

#function 4
def add(a,b):
    return a + b
result = add(a=4,b=5) # result is input
print(result)

#function 5
def add_many(*args):
    A = 0
    for i in args:
            A += i
    return(A)
print(add_many(1,2,3,4,5))

#function 6
def several__functions(choice,*args):
    if choice == "add":
        a = 0
        for i in args:
            a += i
    elif choice == "multiply":
        a = 1
        for i in args:
            a *= i
    return a
print(several__functions("multiply",1,2,3))

#function 7 - only one return statement
def add_mul(a, b):
    return a + b, a * b
A,B = add_mul(2, 3)
print(A)
print(B)  # Output will be a tuple (5, 6)

#function 8 - retun escaping
def say_nick(name):
    if name == "james":
        return
    print("I am %s." % name)
say_nick("jolly")  # This will print "I am jolly."
say_nick("james")  # This will not print anything because of the return statement

#function 9 - return with multiple values
def introduce_myself(name, age, man=True):
    print("My name is %s and I am %d years old." % (name, age))
    if man:
        print("I am man.")
    else:
        print("I am woman.")
introduce_myself("james", 20, True)

#function 10 - vartest
a = 2
def vartest(a):
    a += 1
vartest(a)
print(a)  # This will print the incremented value of a

#function 11 - vatest return 1
a = 2
def vartest(a):
    a += 1
    return a
a = vartest(a)
print(a)  # This will print the incremented value of a

#function 12 - vartest return 2
a = 2
def vartest(b):
    b = a + 1
    return b
vartest(b=a)
print(a)# This will print the original value of a, which is 2

#function 13 - vartest global
a = 1
def vartest():
    global a # 밖에 있는 a를 가져온다.
    a += 1
vartest()
print(a)  # This will print the incremented value of a, which is now 2

#function 14 - vartest mutable
a = [1, 2, 3]
def vartest(a):
    a = a.append(4)  # This will not change the original list
vartest(a)
print(a)  # This will print the original list [1, 2, 3]

#function 15 - lambda function
def asdf(a, b):
    return a + b
a = lambda a, b: a + b  # This is a lambda function that adds two numbers
print(asdf(1, 2))  # This will print 3
# This is a simple lambda function that adds two numbers

# function 16 - lambda function with list
a  = [lambda x: x + 1, lambda x: x * 2]
print(a[0](1))  # This will print 2
print(a[1](2))  # This will print 4