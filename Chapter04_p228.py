# 숫자는 무작위로 입력해도 상관없습니다.
numbers = [1,5,4,8,9,2,8,2,6,3,5,6,4,2,6,7,5,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] = counter[number] + 1
else: counter[number] = 1

# 최종 출력
print(counter)