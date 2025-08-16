s = input()
num = s.split("+")
nums = sorted(map(int, num))
print('+'.join(map(str, nums)))

