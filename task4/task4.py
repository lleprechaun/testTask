file = input()
file = open(file, "r")

numbers = list(map(int, file.readlines()))

middle = int(sum(numbers)/len(numbers))

res = 0
for num in numbers:
    if num > middle:
        res = res + (num - middle)
    elif num < middle:
        res = res + (middle - num)
print(res)
