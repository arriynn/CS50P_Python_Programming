from pyfiglet import Figlet
import random
import sys
figlet = Figlet()
try:
    if len(sys.argv) == 1:
        word = input("Input: ")
        figlet.setFont(font=random.choice(figlet.getFonts()))
        print("Output:" + figlet.renderText(word))

    elif len(sys.argv) > 1 and len(sys.argv) < 4:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            word = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print("Output: " + figlet.renderText(word))

        else:
            sys.exit("Invalid Usage")

except:
    sys.exit("Invalid Usage")