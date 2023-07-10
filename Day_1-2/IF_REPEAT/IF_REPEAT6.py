#day 1

#조건문 / 반복문  - ord

c = input("A부터 입력한 문자까지 순서대로 출력 :")
i = ord('a')   #a의 아스키코드 정수 값 65
c = ord(c)
while i<=c:  #a부터 입력한 문자 정수 값 까지
    print(chr(i), end='')  #chr 캐스팅하여 문자 출력, 줄 바꿈 x
    i +=1  #i + 1과 같음, 1씩 증가
    
    
    ->이것도 덜씀 
