import datetime
import time

def getCurrentTime():
    timestring = str(datetime.datetime.now())
    return timestring[11:19]

def getCurrentDate():
    timestring = str(datetime.datetime.now())
    return timestring[5:10] + '-' + timestring[:4]


print("Welcome to your watch!")
while True:
    choice = input("What would you like to do?  Press \"1\" to check the time, \"2\" to check the date, \"3\" to use the stopwatch, or \"4\" to set a timer. ")
    if choice == "1":
        print("The time is: " + getCurrentTime())
        yorn = input("Would you like to continue using your watch? (Enter yes or no)")
        if(yorn.lower() == "no"):
            print("Thank you for taking the time to use your watch!")
            break

    elif choice == "2":
        print("The date is: " + getCurrentDate())
        yorn = input("Would you like to continue using your watch? (Enter yes or no)")
        if (yorn.lower() == "no"):
            print("Thank you for taking the time to use your watch!")
            break

    elif choice == "4":
        while True:
            timerlengthS = input("Enter the amount of seconds you want your timer to last for.")
            try:
                timerlength = int(timerlengthS)
                break;
            except ValueError:
                print("That was not a number, try again.")
        start = input("Press enter to start the timer.")
        print(timerlength)
        secs = 1
        while secs < timerlength+1:
            currentTime = time.time()
            endTime = currentTime + 1
            while time.time() < endTime:
                pass
            print(timerlength - secs)
            secs+=1
        print("Timer finished.")
        yorn = input("Would you like to continue using your watch? (Enter yes or no)")
        if (yorn.lower() == "no"):
            print("Thank you for taking the time to use your watch!")
            break

    else:
        print("That was not an option, try again.")
