# 날짜 데이터 불러오기
import datetime
now = datetime.datetime.now()

# 대화를 입력받기
chat = input("대화를 시작해보세요> ")

if "안녕" in chat:
    print("안녕하세요.")
elif "지금 몇 시" in chat:
    print("지금은 {}시 입니다.".format(now.hour))
else:
    print(chat)