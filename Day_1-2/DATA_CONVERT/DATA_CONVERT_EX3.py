# day 1

#문제
#정수 3개를 입력 받아 합과 평균을 출력하시오 
#map(int, input().split())활용, 또는 정수 3개 캐스팅

a, b, c = map(int,input("합과 평균을 도출할 정수 3개를 입력하시오 :").split())

m = a+b+c
t = m/3
print("합 :", m)
print("평균 : ", round(t,2))