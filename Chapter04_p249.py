# 4번

max_value = 0
a = 0
b = 0

# 나의 풀이
# for i in range(1, 51):
#     j = 100 - i

#     # 최댓값 구하기
#     max_value = i * j
#     a= i
#     b = j
#     if ((i+1) * (99 -i) > max_value):
#         max_value = (i+1) * (99-i)
#         a = i+1
#         b = 99-i


# 답지
for i in range(1, 100//2 + 1):
    j = 100 - i

    # 최댓값 구하기
    current = i * j
    if max_value < current:
        a = i
        b = j
        max_value = current

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))