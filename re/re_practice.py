# regular expression
import re

# 네 자리 중 세 개만 기억이 남
# ca?e -> cafe, cake, cave 등으로 나타날 수 있음

# p = pattern
p = re.compile("ca.e")
# . : 하나의 문자 의미 > care, cafe, case (O) | caffe (X)
# ^ : 문자열의 시작 > desk, destination (O) | fade (X)
# $ : 문자열의 끝 > case, base (O) | face (X)

def print_match(m):
    if m:
        print("m.group():", m.group())  # 일치하는 문자열 반환
        print("m.string:", m.string)    # 입력받은 문자열
        print("m.start()", m.start())   # 일치하는 문자열의 시작 인덱스
        print("m.end()", m.end())   # 일치하는 문자열의 끝 인덱스
        print("m.span()", m.span()) # 일치하는 문자열의 시작 / 끝 인덱스
    else:
        print("매칭되지 않음")
        # 매치되지 않으면 에러 발생


# m = p.match("careless") # match: 주어진 문자열의 "처음부터" 일치하는지 확인
# print_match(m)

# m = p.search("good care") # search: 주어진 문자열 "중"에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("good care careless cafe") # findall: 일치하는 모든 것을 리스트 형태로 반환
# print(lst)

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열")
# 3. m = p.search("비교할 문자열")
# 4. lst = p.findall("비교할 문자열")