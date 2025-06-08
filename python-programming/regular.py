import re

data =  """
lee = 20030320-1034321
park = 20040219-1002342
"""

pattern = re.compile("(\d{6})[-]\d{7}")
print(pattern.sub("\g<1>-*******",data))

## match() = 문자열 처음부터 매치하는지 조사
## search() =  문자열 전체를 조사 앞뒤상관없이
## findall() = 정규식과 매치되는 모든 문자열을 리스트로 돌려준다
## finditer() = 정규식과 매치되는 모든 문자열을 반복계체로 돌려준다

# match object
import re
p = re.compile('[a-z]+')
m = p.search("4 python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())