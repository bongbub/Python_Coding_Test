# 큰 소수 문자열 도전문제
# 숫자로 이루어진 문자열이 주어지고 부분 문자열 중 
# 가장 큰 소수를 찾는 프로그램 작성하기
# 2<=100000 이하 범위 소수만 소수로 취급
# 입력은 여러개의 테스트 케이스로 이루어지며 1000개 이하
# 각 테스트는 길이 255 이하 문자열로 구성, 마지막 줄 0 입력할 시 종료

import math

# 소수 판별 함수 (2 이상의 자연수에 대해)
def is_prime_number(n):
    li = [1] * (n + 1)
    # 에라토스테네스의 체 적용
    for i in range(2, int(math.sqrt(n)) + 1):
        if li[i]:
            for j in range(i + i, n + 1, i):
                li[j] = 0
    # 소수를 함수 안에서 지정
    p = [i for i in range(2, n + 1) if li[i]]
    # 소수를 리턴
    return p

while 1:
    s = input()
    max_string = []
    
    
    # 0이면 종료
    if s == '0':
        break
    # 10만 범위 정수 입력
    p = is_prime_number(100000)
    res = 2
    
    for n in p:
        # 문자 안에 소수가 존재하면
        if str(n) in s:
            res = n
            max_string.append(res)
            
        # 리스트 내부 소수 확인
        print(max_string)
        # 리스트 중 가장 큰 소수값 출력
        print(max(max_string))