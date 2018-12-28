# This Code is written by Debkanta Mondal
import random
# Randomly Chosen a number between 1 to 9
number=random.randint(1,101)
#UI Design
print("Welcome to APPS Guessing Game 2k18\n-----------------------------------\n\t\t\t\t\t\t\t\t@Developer: Debkanta Mondal")
print("INSTRUCTIONS\n-------------\n")
print("""1.Guess in the time of Guessing.\n
2.Don't Try t Cheat with Machine.\n
3.This is auto motive Game.\n
4.Your Max Attempt is 10.\n
 So Try Guessing Right Faster.\n""")
#Ready Choice Logic
print("Are You Ready To Play? If 'Yes' Type 1 Otherwise Type 0:\n")
ready=int(input())
if ready==1:
    #Choice Input Logic
    choice=int(input("Plz Input Your Guess out of 1 to 100\n"))
    #Main Logic of Game
    attempt=1
    while choice!=number:
        attempt+=1
        if attempt >= 11:
            print("Your Guessing Time is Over. Try in Next Session.")
            comment_bad = input("PLZ Comment Are you felling Sad?Try Later....\n")
            break
        else:
            if choice>number:
                print("Plz Guess Lower.")
                choice = int(input("Plz Input Your Guess Again out of 1 to 100\n"))
            else:
                print("Plz Guess higher.")
                choice = int(input("Plz Input Your Guess Again out of 1 to 100\n"))

    else:
        print("Wow....!Your Guess ",number,"is Right","and Your Attempt is",attempt)
        comment=input("PLZ Comment Are you felling Happy?\n")
else:
    print("Ok.....")
    input("If You Want Plz Write Down Why?\n")
