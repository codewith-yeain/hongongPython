# 숫자의 종류
digits = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
dict = {}
temp = 0

for i in digits:
    dict[i] = dict[i] + 1 if i in dict else "".join(map(str, digits)).count("i")

print("{}에서 사용된 숫자의 종류는 {}개입니다.".format(digits, len(dict)))