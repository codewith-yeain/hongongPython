seatableMin = 2
seatableMax = 10
all = 100
memo = {}

def task(rest, seating):
    key = str([rest, seating])
    # 종료조건
    if key in memo:
        return memo[key]

    if rest < 0:
        return 0
    
    if rest == 0:
        return 1

    # 재귀처리
    count = 0
    for i in range(seating, seatableMax + 1):
        count += task(rest - i, i)
    
    # 메모화 처리
    memo[key] = count

    # 종료
    return count

print(task(all, seatableMin))