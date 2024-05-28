import argparse
parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='файл с элементами массива')
args = parser.parse_args()


file = open(args.file, "r")

numbers = list(map(int, file.readlines()))

middle = int(sum(numbers)/len(numbers))

res = 0
for num in numbers:
    if num > middle:
        res = res + (num - middle)
    elif num < middle:
        res = res + (middle - num)
print(res)
