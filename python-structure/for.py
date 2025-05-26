testlist = [1, 2, 3, 4, 5]
for i in testlist:
    print(i)
# for with range

a = [(1, 2), (3, 4), (5, 6)]
for (first, second) in a:
    print(first + second)
# for with range

number = 0
scores = [99 , 88, 77, 66, 55]
for score in scores:
    number += 1
    if score >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)
# for with range

number = 0
scores = [99 , 88, 77, 66, 55]
for score in scores:
    number += 1
    if score < 60:
        continue
    print("%d번 학생은 합격입니다." %number)

for i in range(2, 10):
    for j in range(1, 10):
        print("%d * %d = %d" %(i, j, i * j))
    print()
      