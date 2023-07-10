#Day 1


date=input('문자를 입력해주세요, 닷으로 구분 : ').split('.')  #문자 1개 입력, .기준 분리, 입력에 메세지 삽입
print("내가 삽입한 문자:",date)
print("다시로 구분 :",'-'.join(date))   #문자를 -로 연결 출력
date.reverse()   #구분된 문자열 역 뒤집기(정렬x)
print("역출력 :",':'.join(date))   #문자를 :로 연결출력
print(date[0], date[1])  #구분된 문자의 내부 인덱스 번호로 출력