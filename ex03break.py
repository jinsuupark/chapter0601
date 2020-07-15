score = [92, 86, 68, 120, 56]

for s in score:
    if(s<0) or (s>100):
        print(s,"은(는) 범위를 벗어났습니다 ")
        break

    print(s)
    
print("성적 처리 끝")

#x = int(input("몇단을 출력할까요?\n"))
for x in range(2,10):
    print(x,"단 출력")
    for n in range(1,10):
        print(x," * ",n,"=",x*n)