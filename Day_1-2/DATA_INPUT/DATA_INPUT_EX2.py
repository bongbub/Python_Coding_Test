#Day 1

#문제 : 주민등록번호 문자열을 입력 받아 숫자만 출력하시오
#변수 s로 입력저장, -으로 구분, 공백으로 병합 ex) 891911-131511  891911131511

s = input("주민등록번호를 입력하시오 :").split('-')   #split을 -로 구분
print(''.join(s))    #join을 사용해서 공백으로 이어 붙임



#한 줄로 써진 교수님 코드
#print(''.join(input('주민등록번호를 입력하세요, -로 구분 :').split('-')))