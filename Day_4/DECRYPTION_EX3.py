# day 4

# 문제
# 홍길동은 비밀 문서를 가지고 다닌다. 소문자 모음 ('a', 'e', 'i', 'o', 'u')의 다음에 'g'를 한 개 쓰고
# 그 모음을 하나 더 쓰는 형태로 문서를 암호화 한다. 암호문을 실제 원본 문장으로 바꾸는 프로그램을 작성하시오
# 입력 예 : hegellogo nigicege dagay -> hello nice day

string = input("암호문을 입력하세요 :")
aou = ['a', 'e', 'i', 'o', 'u']  # 모음 리스트
result = "" # 결과 값을 넣을 빈 문자열

i = 0
while i < len(string):   # 문자 수 만큼 반복
    result += string[i]
    if string[i] in aou:
        i += 3
    else:
        i += 1
        
print (result)