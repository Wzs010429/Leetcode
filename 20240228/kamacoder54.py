# Kamacoder 54 替换数字

string = input()
res = ""

for i in string:
    if ord("0") <= ord(i) <= ord("9"):
        res += "number"
    else:
        res += i

print(res)