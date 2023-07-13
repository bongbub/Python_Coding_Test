# day 4

# 문자열과 숫자들을 받아서 문자열은 오름차순으로, 숫자들은 합쳐서 더해버리기

string = input('문자와 숫자를 입력하시오 :')

# 문자열이 정렬될 리스트
result = []
# 숫자들이 합
value = 0


# 문자열 검사
for i in string:
    if i.isalpha():   # 문자열이 한글을 포함한 알파벳인 경우
        result.append(i)  # result에 삽입
    elif i.isdigit:   #숫자인지 판별
        value += int(i)
        
        result.sort()   # 오름차순 정렬
        
if value != 0:      # 숫자가 하나라도 존재하는 경우 result 뒤에 문자열로 삽입
    result.append(str(value))
    print(''.join(result))   # 최종 결과 출력 
