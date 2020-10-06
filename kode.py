import subprocess as sp
import pymysql
import pymysql.cursors
import random


caterer_ids =["148134290F","1B01EF5928","25C3698824","3692E7305E","48BB559AEA","72E84FE555","90EEF31A88","D08264D579","DD05ABD495","F97EDBB85C"]
ticket_nos=["6CFFABA","6A89913","7386FCC","814E10","8C0083","067D26C","6EF7355","3F529C9","827D4C6","7DAFD","27D01A5","19642C1","01284B1","6922DD","D4DB841","A0F3421","B887052B0","9148F6","3B2CC2C","0C8F4F3","E62DFB","10F3FF0","F3FF46"]


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
        meal_no=meal_no["MEAL_NO"]
        meal_no+1
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

def delete_passenger():
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

    query="DELETE FROM FLIES_ON WHERE PASSPORT_ID='%s'"%(row["p_id"])
    try:
        cur.execute(query)
        con.commit()
        print("Flight Emptied\n")
    except Exception as e:
        con.rollback()
        print("Flight Emptying Failed\n")
        print(">>>>",e)

    query="DELETE FROM LUGGAGE_BAG WHERE PASSPORT_ID='%s'"%(row["p_id"])
    try:
        cur.execute(query)
        con.commit()
        print("Luggage Deleted\n")
    except Exception as e:
        con.rollback()
        print("Luggage Deletion Failed\n")
        print(">>>>",e)

    query="DELETE FROM SUPPLIES_TO WHERE PASSPORT_ID='%s'"%(row["p_id"])
    try:
        cur.execute(query)
        con.commit()
        print("Meal Deleted\n")
    except Exception as e:
        con.rollback()
        print("Supplies_To Deletion Failed\n")
        print(">>>>",e)   

    query="DELETE FROM PASSENGER WHERE PASSPORT_ID='%s'"%(row["p_id"])
    try:
        cur.execute(query)
        con.commit()
        print("Passenger Deleted\n")
    except Exception as e:
        con.rollback()
        print("Pasenger Deletion Failed\n")
        print(">>>>",e)    

    return    

def get_outgoing_flight():
    try:
        # Takes emplyee details as input
        row = {}
        row["date"] = input("Enter required date in YYYY-MM-DD format: ")
        row["city"] = "Hyderabad"

        query = "SELECT * FROM FLIGHT WHERE DATE = '%s' AND DESTINATION <> '%s'" % (
            row["date"], row["city"])

        # print(query)
        cur.execute(query)
        result = cur.fetchone()
        if result is not None:
            print("FLIGHT_NO\tAIRLINE\t\tDESTINATION\tDATE\t\tSLOT\tTAKE_OFF_LOCATION\tBOARDING_TIME")
        else:
            print("No such entries found.")
        # print("yo")
        while result is not None:
            # no = tup[0]
            # print("%s\t" % (result['FLIGHT_NO']))
            print("%s\t%s\t%s\t\t%s\t%s\t%s\t\t%s\t" % (result['FLIGHT_NO'], result['AIRLINE'], result['DESTINATION'], result['DATE'], result['SLOT'], result['TAKE_OFF_LOCATION'], result['BOARDING_TIME']))
            result = cur.fetchone()
        # con.commit()

    except Exception as e:
        print("Failed to fetch data")
        print(">>>>>>>>>>>>>", e)

    return

def get_airline_by_count():
    row = {}
    row["date"] = input("Enter required date in YYYY-MM-DD format: ")
    row["count"] = input("Enter count above which you want to see flights: ")

    if not row["count"].isnumeric():
        print("Failed to fetch data")
        print(">>>>>>>>>>>>>", row["count"], "is not a numeric value")
        return
    query = "SELECT AIRLINE, COUNT(*) AS COUNT FROM FLIGHT WHERE DATE = '%s' GROUP BY AIRLINE HAVING COUNT(*) > '%s'" % (row["date"], row["count"])
    # print(query)
    try:
        cur.execute(query)
        result = cur.fetchone()
        if result is not None:
            print("FLIGHT_NO\tCOUNT")
        else:
            print("No such entries found.")
        # print("yo")
        while result is not None:
            # no = tup[0]
            # print("%s\t" % (result['AIRLINE']))
            print("%s\t%s\t" % (result['AIRLINE'], result['COUNT']))
            result = cur.fetchone()
    except Exception as e:
        print("Failed to fetch data")
        print(">>>>>>>>>>>>>", e)

    return  

