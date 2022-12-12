import regex


import re


def hapax(filepath):
    # Open the file from the path
    file = open(filepath)
    #---------------------------#
    # Containing all the words + Reading from variable "file", w+ means write#
    words = re.findall('\w+', file.read().lower())
    #-------------------------------#
    # Checking all the words as keys, and if keys is duplicated, it will count as more than 1 #
    freqs = {key: 0 for key in words}
    #-------------------------------------------------------------------------------------------#
    # This below loop checks for all the words in array "freqs", and if the words is 
    # strictly only equal to 1 (which means not repeated) it will print the word out #
    for word in words:
        freqs[word] += 1
    for word in freqs:
        if freqs[word] == 1:
            print (word)

# Calls the function, duh#
hapax('new.txt')
