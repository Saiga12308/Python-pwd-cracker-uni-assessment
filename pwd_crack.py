import cls
import os
import multiprocessing

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

    #loop of going through each password
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

pwds.close()

len_pwd_file = len(lines)

#taking sections of it to pass into function so each process can work on 100 passwords at a time
#this is dynamic, but still assumes that the no of passwords is a multiple of 5. still better than hard-coding ig
lines1 = lines[0:(len_pwd_file*(1/5))-1]
lines2 = lines[len_pwd_file*(1/5):(len_pwd_file*(2/5))-1]
lines3 = lines[len_pwd_file*(2/5):(len_pwd_file*(3/5))-1]
lines4 = lines[len_pwd_file*(3/5):(len_pwd_file*(4/5))-1]
lines5 = lines[len_pwd_file*(4/5):len_pwd_file-1]

#clearing the file from memory
del lines

#creating the processes
p1 = multiprocessing.Process(target=crack_password, args=(lines1, dict_file))
p2 = multiprocessing.Process(target=crack_password, args=(lines2, dict_file))
p3 = multiprocessing.Process(target=crack_password, args=(lines3, dict_file))
p4 = multiprocessing.Process(target=crack_password, args=(lines4, dict_file))
p5 = multiprocessing.Process(target=crack_password, args=(lines5, dict_file))

#starting the processes
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()

#waits for all processes to finish before continuing
p1.join()
p2.join()
p3.join()
p4.join()
p5.join()

dict_file.close()