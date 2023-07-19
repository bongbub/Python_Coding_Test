# 일반 재귀 함수로 피보나치 구현

n = int(input('피보나치 n을 입력'))  
# 실행해본 후 n을 30~ 50 정도로 테스트

def Fibonacci(num):
    if num == 0:
        return 0
    elif num == 2 or num == 1:
        return 1
    
    return Fibonacci(num - 2) + Fibonacci(num - 1) 
    #  점화식 표현이 중요함! *********
    
print(Fibonacci(n))