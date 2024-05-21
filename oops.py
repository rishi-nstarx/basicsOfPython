# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(1000/10)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable

# table  = PrettyTable()
# # table.align = "l"
# # table.border = True

# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"], "l")
# table.add_column("Type", ["Electric", "Water", "Fire"], "r")

# print(table)

class User:
    def __init__(self, userid, username):
        self.userid = userid
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    
user1 = User(1, "Rishi")
user2 = User(2, "Sibbu")

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
