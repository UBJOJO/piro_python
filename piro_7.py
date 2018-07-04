# 7-3
greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
# greetings list 목록

def greet(g):           #greet 함수
    i = len(g)
    sum = 0
    while sum <= i - 1:
        print(g[sum])
        sum = sum + 1


greet(greetings)

# 7-11  ( 다시보기 )

numbers = []            # numbers에 자연수 1부터 10까지 추가
i = 1
while i <= 10:
    numbers.append(i)
    i = i + 1
print(numbers)

a = 0
while a < 10:
    if numbers[a] % 2 == 1:
        del numbers[a]
    a = a + 1
print(numbers)


