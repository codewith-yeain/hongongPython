# 밑변과 높이의 길이 입력하기
input_a = input(">밑변을 입력해주세요: ")
input_b = input(">높이를 입력해주세요: ")

a = int(input_a)
b = int(input_b)

# 빗변의 길이 구하기
c = ((a**2) + (b**2))**(1/2)
print("= 빗변의 길이는", c, "입니다.")