def get_city_max():
    query = "SELECT DESTINATION AS CITY, COUNT(*) AS FLIGHTS FROM FLIGHT GROUP BY CITY ORDER BY FLIGHTS DESC LIMIT 1"
    # print(query)
    try:
        cur.execute(query)
        result = cur.fetchone()
        if result is not None:
            print("CITY\t\tFLIGHTS")
        else:
            print("No such entries found.")
        # print("yo")
        while result is not None:
            # no = tup[0]
            # print("%s\t" % (result['AIRLINE']))
            print("%s\t%s\t" % (result['CITY'], result['FLIGHTS']))
            result = cur.fetchone()
    except Exception as e:
        print("Failed to fetch data")
        print(">>>>>>>>>>>>>", e)

def find_passenger():
    row = {}
    row["no"] = input("Enter Passport ID of required passenger: ")

    query = "SELECT * FROM PASSENGER WHERE PASSPORT_ID = '%s'" % (row["no"])
    # print(query)
    try:
        cur.execute(query)
        result = cur.fetchone()
        if result is not None:
            print("%-20s%-20s%-20s%-20s%-20s%-20s" %("PASSPORT_ID", "TICKET_NUMBER", "GENDER", "FIRST_NAME", "LAST_NAME", "DOB"))
        else:
            print("No such entries found.")
        # print("yo")
        while result is not None:
            print("%-20s%-20s%-20s%-20s%-20s%-20s" % (result['PASSPORT_ID'], result['TICKET_NUMBER'], result['GENDER'], result['FIRST_NAME'], result['LAST_NAME'], result['DOB']))
            result = cur.fetchone()
    except Exception as e:
        print("Failed to fetch data")
        print(">>>>>>>>>>>>>", e)

    return 

def luggage_add(no,jk):
    print("Volume of Your Luggage Must be less than 30 sq units")
    l=int(input("Enter Length: "))
    b=int(input("Enter Breadth: "))
    h=int(input("Enter Height: "))
    if l*b*h>30:
        luggage_add(no,jk)
        return
    query="INSERT INTO LUGGAGE_BAG(PASSPORT_ID,BAG_NO,LENGTH,BREADTH,HEIGHT) VALUES ('%s','%s','%s','%s','%s')"%(jk,no,l,b,h)
    try:
        cur.execute(query)
        con.commit()
        print("Luggage Added!")
    except Exception as e:
        con.rollback()
        print("Luggage Insertion Failed\n")
        print(">>>>",e) 
    
    return  

