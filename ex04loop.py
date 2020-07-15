#파이썬의 특징
for star in range(1,10):
    print("*"*star)

# 이중루프문  대표사례
for y in range(1,10):
    for x in range(y):
        print("*",end="")
    print()

for y in range(10,0,-1):
    for x in range(y):
        print("*",end='')
    print()

#
# result = False
#
# print("3 + 4 = ? ")
# for num in range(3):
#     a = int(input('정답을 입력하세요 : '))
#     if a == 7:
#         result = True
#         break
#
# if result:
#     print("정답")
# else:
#     print("땡! 기회를 모두 사용하였습니다")