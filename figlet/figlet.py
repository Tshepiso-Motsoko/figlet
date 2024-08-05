import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        # select a font from the list of available fonts
        font = random.choice(available_fonts)
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in available_fonts:
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")

    # Set the selected font
    figlet.setFont(font=font)

    # Prompt the user for a string of text
    input_str = input("Input: ")

    # Output the text in the desired font
    print(figlet.renderText(input_str))

if __name__ == "__main__":
    main()
