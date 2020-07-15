student =1
while student <=5:
    print(student, "번 학생의 성적을 처리합니다.")
    student += 1 #복합대입연산자

print()

num = 1
even_total =0
odd_total =0
while num<=100:
    if num%2 ==0:
        even_total +=num
    else:
        odd_total += num
    num +=1
print("짝수의 합:", even_total)
print("홀수의 합:", odd_total)
