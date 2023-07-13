#Day 1

a,b = map(int, input('정수 2개를 입력 받아 차를 계산 :').split())  #map이라는 함수를 활용해 정수를 입력 받음
print(a-b)

a,b=input('정수 2개를 입력받아 차를 계산 :').split()  #직접 정수 캐스팅
c=int(a)-int(b)
d=int(a)*int(b)
e=int(a)//int(b)   #나누기
f=int(a)%int(b)    #나머지
print("차, 곱, 몫, 나머지 연산 결과 :", c, d, e, f)

a,b = input("단어 여러번 출력 :").split()
print(a*int(b))

s= int(input("문자 반복 횟수 입력 :"))
s2 = input('문자열 직접 입력 :')
print(s*s2)   #문장 반복