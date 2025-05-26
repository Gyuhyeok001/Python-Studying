throwingrocks = 0
while throwingrocks < 5:
    throwingrocks = throwingrocks + 1
    print("hit target %d times" % throwingrocks)
    if throwingrocks == 5:
        print("hit target 5 times, stop throwing")
# Output:
# hit target 1 times

throwingrocks = 0
while throwingrocks < 5:
    throwingrocks += 1
    print("hit target %d times" % throwingrocks)
    if throwingrocks == 5:
        print("hit target 5 times, stop throwing")
# Output:
# hit target 1 times

juice = 10
money = 1000
while money:
    print("I got your money")
    juice -= 1
    print("I have %d juice left" % juice)
    if juice == 0:
        print("I have no juice left, stop selling")
        break
# Output:

juice = 10
while True:
    money = int(input("Please give me money: "))
    if money < 0:
        print("Invalid amount, please enter a positive number.")
        continue
    print("I got your money")
    if money == 1000:
        print("No change, I got your money")
        juice -= 1
    elif money > 1000:
        print("I will give you change")
        change = money - 1000
        print("Here is your change: %d" % change)
        juice -= 1
    else:
        print("Give coffee and no change")
        print("I have %d juice left" % juice)
    if juice == 0:
            print("I have no juice left, stop selling")
            break
# Output:
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        print("%d is even" % a)
    else:
        print("%d is odd" % a)






