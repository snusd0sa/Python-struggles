class User:
    pass  # used to avoid error when class is empty (indentation error)

    def __init__(self, user_id, username):  # constructor
        print("new user being created...")
        self.id = user_id  # attributes
        self.username = username
        self.followers = 0  # default value instead of providing it as an argument
        self.following = 0

    def follow(self, user):  # method of the class User (function inside a class)
        user.followers += 1
        self.following += 1


user_1 = User("001", "Mathias")  # creating an object of the class User
print(user_1.id)  # accessing the attributes of the object
print(user_1.username)  # accessing the attributes of the object
user_2 = User("002", "Angela")
# user_1 = User()  # creating an object of the class User
# user_1.id = "001"  # adding attributes to the object
# user_1.username = "Mathias"
#
# print(user_1.username)  # accessing the attributes of the object
#
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Angela"
#
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
