# x=10
# y=20
#
# #x,y 교환
# a=x  #a = temp
# x=y
# y=a
#
#
# print("x",x)
# print("y",y)


#가위바위보 게임
# 0:rock 1:scissors 2:paper
#변하지않는변수(상수) 는 대문자
#변수는 소문자
#관례!
import random
ROCK = 0
SCISSORS = 1
PAPER = 2

com = int(random.random()*10)%3 # 1~9의값을 받고 3의 나머지값으로 0,1,2 값을 추출
print(com)
me = int(input("가위바위보를 입력하세요 주먹0 가위1 보2\n"))



# if com == ROCK:
#     if me ==ROCK:
#         print("비겼습니다")
#     elif me ==SCISSORS:
#         print("졌습니다")
#     else:
#         print("이겼습니다")
# elif com ==SCISSORS :
#     if me == ROCK:
#         print("이겼습니다")
#     elif me == SCISSORS:
#         print("비겼습니다")
#     else:
#         print("졌습니다")
# else:
#     if me ==ROCK:
#         print("졌습니다")
#     elif me == SCISSORS:
#         print("이겼습니다")
#     else:
#         print("비겼습니다")
#
if me >= 3 or me < 0:
    print("숫자를 잘못 입력하셨습니다")
elif com == me:
    print("비겼습니다")
elif com == ROCK:
    if me == SCISSORS: print("컴퓨터가 이겼습니다")
    else: print(" 내가 이겼습니다")
elif com == SCISSORS:
    if me == ROCK: print("내가 이겼습니다")
    else: print("컴퓨터가 이겼습니다")
elif com == PAPER:
    if me == ROCK:print("컴퓨터가 이겼습니다")
    else: print("내가 이겼습니다")


