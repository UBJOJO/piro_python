# 11-8
#User Class 만들기
class User:
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# 자료넣어줌
user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")

user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User()
user3.initialize("Taeho", "taeho@codeit.kr", "123abc")

user4 = User()
user4.initialize("Lisa", "lisa@codeit.kr", "abc123")

print(user1.name)

# 11-12


class User:
    # 초기설정 init
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    # introduce 메서드
    def introduce(self):
        print("My name is %s" % (self.name))
        print("My email is %s" % (self.email))
    # introduce_twice 메서드
    def introduce_twice(self):
        for i in range(2):
            self.introduce()


user1 = User("Young", "young@codeit.kr", "123456")
user1.introduce()
user1.introduce_twice()

# 11-14
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.following_list = []
        self.followers_list = []

    def follow(self, another_user):
        self.following_list.append(another_user)
        another_user.followers_list.append(self)

    def num_following(self):
        return len(self.following_list)

    def num_folowers(self):
        return len(self.followers_list)


user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user2.follow(user4)
user4.follow(user1)

print(user1.name, user1.num_followers(), user1.num_following())
print(user2.name, user2.num_followers(), user2.num_following())
print(user3.name, user3.num_followers(), user3.num_following())
print(user4.name, user4.num_followers(), user4.num_following())