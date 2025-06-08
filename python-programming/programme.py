## Think about input and output to figure out the guidline.

# 1. gugudan 
def gugu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i += 1
    return result
print(gugu(2))
print(gugu(3))

# 2. 3 and 5 multiply
result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
    print(result)

# 3. page number
def PageNumber(m,n):
    if m % n == 0:
        return m//n
    else:
        return m//n + 1
print (PageNumber(3,10))

