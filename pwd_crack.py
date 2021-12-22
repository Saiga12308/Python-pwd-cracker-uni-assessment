from multiprocessing.dummy import Pool



# DIVIDE DICTIONARY FILE INTO 18 THEN EACH PROCESS WORKS ON THOSE WORDS



global worker_count
worker_count = 18



#putting full file into memory to divide between threads (only 41kb and 255kb, so it won't be an issue)
pwds = open("A0197423_AIDAN_HERRON_hashed_pw.lst", "r")
dict_file = open("ow_tiny_lower.lst", "r")

global pwd_lines
pwd_lines = pwds.readlines()

dict_lines = dict_file.readlines()

for i in range(10):
    dict_lines.pop(0)

dict_file.close()
pwds.close()



#variables used for main process and subprocesses to communicate
global complete_processes
complete_processes = []

global terminated_processes
terminated_processes = []

global is_active
is_active = True



def crack_password(pid):
    while is_active:
        slice_a = int((pid/worker_count) * len(dict_lines))
        slice_b = int((((pid+1) / worker_count) * len(dict_lines)) -1)

        word_list = dict_lines[slice_a:slice_b]
        
        for password in list_pwds:
            password = password.replace("\n", "")

            #0 = id, 1 = my name and student no, 2 = salt, 3 = hashed pwd
            split_pwd = password.split(":")

            if 



if __name__ == "__main__":

    pool = Pool(worker_count)

    pool.map(crack_password, range(worker_count))

    while len(complete_processes)+len(terminated_processes) != worker_count:
        pass