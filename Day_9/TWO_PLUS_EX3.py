# 투 포인터 도전문제 - 수 더하기
# N개의 수로 된 수열 A[1], A[2], ... A[N]이 있다
# 이 수열의 i번째 수 부터 j번째 수 까지의 합이 M이되는
# 경우의 수를 구하는 프로그램 작성
# 참고 : M = A[i] + A[i+1] + ... + A[j-1] + A[j]
# 참고 : 입력 N은 1<=N<=10000, 합 M은 1<=M<=300000000


# 수열의 개수와 i부터 j까지의 합 M 입력 받기
N, M = list(map(int, input("데이터의 개수 입력 :").split()))
# 수열 입력받기
data = list(map(int, input('수열 입력: ').split()))


# 경우의 수 count
count = 0
# start 와 end의 합 넣을 변수
interval_sum = 0
#end..?
end = 0

# start가 N까지 반복
for start in range(N):
    
    print("시작 :", start)
    
    # interval_sum이 M보다 작으면서 end가 N보다 작을 때 까지 반복 -> end를 가능한 만큼 이동시키기
    while interval_sum < M and end < N:
        # interval_sum 에 data의 마지막 더하깅?
        interval_sum += data[end]
        
        print("끝 :", end)
        
        # end 에 1 더함
        end += 1
        
    # 만약 interval_sum, 즉 부분합이 M과 같아졌다면
    if interval_sum == M:
        print("중간 카운트 보기 : ", count)
        # count 1회 추가
        count += 1
    #interval_sum 에 data(수열)의 start부분으로 뺄셈
    interval_sum -= data[start]
    
# count 출력
print(count)