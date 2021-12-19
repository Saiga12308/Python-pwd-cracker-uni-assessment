﻿from cls.word_variants import word_variant_hashed
from multiprocessing.dummy import Pool

worker_count = 100

#putting full file into memory to divide between threads (only 41kb, so it won't be an issue)
pwds = open("A0197423_AIDAN_HERRON_hashed_pw.lst", "r")
global lines
lines = pwds.readlines()
pwds.close()

def crack_password(pid):
    #function for loops for cracking password. done this way to be able to utilise multiprocessing
    
    #used for slices for threads
    len_pwd_file = len(lines)

    pwds.close()

    slice_a = int((pid/worker_count) * len_pwd_file)
    slice_b = int((((pid+1) / worker_count) * len_pwd_file) -1)

    list_pwds = lines[slice_a:slice_b]

    dict_file = open("ow_tiny_lower.lst", "r")
    correct_passwords = open("correct_pws.txt", "a")

    hashes = {}

    for password in list_pwds:
        #0 = id, 1 = my name and student no, 2 = salt, 3 = hashed pwd
        split_pwd = password.split(":")

        #still had \n at end from file
        split_pwd[3] = split_pwd[3].replace("\n", "")

        for line in dict_file:
            #ignoring comments
            word = line.strip()
            word = word.replace("\n", "")

            if not word.startswith("#"):
                if len(split_pwd[3]) == 32:
                    print("md5 "+str(pid)+" "+word+"\n")
                    hashes = word_variant_hashed(word, split_pwd[2])
                elif len(split_pwd[3]) == 64:
                    print("sha256 "+str(pid)+" "+word+"\n")
                    hashes = word_variant_hashed(word, split_pwd[2], False)

                if split_pwd[3] in hashes:
                    correct_passwords.write(split_pwd[0] + ":" + hashes[split_pwd[3]] + "\n")
                    break
    print("Done cracking passwords!"+str(pid))
    dict_file.close()

#creating the threads
if __name__ == "__main__":

    pool = Pool(worker_count)

    pool.map(crack_password, range(worker_count))