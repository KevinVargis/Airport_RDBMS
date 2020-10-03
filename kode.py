import subprocess as sp
import pymysql
import pymysql.cursors

def menu(ch):
    """
    Function that maps helper functions to option entered
    Add your function calls here
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
                
                '''
                    do we add the menu options for select * passenger, flight etc?
                '''
                print("1.View all out-going flights on a particular day")
                print("2.View all airlines with more than a given number of flights on a particular day")
                print("3.Show city with most incoming flights")
                print("4.Display passenger details search w/passenger name") 
                '''
                    should we do w/passport no instead?
                '''
                print("5.Display number of flights with below average number of passengers")
                print("6.Show airline flying the highest number of minors")
                print("7.Add a new passenger to a flight")
                print("8.Change the meal type of a passenger")
                '''
                    given func. requirement is - Update – Change meal type
                    we could do update passenger details instead also
                '''
                print("9.Delete passenger on a flight")
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
