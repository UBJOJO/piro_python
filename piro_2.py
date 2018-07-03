# 2-10
print("'응답하라 1988'은 많은 시청자들에게 사랑을 받은 드라마에요.")
print('데카르트는 "나는 생각한다. 고로 존재한다."라고 말했다.')

# 2-12
print("오늘은 "+str(2018)+" 년 "+str(7)+"월 "+str(3)+"일"+" 화요일입니다.")

# 2-16
wage = 5
exchange_rate = 1142.16

print("%d시간에 %d%s 벌었습니다." % (1, wage * 1, "달러"))
print("%d시간에 %d%s 벌었습니다." % (5, wage * 5, "달러"))
print("%d시간에 %.1f%s 벌었습니다." % (1, wage * 1 * exchange_rate, "원"))
print("%d시간에 %.1f%s 벌었습니다." % (1, wage * 5 * exchange_rate, "달러"))

