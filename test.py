worker_count = 50
pid = 49

pwds = open("A0197423_AIDAN_HERRON_hashed_pw.lst", "r")
lines = pwds.readlines()

len_pwd_file = len(lines)

pwds.close()

slice_a = int((pid/worker_count) * len_pwd_file)
slice_b = int((((pid+1) / worker_count) * len_pwd_file))

print(lines[slice_a:slice_b])
#print(int((pid/worker_count) * len_pwd_file))
#print(int((((pid+1) / worker_count) * len_pwd_file) -1))