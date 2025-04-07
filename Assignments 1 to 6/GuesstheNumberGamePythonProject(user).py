import random
print("Computer ne ek secret number socha hai! 🧠 Ab usay guess karo! 🔢")
secret_number = random.randint(1,10)
try:
 while True:
   user_input = int(input("Apna andaza lagao (1-10): "))
   if user_input == secret_number:
     print("Bingo! 🎉 Tumne sahi guess kar liya! ✅")
     break
   elif user_input < secret_number:
     print("Bara socho! 📈")
   elif user_input > secret_number:
      print("Chota socho 👀")
except ValueError:
    print("Invalid Input..")
