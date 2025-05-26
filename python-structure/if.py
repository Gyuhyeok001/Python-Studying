money = True
if money:
    print("I have money")
else:
    print("I don't have money")
# if-else statement with a condition

money = False
if money:
    print("I have money")
else:
    print("I don't have money")
# if-else statement with a condition

money = True
if money:
    print("I have money")
    print("I will buy a car")
    print("I will buy a house")
# if statement without else, but with a condition

jake = 20
mike = 18
if jake > mike:
    print("Jake is older than Mike")
if jake < mike:
    print("Jake is younger than Mike")
if jake == mike:
    print("Jake and Mike are the same age")
# if statements with multiple conditions

money = 1000
if money > 500:
    print("I have enough money to buy a car")   
else:
    print("I don't have enough money to buy a car")
# if-else statement with a condition and an else clause

money = 3000
card = True
if money >= 3000 and card:
    print("I can buy a car")
else:
    print("I cannot buy a car")
# if-else statement with multiple conditions using 'and'

money = 2000
card = False
if money > 3000 or card:
    print("I can buy a car")
else:
    print("I cannot buy a car")
# if-else statement with multiple conditions using 'or'

print(1 not in [1, 2, 3])
# if-else statement with 'not in' condition
print(4 not in (1, 2, 3))
# if-else statement with 'not in' condition

menu = ["pizza", "hamburger", "hotdog"]
if "pizza" in menu:
    print("I will have some pizza for dinner")
else:
    print("I will have something else for dinner")
# if-else statement with a condition checking membership in a list

menu = ["pizza", "hamburger", "hotdog"]
if "pizza" in menu:
    pass
else:
    print("I will have something else for dinner")
# if statement with 'pass' for no action when condition is met

menu = ["pizza", "hamburger", "hotdog"]
if "pizza" in menu: pass
else: print("I will have something else for dinner")
# if statement with 'pass' for no action when condition is met, using single-line syntax

bag =["paper", "pen", "eraser"]
pen = True
if "pencil" in bag:
    print("I will study")
else:
    if "pen" in bag:
        print("I will study mmore with pen")
    else:
        print("I will go back home")
# nested if-else statements for checking multiple conditions

bag =["paper", "pen", "eraser"]
pen = True
if "pencil" in bag:
    print("I will study")
elif "pen" in bag:
    print("I will study mmore with pen")
else:
    print("I will go back home")
# nested if-else statements for checking multiple conditions

