# inputMonth, inputDay = map(int, input().split())
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
sum = []
k = 0
while k != 11:
    sum[k] += month[k]
    print(sum[k])
    k += 1





# for i in range(0, 12):
#     if i == inputMonth - 1:
#         day = month[i] + inputDay
#         if day % 7 == 0:
#             print('SAT')
#         elif day % 7 == 1:
#             print('SUN')
#         elif day % 7 == 2:
#             print('MON')
#         elif day % 7 == 3:
#             print('TUE')
#         elif day % 7 == 4:
#             print('WED')
#         elif day % 7 == 5:
#             print('THU')
#         elif day % 7 == 6:
#             print('FRI')

