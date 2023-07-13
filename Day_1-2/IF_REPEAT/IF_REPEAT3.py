# DAY1 - 조건문, 반복문

n = int(input('정수 1개 입력 받아 분류하기 :'))
if n < 0 :
    if n % 2 == 0 :
        print('음수, 짝수 :A')
    else:
        print('음수, 홀수 :B')
else:
    if n % 2 == 0:
        print('양수, 짝수 :C')
    else:
        print('양수, 홀수 :D')
        
if a>=90:
    print("A학점") 
elif a>=70: # elif는 else if의 약어, 들여쓰기 없어 가독성 굿
    print("B학점")
elif a>=40:
    print("C학점")
else:
    print("D학점")

