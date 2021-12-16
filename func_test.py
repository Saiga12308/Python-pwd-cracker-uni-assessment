from cls.word_variants import word_variant_hashed

def crack_password(pid):
    #function for loops for cracking password. done this way to be able to utilise multiprocessing

    #putting full file into memory to divide between threads (only 41kb, so it won't be an issue)
    pwds = open("A0197423_AIDAN_HERRON_hashed_pw.lst", "r")
    lines = pwds.readlines()

    #used for slices for threads
    len_pwd_file = len(lines)

    pwds.close()

    slice_a = int((pid/20) * len_pwd_file)
    slice_b = int((((pid+1) / 20) * len_pwd_file) -1)

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
                    hashes = word_variant_hashed("a", "fdsJKf")
                    print("md5")
                elif len(split_pwd[3]) == 64:
                    hashes = word_variant_hashed("a", "fdsJKf", False)
                    print("sha256")

                if "d9748f777f9eb0c017c1031443223427" in hashes:
                    correct_passwords.write("aaaa")
                    break
        break
    print("Done cracking passwords!")
    dict_file.close()


crack_password(0)