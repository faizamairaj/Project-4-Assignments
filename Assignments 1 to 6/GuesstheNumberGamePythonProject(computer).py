import random
print("Socho ek secret number 1 se 10 ke beech! 🤔")
user_input = int(input("Apna secret number likho (Computer isko guess karega): "))

computer_num = random.randint(1,10)
print(f"Computer ka pehla guess hai: {computer_num}")

while True:
 feedback = input("Kya yeh guess sahi hai? (bara/chhota/sahi):")
 if feedback == "sahi":
    print("Yay! 🎉 Computer ne sahi guess kar liya! ✅")
    break
 elif feedback == "chhota":
    print("Too Low..")
 elif feedback == "bara":
   print("Too High...")
 else:
   print("Galat input! Sirf 'bara', 'chhota' ya 'sahi' likho.")
   continue
 computer_num = random.randint(1,10)
 print(f"Computer ka naya guess hai:{computer_num}")
