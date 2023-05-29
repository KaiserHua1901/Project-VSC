user_name = input("Enter your name:")

if len(user_name) > 12:
    print("user name is more than 12 character")

# This need to be like this because if the find() not found any space, it print out -1.
# SO this mean, if the find() is NOT printing out -1, there is a space there
elif not user_name.find(" ") == -1:
    print("user name contain space")
# OR just make it so that if it NOT have -1 print out the stuff.
elif user_name.find(" ") != -1:
    print("user name contain space")
    
elif user_name.isdigit():
    print("user name contain digit")
    
else:
    print(f"Hello {user_name}")