n, m = map(int, input().split())
arr = []
j = 1
for i in range(n*m):
    arr.append(j)
    j += 1
    if j > n:
        j = 1
myit = iter(arr)
j = next(myit)
count = 1
result = "1"
while True:
    count += 1
    num = next(myit)
    if num == 1 and count % m == 0:
        break
    elif count == m and num != 1:
        count = 1
        result += str(num)
print(result)
