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

# 7-7

def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5 / 9
    return(celcius)


sample_temperature_list = [40, 15, 32, 64, -4, 11]

print("화씨 온도 리스트: " + str(sample_temperature_list))

i = 0
while i < len(sample_temperature_list):
    result = float(fahrenheit_to_celcius(sample_temperature_list[i]))
    result = round(result, 2)
    sample_temperature_list[i] = result

    i += 1

print("섭씨 온도 리스트: " + str(sample_temperature_list))

# 7-9
def krw_to_usd(won):
    return won / 1000

def usd_to_jpy(dollars):
    return dollars * (1000 / 8)


amounts = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000]
print("한국 화폐: " + str(amounts))


i = 0
while i < len(amounts):
    amounts[i] = float(krw_to_usd(amounts[i]))
    i = i + 1
print("미국 화폐: " + str(amounts))


i = 0
while i < len(amounts):
    amounts[i] = float(usd_to_jpy(amounts[i]))
    i = i + 1
print("일본 화폐: " + str(amounts))

# 7-11  ( 다시보기 )
numbers = []

# numbers 1 부터 10까지 추가
i = 1
while i <= 10:
    numbers.append(i)
    i = i + 1

print(str(numbers))

# 홀수제거
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        del numbers[i]
    else:
        i += 1

print(numbers)

# 0 자리에 20 삽입
numbers.insert(0, 20)
print(str(numbers))

#정렬
numbers.sort()
print(str(numbers))


