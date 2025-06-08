# UTF encoding
a = "life is too short"
b = a.encode('utf-8')

print(a.encode('utf-8'))

# EUC encoding
a = "한글"
print (a.encode('euc-kr'))

# EUC decoding // Using same fuction of encoding for the decoding
a = "한글"
b = a.encode('euc-kr')
print(b.decode('euc-kr'))

## source coding express on the top page // ex) _*_ coding: euc-kr _*_

# closer // 함수 안에 함수를 넣는 것을 말함
def mul(m):
    def wrap(n):
        return m*n
    return wrap
if __name__ == "__main__":
    mul3 = mul(3)
    mul5 = mul(5)

    print(mul3(10))
    print(mul5(10))

# decorator // 기존함수의 기능을 바꾸지 않고 추가 할수있는 형태
import time

def elapsed(origin_func):
    def wrapper():
        start = time.time()
        result = origin_func()
        end = time.time()
        print ("activating time: %f sec" % (end - start))
        return result
    return wrapper

@elapsed
def myfunc():
    print("activation starts")

myfunc()

# iterator
q = [1, 2, 3]
iq = iter(q)
for i in iq:
    print(q)

for i in iq:
    print(i)

## __iter__ 와 __next__ 는 함께 써야한다.

# generator
generator = (i*i for i in range (1,1000))

print(next(generator))
print(next(generator))
print(next(generator))

