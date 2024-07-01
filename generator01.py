# 함수를 선언합니다.
def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")
# 함수를 호출합니다.
output = test()
# next() 함수를 호출합니다.
print("D 지점 통과")
a = next(output) # yield1 전까지 실행
