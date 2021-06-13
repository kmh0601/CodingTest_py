# https://www.acmicpc.net/problem/2941

alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

my_string = input()
new_string = ""
count = 0

for i in my_string:
    new_string = new_string + i
    for j in alpha:
        if j in new_string:
            count += 1
            new_string = new_string.replace(j,'')
            count += len(new_string)
            new_string = ""
count += len(new_string)
print(count)