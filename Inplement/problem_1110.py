# https://www.acmicpc.net/problem/1110
number = list(input())
if len(number) == 1:
    number.insert(0,'0')

cnt = 0
target = int(number[0])*10 + int(number[1]) # 목표값
new = target  #새로운 수

while True:
    ttemp = new # 결과값을 다시 시작값으로
    temp = ttemp//10 + ttemp%10 # 중간값
    new = (ttemp%10)*10 + temp%10 # 결과값
    cnt += 1
    if(new == target):
        break
print(cnt)