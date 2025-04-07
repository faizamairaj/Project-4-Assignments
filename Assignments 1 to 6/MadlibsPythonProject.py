def Madlibs():
  name = str (input("Enter your name: "))
  city = str (input("Enter your city name: "))
  verb = str (input("Enter verb: "))
  animal = str (input("Enter your favourite animal: "))
  adjective = str (input("Enter adjective: "))

# story
  story = (f"Ek din, {name} {city} gaya. Wahan usne ek {adjective} {animal} dekha. Jo {verb} raha tha. ye dekh kar, {name} bohot hairan hua!")
  print(story)
  
Madlibs()

