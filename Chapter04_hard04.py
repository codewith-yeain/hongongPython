# 2차원 리스트 평탄화

my_List = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
output = []

for i in range(len(my_List)):
    if type(my_List[i]) != list:
        output.append(my_List[i])
    else:
        for j in my_List[i]:
            output.append(j)

print(output)