import subprocess as sp
import pymysql
import pymysql.cursors
import random


caterer_ids =["148134290F","1B01EF5928","25C3698824","3692E7305E","48BB559AEA","72E84FE555","90EEF31A88","D08264D579","DD05ABD495","F97EDBB85C"]


def change_meal_type():
    row = {}
    row["p_id"] = input("Enter Passport Id of Passenger: ")
    query1="SELECT * FROM PASSENGER WHERE PASSPORT_ID = '%s'"%(row["p_id"])
    cur.execute(query1)
    count=cur.rowcount

    if count==0:
        print
        print("Given Passenger Doesn't Currently Exist")
        print 
        return
    
    query2="SELECT * FROM SUPPLIES_TO WHERE PASSPORT_ID = '%s'"%(row["p_id"])
    cur.execute(query2)
    count=cur.rowcount

    if count==0:
        print
        print("A New Meal Will be Added As Meal Doesn't Exist")
        print         

    print("Enter Your Preferences as Follows")
    print
    row["type"]=input("VEG/NON-VEG: ")
    row["type"] = row["type"].upper()

    row["class"] = input("LUXURY/ECONOMY: ")
    row["class"] = row["class"].upper()

    if (row["type"]!="VEG" and row["type"]!="NON_VEG") or (row["class"]!="LUXURY" and row["type"]!="ECONOMY"):
        print("Invalid Inputs, Please restrict your choice to above options next time")
        print
        return

    if count!=0:
        try:
            query="UPDATE MEAL_PACKAGE AS M SET CLASS = '%s' , TYPE = '%s' WHERE M.EMPLOYEE_ID=(SELECT EMPLOYEE_ID FROM SUPPLIES_TO   WHERE PASSPORT_ID='%s') AND M.MEAL_NO =( SELECT MEAL_NO FROM SUPPLIES_TO WHERE PASSPORT_ID='%s');"%(row["class"],row["type"],row["p_id"],row["p_id"])
            cur.execute(query)
            con.commit()

            print("Update Successful\n")
            print
        
        except Exception as e:
            con.rollback()
            print("Update Failed")
            print(">>>>>>",e)
    
    else:
        caterer_no=random.randint(0,9)
        query="SELECT MAX(MEAL_NO) FROM MEAL_PACKAGE WHERE EMPLOYEE_ID='%s'"%(caterer_ids[caterer_no])
        cur.execute(query)
        meal_no=cur.fetchone()
        meal_no=meal_no+1
        try:
            query="INSERT INTO MEAL_PACKAGE (EMPLOYEE_ID,MEAL_NO,CLASS,TYPE) VALUES ('%s' ,'%s','%s','%s') "%(caterer_ids[caterer_no],meal_no,row["class"],row["type"])
            cur.execute(query)
            con.commit()
        except Exception as e:
            con.rollback()
            print("Meal Package Insertion Failed\n")
            print(">>>>",e)
        
        try:
            query="INSERT INTO SUPPLIES_TO (EMPLOYEE_ID,MEAL_NO,PASSPORT_ID) VALUES (%s' ,'%s','%s')" %(caterer_ids[caterer_no],meal_no,row["p_id"])
            cur.execute(query)
            con.commit()
        except Exception as e:
            con.rollback()
            print("Supplies_To Insertion Failed\n")
            print(">>>>",e)
    return

def menu(ch):
    """
    Function that maps helper functions to option entered
    Add your function calls here
    """

    if(ch == 8):
        change_meal_type()
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
                              db='DNA_PROJECT',
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
