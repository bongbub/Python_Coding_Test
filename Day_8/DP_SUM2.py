# DP - 삼각형의 합

# 탑다운 메모제이션 방식 DP 삼각형 구현
n = int(input("삼각형 깊이 n 입력 :")) # 삼각형 깊이 n 입력
t_list = [] # DP 테이블 생성

for _ in range(n):
    # 삼각형 정보 입력
    t_list.append(list(map(int, input().split()))) 

for i in range(1,n):
    for j in range(i + 1):
        if j == 0:
            t_list[i][j] = t_list[i][j] + t_list[i-1][j]
        elif i == j:
            t_list[i][j] = t_list[i][j] + t_list[i-1][j-1]
        else:
            # 최대 삼각형 정보를 업데이트 하는 점화식
            t_list[i][j] = max(t_list[i][j] + t_list[i-1][j],
                              t_list[i][j]+t_list[i-1][j-1])
            
print(max(t_list[n-1]))