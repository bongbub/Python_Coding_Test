# 피보나치 수열 DP(다이나믹 프로그래밍으로 시간 단축하기)

# 피보나치 함수를 재귀함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(90))
# 단순 재귀함수 구현 -> 지속시간 복잡도 (10억이상..등 큰 수 )
# 100만 넣어도 시간이 엄청 소요됨
print("end")