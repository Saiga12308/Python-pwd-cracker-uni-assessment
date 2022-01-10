import socket, atexit
from paramiko import SSHClient, AutoAddPolicy
from getpass import getpass as gp
from datetime import datetime as dt

class ssh:
    def __init__(self):
        pass

    def SSH_CONN(self, ip, server_port, uname, pword):
        #takes connection details and attempts a connection
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())

        try:
            client.connect(ip, server_port, uname, pword, timeout=10)

        except Exception as err:
            state = ((False, client), uname, str(err))

        else:
            state = ((True, client), uname, 'logon successful')

        return state


    def log(self, user, command, status, error=""):
        #function for logging events
        with open("ssh_log.txt", "a") as log_file:
            if error == "":
                log_file.write(str(dt.now()) + " : " + user + " : " + command + " : " + status + "\n")

            else:
                log_file.write(str(dt.now()) + " : " + user + " : " + command + " : " + status + " : " + error + "\n")


    def get_dir(self, client):
        #detects os and returns the correct command to get the current directory
        pwd_os = ["Linux", "Mac"]

        stdin, stdout, stderr = client.exec_command("uname")
        osname = stdout.read().decode('utf8')

        if any(os in osname.strip() for os in pwd_os):
            return "pwd"

        stdin, stdout, stderr = client.exec_command("ver")
        osname = stdout.read().decode('utf8')

        if "Windows" in osname.strip():
            return "chdir"


    def close_con(self, client, stdin, stdout, stderr, USER, SERVER):
        client.close()
        self.log(USER, "Disconnected from " + SERVER, "Successful")

        if stdin != False:
            stdin.close()
            stdout.close()
            stderr.close()

        print("Connection closed.")



    def start(self):
        login_attempt = True

        while login_attempt:
            try:
                SERVER = str(input("IP: "))

                #verifying the IP is correct (1 will still work as it's equivalent to 0.0.0.1 etc.)
                socket.inet_aton(SERVER)


                PORT = input("PORT: ")
        
                #if empty, default to 22
                if not PORT:
                    PORT = 22

                #used to verify the port is a number
                else:
                    PORT = int(PORT)


                USER = str(input("USERNAME: "))

                if USER.strip() == "":
                    print("Please enter a username.\n\n")
                    continue

                PASS = gp("PASSWORD: ")


                #attempts to connect with given data
                ((flag, client), user, message) = self.SSH_CONN(SERVER, PORT, USER, PASS)

                print(message + "\n")

                if message.strip() == "logon successful":
                    self.log(USER, "Connected to " + SERVER, "Successful")
                    login_attempt = False

                else:
                    self.log(USER, "Attempted connection to " + SERVER, "Failed", message)
                    continue

            except ValueError:
                #port is the only variable that isn't str, therefore is the only one that can return a ValueError
                print("Ports may only be integers. Please try again.\n\n")
                continue

            except OSError:
                #this is the error returned by inet_aton should the IP be incorrect
                print("Bad IP. Please try again.\n\n")
                continue

    
        exit_commands = ["exit", "close", "disconnect", "dc"]
        stdin = False #used to prevent an error if connection is closed before any commands are run

        while flag:
            #gets the command to get the current directory
            if not stdin:
                dir_command = self.get_dir(client)

                #gets the current directory (multiple commands must be run at once to work in other directories as paramiko ends the instance after the command is executed)
                stdin, stdout, stderr = client.exec_command(dir_command)
                current_dir = stdout.read().decode('utf8')
                current_dir = current_dir.strip()
        
            command = str(input(current_dir + ": "))

            #closes connection rather than attempting to run in shell
            if command.lower() in exit_commands:
                self.close_con(client, stdin, stdout, stderr, USER, SERVER)
                break

            stdin, stdout, stderr = client.exec_command(command)

            output = stdout.read().decode('utf8')
            err = stderr.read().decode('utf8')

            #checks the exit status of the command to see if it executed successfully
            if stdout.channel.recv_exit_status() == 0:
                print(output)
                self.log(USER, "Executed '" + command + "'", "Successful")

            else:
                print("ERR: " + err)
                self.log(USER, "Executed '" + command + "'", "Failed", err)