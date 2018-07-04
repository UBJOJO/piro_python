# 3-4
name = "Jeong"
nationality = "korea"
phone_number = "01022984505"

print("Hi, my name is %s. I'from %s. My phone number is %s." % (name, nationality, phone_number))

# 3-9
def print_full_name(first_name, last_name):
    print(last_name + ',' + ' ' + first_name)

print_full_name("재현", "정")

# 3-11
def calculate_change(payment, cost):
    x = payment - cost
    a = int(x / 50000)
    x = x % 50000
    b = int(x / 10000)
    x = x % 10000
    c = int(x / 5000)
    x = x % 5000
    d = int(x / 1000)
    x = x % 1000

    print("50000원 지폐:  %d장" % (a))
    print("10000원 지폐:  %d장" % (b))
    print("5000원 지폐:  %d장" % (c))
    print("1000원 지폐:  %d장" % (d))


calculate_change(100000, 4000)