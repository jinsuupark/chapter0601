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
win_player=0
win_com=0
draw=0
for num in range(3):
    print(num+1,"번째 게임")
    #com = int(random.random()*10)%3 # 1~9의값을 받고 3의 나머지값으로 0,1,2 값을 추출
    com = int(random.random()*3)
    me = int(input("가위바위보를 입력하세요 주먹0 가위1 보2\n"))
    if com==0:
        coms ="ROCK"
    elif com ==1:
        coms ="SCISSORS"
    else:
        coms="PAPER"
    print("컴퓨터는", coms)


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
        draw +=1
    elif com == ROCK:
        if me == SCISSORS:
            print("컴퓨터가 이겼습니다")
            win_com += 1
        else:
            print(" 내가 이겼습니다")
            win_player += 1
    elif com == SCISSORS:
        if me == ROCK:
            print("내가 이겼습니다")
            win_player += 1
        else:
            print("컴퓨터가 이겼습니다")
            win_com += 1
    elif com == PAPER:
        if me == ROCK:
            print("컴퓨터가 이겼습니다")
            win_com +=1
        else:
            print("내가 이겼습니다")
            win_player += 1


print("player가 ",win_player,"번 이기고 computer가",win_com,"이겼으며 비긴횟수는",(3-(win_com+win_player)),"입니다")

if win_com == win_player:
    print("비겼습니다")
elif win_com > win_player:
    print("컴퓨터가 이겼습니다")
else:
    print("내가 이겼습니다")


