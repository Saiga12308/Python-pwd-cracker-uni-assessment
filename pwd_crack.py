import cls
import os
import multiprocessing as mp

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


def crack_password(pwds, dict_file):
    #function for loops for cracking password. done this way to be able to utilise multiprocessing

    for line in pwds:
        #0 = id, 1 = my name and student no, 2 = salt, 3 = hashed pwd
        lst_pwd = line.split(":")

        for line in dict_file:
            #ignoring comments and words too short to be used in a password
            word = line.strip()
            if not word.startswith("#") and len(word) >= 7:


#getting relative path to the files and opening them
cur_path = os.path.dirname(__file__)

lst_path = os.path.relpath("lst\\A0197423_AIDAN_HERRON_hashed_pw.lst", cur_path)
dict_path = os.path.relpath("lst\\ow_tiny_lower.lst", cur_path)

pwds = open(lst_path, "r")
dict_file = open(dict_path, "r")

#putting full file into memory (only 41kb, so it won't be an issue)
lines = pwds.readlines()

#tfw preventing memory leaks
pwds.close()

#used later for long math sequence
len_pwd_file = len(lines)

#to store processes so I can wait on them
process_list = []

#creating the processes
if __name__ == "__main__":
    mp.set_start_method("spawn")
    for i in range(20):
        #this long section of math is a way to divide up the passwords between the processes
        p = mp.Process(target=crack_password, args=(lines[(i/20) * len_pwd_file : (((i+1) / 20) * len_pwd_file) -1], dict_file))
        p.start()
        process_list.append(p)

#waits for all processes to finish before continuing
for process in process_list:
    process.join()

#clearing the file from memory and closing the dictionary file
del lines
dict_file.close()