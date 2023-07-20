# 효율적인 화폐 구성

# INF 초기화값 : 10000같이 더이상 표기가 안되는 수 -> 여기선 초기화로 사용됨


#정수 N, M을 입력 받기
n, m = map(int, input().split())

array = []
# n개의 화폐 단위 정보를 입력 받기
for i in range(n):
    array.append(int(input()))
    
# DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 진행 (바텀업)
d[0] = 0
for i in range(n):
    print("인덱스 번호 :", i)
    for j in range(array[i], m + 1):
        # (i-k)원을 만드는 방법이 존재하는 경우
        if d[j - array[i]] != 10001:
            # 디버그용
            print(d[i], d[j] - array[i] + 1)
            d[j] = min(d[j], d[j - array[i]] + 1)
            
# 계산된 결과 출력
# 최종적으로 M원을 만드는 방법이 없는 경우
if d[m] == 10001:
    print(-1)
else:
    print("최종 : ", d[m])