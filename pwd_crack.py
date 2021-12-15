import cls
import os

#get pw hash and salt
#go into dict and get first line
#check if 7 chars or more

#if not, ignore
#if 7 chars, add "1" to end then try with salt added to beginning and end
#if 8 chars or more, try as is with salt added to beginning and end

#if doesn't work, attempt with a variety of mangling rules

#if still doesn't work, move on to next line in dict and repeat

#if it finds a match, save to file
#if it gets to end of dict and finds no match, move on to next pw



#getting relative path to the files and opening them
cur_path = os.path.dirname(__file__)

lst_path = os.path.relpath("lst\\A0197423_AIDAN_HERRON_hashed_pw.lst", cur_path)
dict_path = os.path.relpath("lst\\ow_tiny_lower.lst", cur_path)

pwds = open(lst_path, "r")
dict_file = open(dict_path, "r")

#starting loop of going through each password
for line in pwds:

    #0 = id, 1 = my name and student no, 2 = salt, 3 = hashed pwd
    lst_pwd = line.split(":")

    for line in dict_file:

        #ignoring comments and words too short to be used in a password
        word = line.strip()
        if not word.startswith("#") and len(word) >= 7:

            word_variants = [word]






pwds.close()
dict_file.close()