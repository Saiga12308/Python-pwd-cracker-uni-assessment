from multiprocessing import Pool
from datetime import date, timedelta
from cls.word_variants import WordVarGen

worker_count = 50

#putting full file into memory to divide between threads (only 41kb, so it shouldn't be an issue)
pwds = open("A0197423_AIDAN_HERRON_hashed_pw.lst", "r")
global lines
lines = pwds.readlines()
pwds.close()

#getting all dates in a list so it doesn't have to be generated each time a process wants to access them
global date_list
date_list = []

start_date = date(2000, 1, 1) 
end_date = date(2003, 12, 31)

delta = end_date - start_date   # returns timedelta

for i in range(delta.days + 1):
    day = start_date + timedelta(days=i)
    day = str(day).split("-")

    date_list.append(day[0]+day[1]+day[2])
    date_list.append(day[2]+day[1]+day[0])



def crack_password(pid):
    #function for loops for cracking password. done this way to be able to utilise multiprocessing

    gen = WordVarGen()

    #used for slices for threads
    len_pwd_file = len(lines)

    pwds.close()

    slice_a = int((pid/worker_count) * len_pwd_file)
    slice_b = int((((pid+1) / worker_count) * len_pwd_file) -1)

    list_pwds = lines[slice_a:slice_b]

    dict_file = open("ow_tiny_lower.lst", "r")

    for password in list_pwds:
        #0 = id, 1 = my name and student no, 2 = salt, 3 = hashed pwd
        split_pwd = password.split(":")

        #still had \n at end from file
        split_pwd[3] = split_pwd[3].replace("\n", "")

        for line in dict_file:
            #ignoring comments in the dictionary file
            word = line.strip()
            word = word.replace("\n", "")

            if not word.startswith("#") and len(word) >= 10:
                #selects hashing algorithm based on length of the hash
                if len(split_pwd[3]) == 32:

                    print("md5 "+str(pid)+" "+word+"\n")
                    hashes = gen.word_variant_hashed(word=word, salt=split_pwd[2], dates=date_list)

                elif len(split_pwd[3]) == 64:

                    print("sha256 "+str(pid)+" "+word+"\n")
                    hashes = gen.word_variant_hashed(word=word, salt=split_pwd[2], dates=date_list, md5=False)

                if split_pwd[3] in hashes:
                    #checks if the hash is in the dictionary returned, then adds to a file if it does
                    correct_passwords = open("A0197423_Aidan_Herron_cracked_pw.lst", "a")

                    correct_passwords.write(split_pwd[0] + ":" + hashes[split_pwd[3]] + "\n")
                    print("Cracked a password!")

                    correct_passwords.close()
                    break

    print("Done cracking passwords!"+str(pid))
    dict_file.close()

#creating the processes
if __name__ == "__main__":

    pool = Pool(worker_count)

    pool.map(crack_password, range(worker_count))

    del lines