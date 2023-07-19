# 문제
# 정수 X가 주어졌을 때, 아래와 같은 연산 4가지를 적절히 사용해서
# 1을 만드려고 한다. 연산을 사용하는 횟수의 최솟값 출력하기
# 연산 종류 : 5,3,2 나누기, -1 마이너스
# 참고 : 입력 x는 1 <= 30000 이하의 정수이다.


x = int(input())  # 정수 x를 입력받기


#입력받은 수 만큼 DP 테이블 초기화 및 크기지정
# d = [0] * (x+1)  -> 내가 짠 코드
d =[0] * 30001  # -> 교수님 코등..ㅎ 참고사항 확인하기

# 다이나믹 프로그래밍(DP) 진행 (바텀업)

for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1

    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
        
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
        
print(d[x])
    