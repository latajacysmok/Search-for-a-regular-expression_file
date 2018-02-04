import sys
import time

while True:
    puzzel = input("Enter the word you are looking for: \t")
    i = 0
    with open('fileName.txt','r') as f:
        for line in f:
            for word in line.split():
               if word == puzzel:
                   i += 1

        print("I found the search word: {}, {} times".format(puzzel, i))
    quit = input("\nTo finish the program, enter [yes], otherwise enter [no]: ")
    while True:
        if quit.lower() == "yes":
            print("We say goodbye and see you :)")
            time.sleep(1)
            sys.exit(0)
        elif quit.lower() == "no":
            print("Welcome back to the program.")
            time.sleep(1)
            e += 1
            break
        else:
            print("You must select [yes] or [no]!")