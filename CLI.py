from Passy import *

def Login():
    User = input("Input your username: ")
    print(CheckCreds(User,Pass = input("Input your password: ")))

# if __name__ == "__main__":
#     print(f"Arguments count: {len(sys.argv)}")
#     for i, arg in enumerate(sys.argv):
#         print(f"Argument {i:>6}: {arg}")
        
if __name__ == "__main__":
    Login()