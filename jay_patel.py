from time import sleep
import random as r
from ansi_utils import *

def main():
    bold = "\u001b[1m"
    dim = "\u001b[2m"
    italic = "\u001b[3m"
    underline = "\u001b[4m"
    strike = "\u001b[9m"
    clear_effect = '\u001b[0m'
    Jay = 'Jay '
    Patel = 'Patel'
    while True:
        ansi_color = r.choice([foreground.rgb(27, 161, 226), foreground.rgb(0, 138, 0),
                         foreground.rgb(162, 0, 37), foreground.rgb(250, 104, 0),
                         foreground.rgb(109, 135, 100), foreground.rgb(255, 255, 255)])
        ansi_effect = r.choice([bold, dim, italic, underline, strike, ''])
        new = r.choice(['', '\n'])
        sanjay = r.choice(['', 'Sanjay '])
        sleep(1.25 * r.random())

        print(new+ansi_color+ansi_effect+Jay+sanjay+Patel+clear_effect+' ', end='', flush=True)

main()

