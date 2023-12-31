# 소수찾기 - 제일 빠른 방법 (SQRT)

# 에라토스테네스의 체 적용
import math

n = 1000 # 2부터 1000까지 모든 수에 대해 소수 판별

# 처음엔 모두가 소수(True)인 것으로 초기화(0,1제외)
array = [True for i in range(n + 1)]

# 에라토스테네스의 체 알고리즘 수행
# 2부터 n의 제곱근까지의 모든 수를 확인하며
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True: # i가 소수인경우(남은수인경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n+1):
    if array[i]:
               print(i ,end = '')