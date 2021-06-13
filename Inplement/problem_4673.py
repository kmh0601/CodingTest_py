# https://www.acmicpc.net/problem/4673

def d(n):
    result = n
    n = list(str(n))

    for i in n:
        result += int(i)

    return result

target = list(range(1,10001))
for i in range(1,10001):
    try:
        target.remove(d(i))
    except:
        continue
for i in target:
    print(i)