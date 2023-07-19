# DP 메모제이션 기법으로 피보나치 구현

import sys

# n = int(sys.stdin.readline()) 더 빠른 입력 방식
N = int(input("피보나치 n을 입력 :"))  # 실행 해 본 후 n을 30 ~ 50 정도로 테스트


arr = [0 for _ in range(N+1)]   # 임시 공간 리스트 생성 및 초기화
arr[1] = 1   # 0, 1로 시작

# 피보나치 2부터 유효
for i in range(2, N+1):
    arr[i] = arr[i-1] + arr[i-2]  # 바로 값을 가져옴

    
    
# 연산 결과를 앞에 선언한 임시공간에서 가져옴
# 반복 하면서 이미 누적된 합을 리스트에 적어놓고 최종 결과만 가져옴
    
    
print(arr[-1])