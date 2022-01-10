from ssh import ssh

if __name__ == "__main__":
    while True:
        try:
            option = int(input("Which section would you like to run?\n"+
                               "1. Password cracker (doesn't work)\n"+
                               "2. SSH client\n"))

            if option != 2:# and option != 1:
                print("Please only select a given option.\n")

            else:
                break

        except ValueError:
            print("Please only select a given option.\n")

    #can't find a way to 

    #if option == 1:
    #    pwd = pwd_crack()
    #    pwd.start()

    #This doesn't need to be an elif as I make sure option is either 1 or 2 earlier, but I do so to guarantee that other numbers don't make it through
    if option == 2:
        ssh_client = ssh()
        ssh_client.start()