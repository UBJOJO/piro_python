# 5-4
i = 1
while i <= 50:
    print(i * 2)
    i = i + 1

# 5-6
i = 100
while i % 23 != 0:
    i = i + 1
print(i)

# 5-11
def print_grade(midterm, final):
    total = midterm + final

    if total >= 90:
        print("You get on A")
    elif total >= 80:
        print("You get on B")
    elif total >= 70:
        print("You get on C")
    elif total >= 60:
        print("You get on D")
    else:
        print("You fail")


print_grade(50, 0)

# 5-17

n = 120
i = 1
count = 0
while i <= 120:
    if 120 % i == 0:
        print(i)
        count = count + 1
    i = i + 1
print("120의 약수는 총 %d개입니다" % (count))