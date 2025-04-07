Affirmation: str = 'I am capable of doing anything I put my mind to.'

def main():
 print("please type the following affirmation: " + Affirmation)
 user_feedback = input()
 while user_feedback != Affirmation:
  print("That was not the affirmation :")

print("please type the following affirmation: " + Affirmation)
user_feedback = input()
print("That's right :")

main()

