# 염기의 개수
bases = list(input("염기 서열을 입력해주세요: "))
dna = {"a" : 0, "t" : 0, "g" : 0, "c" : 0}

print(bases)
for data in dna:
    for i in bases:
        if i == data: dna[data] += 1
    print("{}의 개수: {}".format(data, dna[data]))
# ctacaatgtcagtatacccattgcattagccggc