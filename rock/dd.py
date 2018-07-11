# Num = int(input())
# subNumber = list(map(int, input().split()))
# subNumber.sort()
# H_score = subNumber[Num - 1]
#
# for i in range(Num):
#     subNumber[i] = subNumber[i] / H_score * 100
#
# sum = 0
# for i in range(Num):
#     sum += subNumber[i]
#
# aver = sum / Num
# print('%.2f' % aver)
SubNum = int(input())
subNumber = []
subAv = []
for i in range(SubNum):
    subNumber[i] = list(map(int, input().split()))
    subAv[i] = subNumber[i]/subNumber[i][0]
    print(subNumber[i])
    print(subAv[i])

