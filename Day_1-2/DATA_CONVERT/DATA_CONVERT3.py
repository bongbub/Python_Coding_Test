#day 1

#소수점 자리 계산
f = float(input('소수점 5자리 이하 입력 -> 소수점 2자리 입력해주겠음 :'))
print(round(f,2))    #round -> 반올림 함수(중간값(0.5)는 반올림되지 않음 주의)

a = input('소수를 5자리 이하로 입력 ')
a = float(a)   #입력값을 소수로 캐스팅
print(format(a,"2f"))   #format 함수 소수점 2자리 출력

a,b = map(float, input("소수 5자리 이하 2개 입력 :").split())   #실수 2개 받음
c = a/b
print("%0.3f" %c)    #소수점 3번째 자리 출력

a, b, c = input('정수를 3개 입력 : ').split() # 정수 3개 입력 받음
a = int(a)
b = int(b)
c = int(c)
total = a+b+c # 변수에 합 저장
avg = total/3 # 변수에 평균 저장
print(total, format(avg, ".2f")) # 합산 결과와 평균(소수점 2자리) 출력

