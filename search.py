from dictionary import *

def padhexa(s):
    return '0x' + s[2:].zfill(2)

def search(WORD):
    dictionarys = [cmd_IMMEDIATE, cmd_ABSOLUTE, cmd_ZERO_PAGE, cmd_ACCU, cmd_IMPLIED, cmd_IND_X, cmd_IND_Y, cmd_Z_PAGE_X, cmd_ABS_X, 
    cmd_ABS_Y, cmd_RELATIVE, cmd_INDIRECT, cmd_Z_PAGE_Y,]
    print("DICT".ljust(20, " "), "OP".ljust(5, " "), "N".ljust(2, " "), "#".ljust(2, " "))
    for dictionary in dictionarys: 
        for key in dictionary:
            if key == WORD:
                word = hex(dictionary[key][0])
                word = padhexa(word)
                print(dictionary['name'].ljust(20, " "), word.ljust(5, " "), str(dictionary[key][1]).ljust(2, " "), str(dictionary[key][2]).ljust(2, " "))

while True: 
    search(input("ENTER SEARCH WORD: "))