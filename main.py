from pwd_crack import pwd_crack
from ssh import ssh

if __name__ == "__main__":
    while True:
        try:
            option = int(input("Which section would you like to run?\n"+
                               "1. Password cracker\n"+
                               "2. SSH client\n"))

            if option != 1 and option != 2:
                print("Please only select a given option.\n")

            else:
                break

        except ValueError:
            print("Please only select a given option.\n")


    if option == 1:
        while True:
            try:
                process_count = int(input("Select the process count:\n" +
                                            "1. 10\n" +
                                            "2. 20\n" +
                                            "3. 50\n"))
                if process_count == 1:
                    pwd = pwd_crack(10)
                    break

                elif process_count == 2:
                    pwd = pwd_crack(20)
                    break

                elif process_count == 3:
                    pwd = pwd_crack(50)
                    break

                else:
                    print("Please only select a value from the list.\n")

            except ValueError:
                print("Please only select a value from the list.\n")
        
        pwd.start()

    #This doesn't need to be an elif as I make sure option is either 1 or 2 earlier, but I do so to guarantee that other numbers don't make it through
    if option == 2:
        ssh_client = ssh()
        ssh_client.start()