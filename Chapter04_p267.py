# 리스트 내포를 사용해본 코드입니다.
output = [x for x in range(1, 101) if "{:b}".format(x).count("0") == 1]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))
