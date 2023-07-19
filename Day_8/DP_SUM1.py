# DP - 수열의 합 연산

n = int(input('더하기 입력 개수 :'))

arr = list(map(int, input().split()))
dp = [0] * len(arr)  # DP 테이블 공간 선언 및 초기화
dp[0] = arr[0]

for i in range(1,len(arr)):
    dp[i] = max(arr[i], dp[i-1] + arr[i])  # 점화식 표현 중요!

print('합 연산 결과 :',max(dp))

# dp문제는 항상 dp 테이블이 필요
# 연산 결과를 dp 테이블에 지속하여 업데이트 함.