import argparse
parser = argparse.ArgumentParser()
parser.add_argument('n', type=int, help='Количество чисел в массиве')
parser.add_argument('m', type=int, help='Движение интервала m')
args = parser.parse_args()

arr = []
j = 1
for i in range(args.n * args.m):
    arr.append(j)
    j += 1
    if j > args.n:
        j = 1
myit = iter(arr)
j = next(myit)
count = 1
result = "1"
while True:
    count += 1
    num = next(myit)
    if num == 1 and count % args.m == 0:
        break
    elif count == args.m and num != 1:
        count = 1
        result += str(num)
print(result)


