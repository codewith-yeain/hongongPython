# 염기 코돈 개수
my_dict = {}
bases = input("염기 서열을 입력해주세요: ")
codonList = [bases[i:i+3] for i in range(0, len(bases), 3)]

for i in codonList:
    my_dict[i] = my_dict[i] + 1 if i in my_dict else "".join(codonList).count(i)

print(my_dict)
# ctacaatgtcagtatacccattgcattagccggc