#imports modules
from datetime import date
from datetime import datetime
import pyperclip as pc

#defines date / time
today = date.today()
now = datetime.now()

class date:
    DEFAULT = today.strftime("%Y-%m-%d")
    VERBOSE = now.strftime("%Y-%m-%d-%H%M%S")
#    MANUAL = manual input (prompt for this)
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
class version:
    NAME = "fileNamer"
    INFO = "Build 0.0.2"
    AUTHOR = "choi"
    DATE = "2022-01-03"
class prompt:
    BPM = "Enter BPM: "
    KEYWORD = "Enter Keyword: "
    OUTPUT = "Successfully added to clipboard: "

#start up info
#print ()
print(color.BOLD + color.RED + version.NAME + color.END)
print(color.BOLD + color.CYAN + version.INFO + color.END)

#color.DARKCYAN + version.DATE + color.END, sep=' ')
print ()

#input
BPM = input(color.BOLD + color.YELLOW + prompt.BPM + color.END)
BPMFormatted = BPM + "BPM"
KeyWord = input (color.BOLD + color.YELLOW + prompt.KEYWORD + color.END)

#output
output = "%s-%s-%s" % (date.DEFAULT, BPMFormatted, KeyWord)
pc.copy(output)
print ()
print(color.BOLD + prompt.OUTPUT + color.END)
print(color.CYAN + output + color.END)


#print (date.DEFAULT)
#print (date.VERBOSE)

