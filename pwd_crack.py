import cls
import os
import multiprocessing as mp

def write_pw_to_file(q, id, password):
    correct_passwords = open("correct_pws.txt", "a")



def crack_password(pwds, dict_file):
    #function for loops for cracking password. done this way to be able to utilise multiprocessing

    for line in pwds:
        #0 = id, 1 = my name and student no, 2 = salt, 3 = hashed pwd
        split_pwd = line.split(":")

        for line in dict_file:
            #ignoring comments
            word = line.strip()
            if not word.startswith("#"):
                if len(split_pwd[3]) == 32:
                    hashes = cls.word_variants.word_variant_hashed(line, split_pwd[2])
                if len(split_pwd[3]) == 64:
                    hashes = cls.word_variants.word_variant_hashed(line, split_pwd[2], False)

                if split_pwd[3] in hashes:


#getting relative path to the files and opening them
cur_path = os.path.dirname(__file__)

lst_path = os.path.relpath("lst\\A0197423_AIDAN_HERRON_hashed_pw.lst", cur_path)
dict_path = os.path.relpath("lst\\ow_tiny_lower.lst", cur_path)

pwds = open(lst_path, "r")
dict_file = open(dict_path, "r")

#putting full file into memory to divide between processes (only 41kb, so it won't be an issue)
lines = pwds.readlines()
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