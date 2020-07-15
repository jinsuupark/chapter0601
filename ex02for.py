for student in [1,2,3,4,5]:
    print(student,"번 학생의 성적을 처리합니다")

total = 0
for num in range(1,101): #종료값은 포함되지 않는다
    total += num

print("total = ", total)


total = 0
for num in range(2,101,2): #시작,끝, 증가값
    total += num
print("total =",total)


for num in range(5): # 0,1,2,3,4 하나만 일때는 끝값.시작값의 default 는 0
    print(num)

for x in range(1,51):
    if (x % 10) == 0:
        print('+',end='')
    else:
        print('-',end ='')