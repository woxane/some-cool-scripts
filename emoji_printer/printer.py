#!/usr/bin/env python3

from sys import argv
from pyautogui import write
from os import path,system


def printer(word) : 
    write(word) 

def notifaction_send(notifation_data) : 
    system(f"notify-send printer {notifation_data}")

def word_finder(index_) : 
    file_path = path.dirname(argv[0]) # this variable is for while you want to run this script from another directory and we have error beacuse there is not any data_file.txt in there .
    with open(path.abspath(file_path)+"/data_file.txt" , "r") as file : 
        return((file.read().splitlines())[index_-1])


if __name__ == "__main__" : 
    try :
        word = word_finder(int(argv[1]))
        printer(word)
    except IndexError : 
        notifaction_send(" 'the index that you sent for the print is not valid ! (maybe its not in the list)'")
