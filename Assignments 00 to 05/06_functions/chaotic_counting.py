import random

Done_likelihood = 0.3

def chaotic_counting():
    for i in range(1,11):
        if random.random() < Done_likelihood:
            break
        print(i)

def main():
    print("counting until 10 or stopping randomly!")
    chaotic_counting()
    print("I'm done.")
main()
    
    
    
