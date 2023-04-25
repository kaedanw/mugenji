introTitle = "Instructions:"
introMessage = """
1. TYPE a word to add to list [...]
2. Enter NOTHING to randomise a word [ENTER]
"""


# DEFINING FUNCTIONS
"""
    Ask user whether to add a word or randomise a word:
    - [Q] to quit
    - [C] to clear
    - [O] to open list in notepad
    - [P] to view list in terminal
    - ["Any word"] to add to list
    - [""] to randomise a word
"""
import subprocess
import random

def user_choice(guiInput = ""):
    userInput = guiInput.upper()
    if userInput == "Q":
        return userInput
    elif userInput == "C":
        mugenTxt = open("MugenList.txt", "w")
        mugenTxt.writelines([])
        mugenTxt.close()
        mugenList.clear()
        return userInput
    elif userInput == "O":
        subprocess.Popen(["notepad.exe","MugenList.txt"])
        return userInput
    elif userInput == "P":
        print("\n// Current List: \n")
        y = [x.replace("\n","") for x in mugenList]
        #print(y)                # Horizontal List Format
        for z in y:             # Vertical List Format
            print(z)
        print("\n//")
        return userInput
    elif (userInput != "") and (len(userInput) > 1):
        wordCheck = check_list(userInput)
        return wordCheck
    elif (userInput != "") and (len(userInput) <= 1):
        wordCheck = f"ERROR: Please enter a word longer than one letter.\n"
        print(wordCheck)
        return wordCheck
    else:
        rng = random.randint(0, len(mugenList)-1)
        wordCheck = f"\n// Generated Word: {mugenList[rng].upper()}\n"
        print(wordCheck)
        return wordCheck

"""
    Checks if word is duplicate in list
    - Add to text file if not duplicate
    - Display error and return to user input if duplicate
    - Append to a variable list for ease of use
"""
def check_list(word):
    if not (word + "\n") in mugenList:
        mugenTxt = open("MugenList.txt", "a+")
        mugenTxt.write(word + "\n")
        mugenTxt.close()
        mugenList.append(word + "\n")
        print(f"Added \"{word.upper()}\" to list.")
        return f"Added \"{word.upper()}\" to list."
    else:
        print(f"Already in list.")
        return f"Already in list."


# RUN MUGENJI
"""
    Setup MugenJi
    - Read the list from a text file (can only be done once per open func)
    - Check if list is empty -> if so add "word" to list
    - Check if last line is a linebreak -> if not add linebreak to prevent word stack
"""
mugenTxt = open("MugenList.txt", "a")
mugenTxt.close()
mugenTxt = open("MugenList.txt", "r")
mugenList = mugenTxt.readlines()
mugenTxt.close()
if not bool(mugenList):
    minEntry = "WORD"
    print("Empty list:")
    check_list(minEntry)
else:
    mugenTxt = open("MugenList.txt", "r")
    lastEntry = mugenTxt.readlines()[-1]
    mugenTxt.close()
    if lastEntry.find("\n") == -1:
        mugenTxt = open("MugenList.txt", "a+")
        mugenTxt.write("\n")
        mugenTxt.close()


mugenTxt = open("MugenList.txt", "r")
mugenList = [x.upper() for x in mugenTxt.readlines()]
mugenTxt.close()
# user_choice()
