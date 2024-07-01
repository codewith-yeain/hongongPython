# 정수를 입력받기
number = input("정수를 입력해주세요> ")
number = int(number)

# 2의 배수인지 확인하기
if number % 2 == 0:
    print("{}은(는) 2로 나누어 떨어지는 숫자입니다.".format(number))
else:
    print("{}은(는) 2로 나누어 떨어지는 숫자가 아닙니다.".format(number))

# 3의 배수인지 확인하기
if number % 3 == 0:
    print("{}은(는) 3으로 나누어 떨어지는 숫자입니다.".format(number))
else:
    print("{}은(는) 3으로 나누어 떨어지는 숫자가 아닙니다.".format(number))

# 4의 배수인지 확인하기
if number % 4 == 0:
    print("{}은(는) 4로 나누어 떨어지는 숫자입니다.".format(number))
else:
    print("{}은(는) 4로 나누어 떨어지는 숫자가 아닙니다.".format(number))

# 5의 배수인지 확인하기
if number % 5 == 0:
    print("{}은(는) 5로 나누어 떨어지는 숫자입니다.".format(number))
else:
    print("{}은(는) 5로 나누어 떨어지는 숫자가 아닙니다.".format(number))