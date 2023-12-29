sum = 0
count = 0

for i in range(10):
    num = int(input())
    if num >= 0 and num <= 200:
        sum = sum + num
        count = count +1

print(sum, round(sum/count, 1))