def add_pasenger():
    row={}
    ticket_count=0
    try:
        query="SELECT * FROM PASSENGER WHERE TICKET_NUMBER='%s'"%(ticket_nos[ticket_count])
        cur.execute(query)
        count=cur.rowcount
        while count!=0:
            ticket_count=ticket_count+1
            query="SELECT * FROM PASSENGER WHERE TICKET_NUMBER='%s'"%(ticket_nos[ticket_count])
            cur.execute(query)
            count=cur.rowcount    
    except Exception as e:
        print(">>>>>>",e)

    dest=input("Enter Destination: ")
    start=input("Enter Start Location: ")
    dest=dest.lower()
    dest=dest.capitalize()
    start=start.lower()
    start=start.capitalize()

    query="SELECT * FROM FLIGHT WHERE TAKE_OFF_LOCATION='%s' AND DESTINATION='%s'"%(start,dest)    
    cur.execute(query)
    count=cur.rowcount
    if count==0:
        print("No Flight meets your requirements :(\n")
        return

    a=cur.fetchone()

    f_no=a["FLIGHT_NO"]
    b_time=a["BOARDING_TIME"]
    airline=a["AIRLINE"]
    
    try:
        query="SELECT * FROM FLIES_ON WHERE FLIGHT_NO = '%s'"%(f_no)
        cur.execute(query)
        count=cur.rowcount
        if count==150:
            print("The flight is already full. Sorry for the inconveniance")
            return
    except Exception as e:
        print(">>>>>>",e)

    row["p_id"]=input("Enter Your Passport ID: ")
    f_name=input("Enter First Name: ")
    l_name = input("Enter Last Name: ")
    gender = input("Enter Gender: ")
    gender=gender.upper()
    dob = input(" Enter DoB(YYYY-MM-DD): ")

    if dob<='2002-10-04':
        age="ADULT"
    else:
        age="MINOR"

    try:
        query="INSERT INTO PASSENGER (PASSPORT_ID,TICKET_NUMBER,GENDER,FIRST_NAME,LAST_NAME,DOB,AGE_GROUP) VALUES ('%s','%s','%s','%s','%s','%s','%s')"%(row["p_id"],ticket_nos[ticket_count],gender,f_name,l_name,dob,age)
        ticket_count=ticket_count+1
        cur.execute(query)
        con.commit()
        print("Passenger Created\n")
    except Exception as e:
        con.rollback()
        print("Passenger Insertion Failed\n")
        print(">>>>",e)
        return

    try:
        query="INSERT INTO FLIES_ON (PASSPORT_ID,FLIGHT_NO) VALUES('%s','%s')"%(row["p_id"],f_no)
        cur.execute(query)
        con.commit()
        print ("%s Flight:%s\n With Ticket_No:%s \n Boarding Time:%s Confirmed\n" %(airline,f_no,ticket_nos[ticket_count-1],b_time))

    except Exception as e:
        con.rollback()
        print("Flies_On Insertion Failed\n")
        print(">>>>",e)

    print("Enter Your Meal Preferences as Follows")
    print
    row["type"]=input("VEG/NON-VEG: ")
    row["type"] = row["type"].upper()

    row["class"] = input("LUXURY/ECONOMY: ")
    row["class"] = row["class"].upper()

    if (row["type"]!="VEG" and row["type"]!="NON_VEG") or (row["class"]!="LUXURY" and row["type"]!="ECONOMY"):
        print("Invalid Inputs, Please restrict your choice to above options next time")
        print
        return 

    caterer_no=random.randint(0,9)
    
    query="SELECT MAX(MEAL_NO) FROM MEAL_PACKAGE WHERE EMPLOYEE_ID='%s'"%(caterer_ids[caterer_no])
    cur.execute(query)
    meal_no=cur.fetchone()
    m_no=meal_no["MAX(MEAL_NO)"]
    m_no=m_no+1
    try:
        query="INSERT INTO MEAL_PACKAGE (EMPLOYEE_ID,MEAL_NO,CLASS,TYPE) VALUES ('%s' ,'%s','%s','%s') "%(caterer_ids[caterer_no],m_no,row["class"],row["type"])
        cur.execute(query)
        con.commit()
        print("Meal Confirmed\n")
    except Exception as e:
        con.rollback()
        print("Meal Package Insertion Failed\n")
        print(">>>>",e)
        
    try:
        query="INSERT INTO SUPPLIES_TO (EMPLOYEE_ID,MEAL_NO,PASSPORT_ID) VALUES ('%s','%s','%s')" %(caterer_ids[caterer_no],m_no,row["p_id"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Supplies_To Insertion Failed\n")
        print(">>>>",e)

    try:
        bag_no=int(input("How many bags do you want to register?: "))
        for x in range(1,int(bag_no+1)):
            print(x)
            luggage_add(x,row["p_id"])
    except Exception as e:
        print(">>>>",e)

    return
    
def get_below_avg():
    query = "CREATE VIEW YAM AS SELECT FLIGHT_NO, COUNT(*) AS YO FROM FLIES_ON GROUP BY FLIGHT_NO"
    # print(query)
    try:
        cur.execute(query)
    except Exception as e:
        print("Failed to fetch data")
        print(">>>>>>>>>>>>>", e)
        return

    query = "CREATE VIEW HUE AS SELECT FLIGHT_NO, COUNT(*) AS YO FROM FLIES_ON GROUP BY FLIGHT_NO HAVING  (SELECT AVG(YO) FROM YAM) > YO"
    try:
        cur.execute(query)
    except Exception as e:
        print("Failed to fetch data")
        print(">>>>>>>>>>>>>", e)
        return
    
    query = "SELECT AVG(YO) FROM YAM"
    try:
        cur.execute(query)
        result = cur.fetchone()
        while result is not None:
            # no = tup[0]
            # print("%s\t" % (result['AIRLINE']))
            print("Average no. of passengers per flight - %s\t" % (result['AVG(YO)']))
            result = cur.fetchone()
    except Exception as e:
        print("Failed to fetch data")
        print(">>>>>>>>>>>>>", e)
        return

    query = "SELECT HUE.FLIGHT_NO, AIRLINE, DESTINATION, DATE, SLOT, TAKE_OFF_LOCATION, BOARDING_TIME, YO AS PASSENGER_COUNT FROM HUE, FLIGHT WHERE HUE.FLIGHT_NO = FLIGHT.FLIGHT_NO"
    try:
        cur.execute(query)
        result = cur.fetchone()
        if result is not None:
            print("FLIGHT_NO\tAIRLINE\t\tDESTINATION\tDATE\t\tSLOT\tTAKE_OFF_LOCATION\tBOARDING_TIME\t\tPASSENGER_COUNT")
            print("")
        else:
            print("No such entries found.")
        # print("yo")
        while result is not None:
            print("%s\t%s\t%s\t%s\t%s\t%-24s%s\t%s" % (result['FLIGHT_NO'], result['AIRLINE'], result['DESTINATION'], result['DATE'], result['SLOT'], result['TAKE_OFF_LOCATION'], result['BOARDING_TIME'], result['PASSENGER_COUNT']))
            result = cur.fetchone()
            print("")
    except Exception as e:
        print("Failed to fetch data")
        print(">>>>>>>>>>>>>", e)
        return

    query = "DROP VIEW HUE"
    try:
        cur.execute(query)
    except Exception as e:
        print("Failed to drop temporary table")
        print(">>>>>>>>>>>>>", e)
        return

    query = "DROP VIEW YAM"
    try:
        cur.execute(query)
    except Exception as e:
        print("Failed to drop temporary table")
        print(">>>>>>>>>>>>>", e)
        return

def get_max_minors():
    query = "CREATE VIEW YO AS SELECT FLIGHT_NO, AGE_GROUP FROM FLIES_ON AS F, PASSENGER AS P WHERE F.PASSPORT_ID = P.PASSPORT_ID"
    # print(query)
    try:
        cur.execute(query)
    except Exception as e:
        print("Failed to fetch data")
        print(">>>>>>>>>>>>>", e)
        return

    query = "CREATE VIEW YAM AS SELECT * FROM YO WHERE AGE_GROUP = 'MINOR'"
    try:
        cur.execute(query)
    except Exception as e:
        print("Failed to fetch data")
        print(">>>>>>>>>>>>>", e)
        return

    query = "CREATE VIEW F AS SELECT FLIGHT_NO, COUNT(*) AS COUNT FROM YAM GROUP BY FLIGHT_NO"
    try:
        cur.execute(query)
    except Exception as e:
        print("Failed to fetch data")
        print(">>>>>>>>>>>>>", e)
        return

    query = "CREATE VIEW DED AS SELECT AIRLINE, COUNT FROM FLIGHT, F WHERE FLIGHT.FLIGHT_NO = F.FLIGHT_NO"
    try:
        cur.execute(query)
    except Exception as e:
        print("Failed to fetch data")
        print(">>>>>>>>>>>>>", e)
        return
    
    query = "SELECT AIRLINE, SUM(COUNT) FROM DED GROUP BY AIRLINE ORDER BY SUM(COUNT) DESC LIMIT 1"
    try:
        cur.execute(query)
        result = cur.fetchone()
        if result is not None:
            print("AIRLINE\t\tNO_OF_MINORS")
        else:
            print("No such entries found.")
        # print("yo")
        while result is not None:
            # no = tup[0]
            # print("%s\t" % (result['AIRLINE']))
            print("%s\t%s" % (result['AIRLINE'], result['SUM(COUNT)']))
            result = cur.fetchone()
    except Exception as e:
        print("Failed to fetch data")
        print(">>>>>>>>>>>>>", e)
        return

    query = "DROP VIEW YAM, YO, F, DED"
    try:
        cur.execute(query)
    except Exception as e:
        print("Failed to drop temporary table")
        print(">>>>>>>>>>>>>", e)
        return

    
        
def menu(ch):
    """
    Function that maps helper functions to option entered
    Add your function calls here
    """
    if(ch == 7):
        add_pasenger()
    if(ch == 8):
        change_meal_type()
    elif(ch == 9):
        delete_passenger()
    elif(ch == 1):
        get_outgoing_flight()
    elif(ch == 2):
        get_airline_by_count()
    elif(ch == 3):
        get_city_max()
    elif(ch == 4):
        find_passenger()
    elif(ch == 5):
        get_below_avg()
    elif(ch == 6):
        get_max_minors()
    else:
        print("Error:'%s' Invalid Option")


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
                print("4.Display passenger details search using PASSPORT ID") 
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
