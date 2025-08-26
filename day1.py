


'''Name =input("Enter Your name: ")
City= input("I am from: ")
other=f"Hellow Friends My name is {Name}, I am from {City}"

other_person=input("Enter other person name: ")
print(other.replace("Friends",other_person))'''


# def dep_type(env):
#     env = "dev"
#     if env == "dev":
#         print("Its Dev TOol")
#     elif env== "sales":
#         print("Its Sales Tool")
#     elif env=="prod":
#         print("Its Production tool")
#     else:
#         print("What do you want to say")

# dep_type(env="dev")


# def sum_no():
#     a = int(input("enter a number; "))
#     b = int(input("enter a number; "))
#     print(a+b)
# sum_no()

import os

print(os.name())

def check_os(system):
    if system == "Windows":
        print("you are using Windows")
    elif system == "Mac":
        print("You are using Mac")
    else:
        print("You are using OG LINUX")

for i in range(0,5):

    check_os("Windows")

