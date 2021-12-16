import multiprocessing as mp
from random import randint

def write_to_file(num):
    file = open("foo.txt", "a")
    file.write("I am making this longer so that there's a bigger chance that it does this at the same time. I am process "+str(num)+"\n")
    print("done!")


if __name__ == "__main__":
    pool = mp.Pool(5)

    pool.map(write_to_file, range(5))