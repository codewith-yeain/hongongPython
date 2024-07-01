# 2번

# 숫자는 무작위로 입력해도 상관없습니다.
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

# 나의 풀이
# num = 0
# for key in key_list:
#     character[key] = value_list[num]
#     num += 1

# 답지
for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]

print(character)

#-----------------------------------------------------
# 3번

limit = 10000
i = 1
sum_value = 0

# sum은 파이썬 내부에서 사용하는 식별자이므로 sum_value라는 변수 이름을 사용합니다.
while sum_value <= limit:
    sum_value += i
    i += 1


print("{}을(를) 더할 때 {}을(를) 넘으며 그떄의 값은 {}입니다.".format(i-1, limit, sum_value))