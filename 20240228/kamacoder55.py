# Kamacoder 55 右旋转字符串

n = int(input())
s = input()

print(s[-n:]+s[:len(s)-n])