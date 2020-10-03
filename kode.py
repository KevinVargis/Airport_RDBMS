import subprocess as sp
import pymysql
import pymysql.cursors

def menu(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch != 0):
        print("lmao")
    else:
        print("Error: Invalid Option")


while(True):   # main loop
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hard core username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='COMPANY',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("Enter 0 to Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 0:
                    break
                else:
                    menu(ch)
                    # print("lmao")
                    tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
