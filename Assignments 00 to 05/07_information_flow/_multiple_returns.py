def get_user_info():
    name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    age = int(input("Enter your age: "))
    # Return multiple values as a tuple
    return name, last_name, email, age 

def main(): 
    user_data = get_user_info()
    print("Recieved the following user data:", user_data)
   
main()