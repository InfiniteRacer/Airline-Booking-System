#==============================================================================================
        
#Airline Booking System By Sam Powsney
        
#==============================================================================================

#==============================================================================================

#Variable Database Section

#==============================================================================================

#Plane Models
plane1 = 'Medium narrow body'
plane1run = '8'
plane1range = '2650'
plane1cap = '180'
plane1minfirst = '8'
#=============
plane2 = 'Large narrow body'
plane2run = '7'
plane2range = '5600'
plane2cap = '220'
plane2minfirst = '10'
#=============
plane3 = 'Medium wide body'
plane3run = '5'
plane3range = '4050'
plane3cap = '406'
plane3minfirst = '14'

#UK Airports
ukairport1 = 'Liverpool John Lennon'
ukairport1code = 'LPL'
ukairport1codelwr = 'lpl'
#=============
ukairport2 = 'Bournemouth International'
ukairport2code = 'BOH'
ukairport2codelwr = 'boh'

#Overseas Airports
overseasairport1 = 'John F Kennedy International'
overseasairport1code = 'JFK'
overseasairport1codelwr = 'jfk'
overseasairport1lpl = '5326'
overseasairport1boh = '5486'
#===================
overseasairport2 = 'Paris-Orly'
overseasairport2code = 'ORY'
overseasairport2codelwr = 'ory'
overseasairport2lpl = '629'
overseasairport2boh = '379'
#===================
overseasairport3 = 'Adolfo Suarez Madrid- Barajas'
overseasairport3code = 'MAD'
overseasairport3codelwr = 'mad'
overseasairport3lpl = '1428'
overseasairport3boh = '1151'
#===================
overseasairport4 = 'Amsterdam Schiphol'
overseasairport4code = 'AMS'
overseasairport4codelwr = 'ams'
overseasairport4lpl = '526'
overseasairport4boh = '489'
#===================
overseasairport5 = 'Cairo International'
overseasairport5code = 'CAI'
overseasairport5codelwr = 'cai'
overseasairport5lpl = '3779'
overseasairport5boh = '3584'

#Saved Flight Database
flight1 = 'No Flight Scheduled.'
#====================
flight1uk = 'N/A'
#====================
flight1ukcode = 'N/A'
#====================
flight1ukcodelwr = 'N/A'
#====================
flight1os = 'N/A'
#====================
flight1oscode = 'N/A'
#====================
flight1oscodelwr = 'N/A'
#====================
flight1planechoice = 'N/A'
#====================
flight1standard = 'N/A'
#====================
flight1first = 'N/A'
#====================
flight2 = 'No Flight Scheduled.'
#====================
flight2uk = 'N/A'
#====================
flight2ukcode = 'N/A'
#====================
flight2ukcodelwr = 'N/A'
#====================
flight2os = 'N/A'
#====================
flight2oscode = 'N/A'
#====================
flight2oscodelwr = 'N/A'
#====================
flight2planechoice = 'N/A'
#====================
flight2standard = 'N/A'
#====================
flight2first = 'N/A'
#====================
flight3 = 'No Flight Scheduled.'
#====================
flight3uk = 'N/A'
#====================
flight3ukcode = 'N/A'
#====================
flight3ukcodelwr = 'N/A'
#====================
flight3os = 'N/A'
#====================
flight3oscode = 'N/A'
#====================
flight3oscodelwr = 'N/A'
#====================
flight3planechoice = 'N/A'
#====================
flight3standard = 'N/A'
#====================
flight3first = 'N/A'

#Current User Information (DELETE ALL THAT ARENT NEEDED AFTER SECTION OF THIS CODE IS FINSIHED)
usersignedin = 'N'
#====================
userlist = []
#====================
userfirstname = ''
#====================
userlastname = ''
#====================
useremail = ''
#====================
userpassword = ''

#==============================================================================================

#FIRST Start (ALL)

#==============================================================================================

def start():
    
    global mainmenuchoice
    
    def mainmenuchoice():
        
        print("Enter '1' to go to the Airline Portal")
        print("Enter '2' to go to the Customer Portal")
        print("Enter '3' to enter 'DANGER ZONE'")
        print("Enter '4' to Quit")
        
        print("")
        
        menuchoice=input("Enter option here: ")
        
        print("")
        
        if menuchoice == '1':
            
            mainmenucheck()
            
        elif menuchoice == '2':
            
            if usersignedin == 'N' or usersignedin == 'n':
            
                userserver()
                
            elif usersignedin == 'Y' or usersignedin == 'y':
                
                mainmenuuser()
                
            else:
                
                print("There has been an error on our side! Please try again...")
                
                print("")
                mainmenuchoice()
            
        elif menuchoice == '3':
            
            dangerzone()
            
        elif menuchoice == '4':
            
            quitsecmain()
            
        else:
            
            print("Invalid Input. Please try again...")
            print("")
            mainmenuchoice()
            
    print("Airline Profit & Booking Program - Created by Samuel Powsney")
    print("")
    
    print("First Time Instructions:")
    print("Please select an option below. Type the number and press enter.")
    print("")
    print("Airport Codes MUST be in ALL capitals.")
    print("")
    
    mainmenuchoice()
    
#==============================================================================================

#Check Main Menu STAFF VERSION

#==============================================================================================
    
def mainmenucheck():
    
    def mainmenuchecksec():
        
        global usersignedin
        
        print("To continue - you must be logged out of the last signed in user account.")
        changecheck=input("Would you like to continue? (y/n) ")
        print("")
        
        if changecheck == 'Y' or changecheck == 'y':
            
            usersignedin = 'N'
            
            mainmenu()
            
        elif changecheck == 'N' or changecheck == 'n':
            
            print("(You are still signed in!)")
            print("Returning you to the main menu...")
            print("")
            
            mainmenuchoice()
        
        else:
            
            print("Invalid Input! Please try again...")
            print("")
            
            mainmenuchecksec()
    
    if usersignedin == 'N' or usersignedin == 'n':
        
        mainmenu()
        
    elif usersignedin == 'Y' or usersignedin == 'y':
        
        mainmenuchecksec()
        
    else:
        
        print("Sorry! Something has gone wrong from our side, please try again...")
        print("")
        
        mainmenuchoice()
    
#==============================================================================================

#Main Menu STAFF VERSION

#==============================================================================================

def mainmenu():
    
    print("Main Menu:")
    
    print("Enter '1' To Enter Airport Details")
    print("Enter '2' To Enter Flight Details")
    print("Enter '3' To Enter Price Plan And Calculate Profit")
    print("Enter '4' To Clear Data")
    print("Enter '5' To View Save Slots")
    print("Enter '6' To Change Portal Type (Staff/User)")
    print("Enter '7' To Quit")
    
    print("")
    
    mainmenuchoices()
    
def mainmenuchoices():
    
    menuuser=input("Enter option here: ")
    print("")
    
    if menuuser == '1':
        
        airportdetails()
        
    elif menuuser == '2':
        
        flightdetails()
        
    elif menuuser == '3':
        
        priceplan()
        
    elif menuuser == '4':
        
        cleardata()
        
    elif menuuser == '5':
        
        viewsaveslot()
        
    elif menuuser == '6':
        
        mainmenuchoice()
        
    elif menuuser == '7':
        
        quitsec()
        
    else:
        
        print("Invalid Input! Please Try Again!")
        print("")
        
        mainmenuchoices()
        
#==============================================================================================

#Main Menu USER VERSION

#==============================================================================================
        
def mainmenuuser():
    
    print("Welcome Back, " +userfirstname+ "!")
    print("")
    print("Main Menu:")
    
    print("Enter '1' To View Flights Available")
    print("Enter '2' To Search Flights")
    print("Enter '3' To Book A Flight (COMING SOON...)")
    print("Enter '4' To Manage Flights (COMING SOON...)")
    print("Enter '5' To Manage Account (COMING SOON...)")
    print("Enter '6' To Change Portal Type (Staff/User)")
    print("Enter '7' To Sign Out")
    print("Enter '8' To Quit")
    
    print("")
    
    mainmenuuserchoices()
    
def mainmenuuserchoices():
    
    menuchoice=input("Enter option here: ")
    print("")
    
    if menuchoice == '1':
        
        availflights()
        
    elif menuchoice == '2':
        
        searchflights()
        
    elif menuchoice == '3':
        
        booking()
        
    elif menuchoice == '4':
        
        cancelbooking()
        
    elif menuchoice == '5':
        
        usermanagement()
        
    elif menuchoice == '6':
        
        mainmenuchoice()
        
    elif menuchoice == '7':
        
        signout()
        
    elif menuchoice == '8':
        
        quitsecuser()
        
    else:
        
        print("Invalid Input! Please try again...")
        print("")
        
        mainmenuuserchoices()
        
#==============================================================================================
        
#Sections Start Here
        
#==============================================================================================
        
#==============================================================================================
        
#Airport Details
        
#==============================================================================================
        
def airportdetails():
    
    global ukairportchoice
    global ukairportchoicecode
    
    def airportdetailsnext():
        
        global distance
        global overseasairportchoice
        global overseasairportchoicecode
        
        print("You have selected " +ukairportchoice+ ".")
        print("")
        
        overseasairportchoicenon=input("Enter Overseas Airport Code: ")
        
        if overseasairportchoicenon == overseasairport1code or overseasairportchoicenon == overseasairport1codelwr:
            
            overseasaiportchoicecode = overseasairport1code
            
            overseasairportchoice = overseasairport1
            
            if ukairportchoicecode == ukairport1code or ukairportchoicecode == ukairport1codelwr:
                
                distance = overseasairport1lpl
                
            elif ukairportchoicecode == ukairport2code or ukairportchoicecode == ukairport2codelwr:
                
                distance = overseasairport1boh
                
            else:
                
                print("Error! Please try again. Somethings gone wrong from our side...")
                
                print("")
                mainmenu()
            
            print("")
            airportdetailsfinal()
            
        elif overseasairportchoicenon == overseasairport2code or overseasairportchoicenon == overseasairport2codelwr:
            
            overseasairportchoicecode = overseasairport2code
            
            overseasairportchoice = overseasairport2
            
            if ukairportchoicecode == ukairport1code or ukairportchoicecode == ukairport1codelwr:
                
                distance = overseasairport2lpl
                
            elif ukairportchoicecode == ukairport2code or ukairportchoicecode == ukairport2codelwr:
                
                distance = overseasairport2boh
                
            else:
                
                print("Error! Please try again. Somethings gone wrong from our side...")
                
                print("")
                mainmenu()
            
            print("")
            airportdetailsfinal()
            
        elif overseasairportchoicenon == overseasairport3code or overseasairportchoicenon == overseasairport3codelwr:
            
            overseasairportchoicecode = overseasairport3code
            
            overseasairportchoice = overseasairport3
            
            if ukairportchoicecode == ukairport1code or ukairportchoicecode == ukairport1code:
                
                distance = overseasairport3lpl
                
            elif ukairportchoicecode == ukairport2code or ukairportchoicecode == ukairport2code:
                
                distance = overseasairport3boh
                
            else:
                
                print("Error! Please try again. Somethings gone wrong from our side...")
                
                print("")
                mainmenu()
            
            print("")
            airportdetailsfinal()
            
        elif overseasairportchoicenon == overseasairport4code or overseasairportchoicenon == overseasairport4codelwr:
            
            overseasairportchoicecode = overseasairport4code
            
            overseasairportchoice = overseasairport4
            
            if ukairportchoicecode == ukairport1code or ukairportchoicecode == ukairport1codelwr:
                
                distance = overseasairport4lpl
                
            elif ukairportchoicecode == ukairport2code or ukairportchoicecode == ukairport2codelwr:
                
                distance = overseasairport4boh
                
            else:
                
                print("Error! Please try again. Somethings gone wrong from our side...")
                
                print("")
                mainmenu()
            
            print("")
            airportdetailsfinal()
            
        elif overseasairportchoicenon == overseasairport5code or overseasairportchoicenon == overseasairport5codelwr:
            
            overseasairportchoicecode = overseasairport5code
            
            overseasairportchoice = overseasairport5
            
            if ukairportchoicecode == ukairport1code or ukairportchoicecode == ukairport1codelwr:
                
                distance = overseasairport5lpl
                
            elif ukairportchoicecode == ukairport2code or ukairportchoicecode == ukairport2codelwr:
                
                distance = overseasairport5boh
                
            else:
                
                print("Error! Please try again. Somethings gone wrong from our side...")
                
                print("")
                mainmenu()
            
            print("")
            airportdetailsfinal()
            
        else:
        
            print("Invalid Input. Please check the code and try again.")
            print("")
        
            mainmenu()
                
    def airportdetailsfinal():
        
        print("You have selected " +overseasairportchoice+ ".")
        print("")
        
        mainmenu()
    
    ukairportchoicenon=input("Enter UK Airport Code: ")
    
    if ukairportchoicenon == ukairport1code or ukairportchoicenon == ukairport1codelwr:
        
        ukairportchoicecode = ukairport1code
        
        ukairportchoice = ukairport1
        
        print("")
        airportdetailsnext()
        
    elif ukairportchoicenon == ukairport2code or ukairportchoicenon == ukairport2codelwr:
        
        ukairportchoicecode = ukairport2code
        
        ukairportchoice = ukairport2
        
        print("")
        airportdetailsnext()
        
    else:
        
        print("Invalid Input. Please check the code and try again.")
        print("")
        
        mainmenu()
        
#==============================================================================================
        
#Flight Details
        
#==============================================================================================
    
def flightdetails():
    
    global maxrange
    global capallstandard
    global planechoice
    global planechoicerun
    global planechoicerange
    global planechoicecap
    global planechoiceminfirst
    global firstclassseatsmax
    
    def flightdetailsnext():
        
        global firstclassseats
        global firstclassseatsnon
        global standardseatsnumb
        global firstclassseatsnon
        
        print("")
        
        firstclassseatsnon=float(input("Number of First Class Seats? "))
        
        if float(firstclassseatsnon) == 0:
            
            print("")
            flightdetailscalc()
            
        else:
            
            if float(firstclassseatsnon) < float(planechoiceminfirst):
                print("Invalid Input. There must be more than " +planechoiceminfirst+ " for this specific aircraft.")
                
                print("")
                mainmenu()
                
            elif float(firstclassseatsnon) > float(firstclassseatsmax):
                
                print("Invalid Input. There must be " +str(firstclassseatsmax)+ " or less first class seats for this aircraft type.")
                
                print("")
                mainmenu()
                
            else:
                
                print("")
                flightdetailscalc()
            
    def flightdetailscalc():
        
            global firstclassseats
            global standardseatsnumb
        
            firstclassseats = firstclassseatsnon
            standardseatsnumb = float(planechoicecap) - float(firstclassseats) * 2
            
            mainmenu()
    
    print("What type of aircraft would you like to be used?")
    
    print("Enter '1' for " +plane1+ ".")
    print("Enter '2' for " +plane2+ ".")
    print("Enter '3' for " +plane3+ ".")
    
    planechoicenon=input("Enter number: ")
    
    print("")
    
    if planechoicenon == '1':
        
        print("Run Cost for each Seat (Each 100km) - £" +plane1run)
        print("Maximum Flight Range - " +plane1range+ " KM")
        print("Maximum Amount of Seats - " +plane1cap)
        print("Minimum First Class Seats (If Applicable) - " +plane1minfirst)
        
        planechoice = plane1
        planechoicerun = plane1run
        planechoicerange = plane1range
        planechoicecap = plane1cap
        planechoiceminfirst = plane1minfirst
        
        maxrange = planechoicerange
        
        capallstandard = planechoicecap
        
        firstclassseatsmax = float(planechoicecap) / 2
        
        flightdetailsnext()
        
    elif planechoicenon == '2':
        
        print("Run Cost for each Seat (Each 100km) - £" +plane2run)
        print("Maximum Flight Range - " +plane2range+ " KM")
        print("Maximum Amount of Seats - " +plane2cap)
        print("Minimum First Class Seats (If Applicable) - " +plane2minfirst)
        
        planechoice = plane2
        planechoicerun = plane2run
        planechoicerange = plane2range
        planechoicecap = plane2cap
        planechoiceminfirst = plane2minfirst
        
        maxrange = planechoicerange
        
        capallstandard = planechoicecap
        
        firstclassseatsmax = float(planechoicecap) / 2
        
        flightdetailsnext()
        
    elif planechoicenon == '3':
        
        print("Run Cost for each Seat (Each 100km) - £" +plane3run)
        print("Maximum Flight Range - " +plane3range+ " KM")
        print("Maximum Amount of Seats - " +plane3cap)
        print("Minimum First Class Seats (If Applicable) - " +plane3minfirst)
        
        planechoice = plane3
        planechoicerun = plane3run
        planechoicerange = plane3range
        planechoicecap = plane3cap
        planechoiceminfirst = plane3minfirst
        
        maxrange = planechoicerange
        
        capallstandard = planechoicecap
        
        firstclassseatsmax = float(planechoicecap) / 2
        
        flightdetailsnext()
        
    else:
        
        print("Invalid Input. We cannot find that aircraft type, please try again.")
        print("")
        
        mainmenu()
        
#==============================================================================================
        
#Price Plan
        
#==============================================================================================
    
def priceplan():
    
    def priceplancheck1():
        
        if ukairportchoicecode == ukairport1code:
            
            priceplancheck2()
            
        elif ukairportchoicecode == ukairport2code:

            priceplancheck2()
            
        else:
            
            print("You need to enter all the details for the airports before continuing.")
            print("")
            mainmenu()
        
    def priceplancheck2():
        
        if planechoice == plane1:
            
            priceplancheck3()
            
        elif planechoice == plane2:
            
            priceplancheck3()
            
        elif planechoice == plane3:
            
            priceplancheck3()
            
        else:
            
            print("You need to enter all the details about the aircraft before continuing.")
            print("")
            mainmenu()
        
    def priceplancheck3():
        
        if firstclassseats == '':
            
            print("You need to enter all the details (Including About First Class) before continuing.")
            print("")
            mainmenu()
            
        else:
            
            priceplancheck4()
        
    def priceplancheck4():
        
        if maxrange == distance:
            
            print("You need to select a different aircraft! It isn't possible/unsafe to complete the route with the selected aircraft.")
            print("")
            print("Your Aircrafts Maxiumum Range is " +planechoicerange+ "km!")
            print("Your Selected Journey Length is " +distance+ "km!")
            
            print("")
            mainmenu()
            
        elif maxrange < distance:
            
            print("You need to select a different aircraft! It isn't possible to complete the route with the selected aircraft.")
            print("")
            print("Your Aircrafts Maxiumum Range is " +planechoicerange+ "km!")
            print("Your Selected Journey Length is " +distance+ "km!")
            
            print("")
            mainmenu()
            
        else:
            
            priceplannext()
        
    def priceplannext():
        
        global pricestandard
        global pricefirst

        pricestandard=input("Price of a Standard ticket: £")
        
        pricefirst=input("Price of a First Class ticket: £")
        
        priceplancalc()
        
    def priceplancalc():
        
        global flightcostperseat
        global flightcost
        global flightincome
        global flightprofit
        
        flightcostperseat = float(planechoicerun) * float(distance) / 100
        
        flightincome = float(firstclassseats) * float(pricefirst) + float(standardseatsnumb) * float(pricestandard)
        
        flightcost = float(flightcostperseat) * (float(firstclassseats) + float(standardseatsnumb))
        
        flightprofit = flightincome - flightcost
        
        priceplanfinal()
        
    def priceplanfinal():
        
        print("")
        print("Uk Airport - " +ukairportchoice)
        print("Overseas Airport - " +overseasairportchoice)
        print("Distance - " +distance+ " KM")
        print("Plane Type - " +planechoice)
        print("Maximum Flight Range - " +maxrange+ " KM")
        print("Flight Cost For Each Seat (Per 100KM) - £" +str(flightcostperseat))
        print("Capacity (If all are Standard) - " +planechoicecap)
        print("Number of First Class Seats - " +str(firstclassseats))
        print("Number of Standard Seats - " +str(standardseatsnumb))
        print("Standard Ticket Price - £" +pricestandard)
        print("First Ticket Price - £" +pricefirst)
        print("Flight Cost (Per Seat) - £" +str(flightcostperseat))
        print("Flight Cost - £" +str(flightcost))
        print("Flight Income - £" +str(flightincome))
        print("Flight Profit - £" +str(flightprofit))
        print("")
        
        priceplancheckpoint=input("Enter anything to continue: ")
        print("")
        
        savecheckpoint()
        
    def savecheckpoint():
        
        print("Enter '1' to return to the main menu.")
        print("Enter '2' to save a flight.")
        
        print("")
        saveflightcheckpoint=input("Enter choice here: ")
        print("")
        
        if saveflightcheckpoint == '1':
        
            mainmenu()
            
        elif saveflightcheckpoint == '2':
        
            saveflight()
            
        else:
            
            print("Invalid Input! Please try again...")
            print("")
            
            savecheckpoint()
            
    priceplancheck1()
    
#==============================================================================================
        
#Clear Data
        
#==============================================================================================
    
def cleardata():
    
    def cleardatafinal():
        
        global ukairportchoice
        global overseasairportchoice
        global distance
        global planechoice
        global maxrange
        global runcost
        global capallstandard
        global firstclassseats
        global standardseatsnumb
        global pricestandard
        global pricefirst
        global flightcostperseat
        global flightcost
        global flightincome
        global flightprofit
        
        ukairportchoice = ''
        overseasairportchoice = ''
        distance = ''
        planechoice = ''
        maxrange = ''
        runcost = ''
        capallstandard = ''
        firstclassseats = ''
        standardseatsnumb = ''
        pricestandard = ''
        pricefirst = ''
        flightcostperseat = ''
        flightcost = ''
        flightincome = ''
        flightprofit = ''
        
        print("Your data has now been cleared!")
        print("")
        
        mainmenu()
    
    clearuser=input("Are you sure you want to clear your current data? (y/n) ")
    
    if clearuser == 'y' or clearuser == 'Y':
        
        print("")
        cleardatafinal()
        
    elif clearuser == 'n' or clearuser == 'N':
        
        print("Operation stopped! Returning you back to the main menu...")
        print("")
        mainmenu()
        
    else:
        
        print("Invalid Input! Please try again.")
        print("")
        
        cleardata()
        
#==============================================================================================
        
#Quit Section (Staff)
        
#==============================================================================================
    
def quitsec():
    
    def quitsecfinal():
    
        print("You have ended the program! Your data has also been cleared automatically.")
        exit()
        
    quituser=input("Are you sure you want to quit? (y/n) ")
    
    if quituser == 'y' or quituser == 'Y':
        
        print("")
        quitsecfinal()
        
    elif quituser == 'n' or quituser == 'N':
        
        print("Operation stopped! Returning you back to the main menu...")
        print("")
        mainmenu()
        
    else:
        
        print("Invalid Input! Please try again.")
        print("")
        
        quitsec()
        
    quitsec()
    
#==============================================================================================
        
#Quit Section (User)
        
#==============================================================================================
    
def quitsecuser():
    
    def quitsecfinal():
    
        print("You have ended the program! Your data has also been cleared automatically.")
        exit()
        
    quituser=input("Are you sure you want to quit? (y/n) ")
    
    if quituser == 'y' or quituser == 'Y':
        
        print("")
        quitsecfinal()
        
    elif quituser == 'n' or quituser == 'N':
        
        print("Operation stopped! Returning you back to the main menu...")
        print("")
        mainmenuuser()
        
    else:
        
        print("Invalid Input! Please try again.")
        print("")
        
        quitsecuser()
        
    quitsec()
    
#==============================================================================================
        
#Quit Section (Main Menu)
        
#==============================================================================================
    
def quitsecmain():
    
    def quitsecfinal():
    
        print("You have ended the program! Your data has also been cleared automatically.")
        exit()
        
    quituser=input("Are you sure you want to quit? (y/n) ")
    
    if quituser == 'y' or quituser == 'Y':
        
        print("")
        quitsecfinal()
        
    elif quituser == 'n' or quituser == 'N':
        
        print("Operation stopped! Returning you back to the main menu...")
        print("")
        mainmenuchoice()
        
    else:
        
        print("Invalid Input! Please try again.")
        print("")
        
        quitsecmain()
        
    quitsec()
    
#==============================================================================================
        
#Save Flight
        
#==============================================================================================
    
def saveflight():
    
    print("Flight saving: " +ukairportchoice+ " - " +overseasairportchoice+ "")
    
    print("Current save slots: ")
    print("")
    
    print("Slot 1: " +flight1)
    print("Slot 2: " +flight2)
    print("Slot 3: " +flight3)
    
    print("")
    savecheckpoint=input("Which save slot would you like to use? (Enter '0' to cancel) ")
    print("")
    
    if savecheckpoint == '0':
        
        print("Canceled!")
        print("")
        
        mainmenu()
        
    elif savecheckpoint == '1':
        
        def next1():
            
            next2()
            
        def next1override():
            
            flight1checkpoint=input("Are you sure you would like to override the save slot? (y/n) ")
            print("")
            
            if flight1checkpoint == 'y' or flight1checkpoint == 'Y':
                
                next2()
                
            elif flight1checkpoint == 'n' or flight1checkpoint == 'N':
                
                print("Operation stopped!")
                print("")
                
                saveflight()
                
            else:
                
                print("Invalid Input! Please try again...")
                print("")
                
                next1override()
                
        def next2():
            
            global flight1
            global flight1uk
            global flight1ukcode
            global flight1ukcodelwr
            global flight1os
            global flight1oscode
            global flight1oscodelwr
            global flight1planechoice
            global flight1standard
            global flight1first
            
            flight1=(ukairportchoice+ " - " +overseasairportchoice+ "")
            
            flight1uk=ukairportchoice
            
            flight1ukcode=ukairportchoicecode
            
            if ukairportchoicecode == ukairport1code:
                
                flight1ukcodelwr=ukairport1codelwr
                
            elif ukairportchoicecode == ukairport2code:
                
                flight1ukcodelwr=ukairport2codelwr
                
            else:
                
                print("Sorry! Something has gone wrong from our side, please try again...")
                print("")
                
                mainmenu()
            
            flight1os=overseasairportchoice
            
            flight1oscode=overseasairportchoicecode
            
            if overseasairportchoicecode == overseasairport1code:
                
                flight1oscodelwr=overseasairport1codelwr
                
            elif overseasairportchoicecode == overseasairport2code:
                
                flight1oscodelwr=overseasairport2codelwr
                
            elif overseasairportchoicecode == overseasairport3code:
                
                flight1oscodelwr=overseasairport3codelwr
                
            elif overseasairportchoicecode == overseasairport4code:
                
                flight1oscodelwr=overseasairport4codelwr
                
            elif overseasairportchoicecode == overseasairport5code:
                
                flight1oscodelwr=overseasairport5codelwr
                
            else:
                
                print("Sorry! Something has gone wrong from our side, please try again...")
                print("")
                
                mainmenu()
            
            flight1planechoice=planechoice
            
            flight1standard=pricestandard
            
            flight1first=pricefirst
            
            next3()
            
        def next3():
            
            filehandlesection()
        
        if flight1 == 'No Flight Scheduled.':
            
            next1()
            
        else:
            
            next1override()
            
    elif savecheckpoint == '2':
        
        def next1():
            
            next2()
            
        def next1override():
            
            flight2checkpoint=input("Are you sure you would like to override the save slot? (y/n) ")
            print("")
            
            if flight2checkpoint == 'y' or flight2checkpoint == 'Y':
                
                next2()
                
            elif flight2checkpoint == 'n' or flight2checkpoint == 'N':
                
                print("Operation stopped!")
                print("")
                
                saveflight()
                
            else:
                
                print("Invalid Input! Please try again...")
                print("")
                
                next1override()
                
        def next2():
            
            global flight2
            global flight2uk
            global flight2ukcode
            global flight2ukcodelwr
            global flight2os
            global flight2oscode
            global flight2oscodelwr
            global flight2planechoice
            global flight2standard
            global flight2first
            
            flight2=(ukairportchoice+ " - " +overseasairportchoice+ "")
            
            flight2uk=ukairportchoice
    
            flight2ukcode=ukairportchoicecode
            
            if ukairportchoicecode == ukairport1code:
                
                flight2ukcodelwr=ukairport1codelwr
                
            elif ukairportchoicecode == ukairport2code:
                
                flight2ukcodelwr=ukairport2codelwr
                
            else:
                
                print("Sorry! Something has gone wrong from our side, please try again...")
                print("")
                
                mainmenu()
            
            flight2os=overseasairportchoice
            
            flight2oscode=overseasairportchoicecode
            
            if overseasairportchoicecode == overseasairport1code:
                
                flight2oscodelwr=overseasairport1codelwr
                
            elif overseasairportchoicecode == overseasairport2code:
                
                flight2oscodelwr=overseasairport2codelwr
                
            elif overseasairportchoicecode == overseasairport3code:
                
                flight2oscodelwr=overseasairport3codelwr
                
            elif overseasairportchoicecode == overseasairport4code:
                
                flight2oscodelwr=overseasairport4codelwr
                
            elif overseasairportchoicecode == overseasairport5code:
                
                flight2oscodelwr=overseasairport5codelwr
                
            else:
                
                print("Sorry! Something has gone wrong from our side, please try again...")
                print("")
                
                mainmenu()
            
            flight2planechoice=planechoice
            
            flight2standard=pricestandard
            
            flight2first=pricefirst
            
            next3()
            
        def next3():
            
            filehandlesection()
        
        if flight2 == 'No Flight Scheduled.':
            
            next1()
            
        else:
            
            next1override()
            
    elif savecheckpoint == '3':
        
        def next1():
            
            next2()
            
        def next1override():
            
            flight3checkpoint=input("Are you sure you would like to override the save slot? (y/n) ")
            print("")
            
            if flight3checkpoint == 'y' or flight3checkpoint == 'Y':
                
                next2()
                
            elif flight3checkpoint == 'n' or flight3checkpoint == 'N':
                
                print("Operation stopped!")
                print("")
                
                saveflight()
                
            else:
                
                print("Invalid Input! Please try again...")
                print("")
                
                next1override()
                
        def next2():
            
            global flight3
            global flight3uk
            global flight3ukcode
            global flight3ukcodelwr
            global flight3os
            global flight3oscode
            global flight3oscodelwr
            global flight3planechoice
            global flight3standard
            global flight3first
            
            flight3=(ukairportchoice+ " - " +overseasairportchoice+ "")
            
            flight3uk=ukairportchoice
        
            flight3ukcode=ukairportchoicecode
            
            if ukairportchoicecode == ukairport1code:
                
                flight3ukcodelwr=ukairport1codelwr
                
            elif ukairportchoicecode == ukairport2code:
                
                flight3ukcodelwr=ukairport2codelwr
                
            else:
                
                print("Sorry! Something has gone wrong from our side, please try again...")
                print("")
                
                mainmenu()
            
            flight3os=overseasairportchoice
            
            flight3oscode=overseasairportchoicecode
            
            if overseasairportchoicecode == overseasairport1code:
                
                flight3oscodelwr=overseasairport1codelwr
                
            elif overseasairportchoicecode == overseasairport2code:
                
                flight3oscodelwr=overseasairport2codelwr
                
            elif overseasairportchoicecode == overseasairport3code:
                
                flight3oscodelwr=overseasairport3codelwr
                
            elif overseasairportchoicecode == overseasairport4code:
                
                flight3oscodelwr=overseasairport4codelwr
                
            elif overseasairportchoicecode == overseasairport5code:
                
                flight3oscodelwr=overseasairport5codelwr
                
            else:
                
                print("Sorry! Something has gone wrong from our side, please try again...")
                print("")
                
                mainmenu()
        
            flight3planechoice=planechoice
            
            flight3standard=pricestandard
            
            flight3first=pricefirst
            
            next3()
            
        def next3():
            
            filehandlesection()
        
        if flight3 == 'No Flight Scheduled.':
            
            next1()
            
        else:
            
            next1override()
        
    else:
        
        print("Invalid Input! Please try again...")
        print("")
        
        saveflight()
        
#==============================================================================================
        
#View Saved Flights & Available Flights
        
#==============================================================================================
        
def viewsaveslot():
    
    print("Flight Slot 1: " +flight1)
    print("Flight Slot 2: " +flight2)
    print("Flight Slot 3: " +flight3)
    
    print("")
    mainmenu()
    
def availflights():
    
    print("Current Available Flights:")
    print("")
    
    print("-----------------------------------------------------------")
    print("")
    
    print("FROM:")
    print(flight1uk+ " (" +flight1ukcode+ ")")
    print("TO:")
    print(flight1os+ " (" +flight1oscode+ ")")
    print("")
    print("Plane Model - " +flight1planechoice)
    print("")
    print("Economy Class - Starting at: £" +flight1standard)
    print("First Class - Starting at: £" +flight1first)
    
    print("")
    print("-----------------------------------------------------------")
    print("")
    
    print("FROM:")
    print(flight2uk+ " (" +flight2ukcode+ ")")
    print("TO:")
    print(flight2os+ " (" +flight2oscode+ ")")
    print("")
    print("Plane Model - " +flight2planechoice)
    print("")
    print("Economy Class - Starting at: £" +flight2standard)
    print("First Class - Starting at: £" +flight2first)
    
    print("")
    print("-----------------------------------------------------------")
    print("")
    
    print("FROM:")
    print(flight3uk+ " (" +flight3ukcode+ ")")
    print("TO:")
    print(flight3os+ " (" +flight3oscode+ ")")
    print("")
    print("Plane Model - " +flight3planechoice)
    print("")
    print("Economy Class - Starting at: £" +flight3standard)
    print("First Class - Starting at: £" +flight3first)
    
    print("")
    print("-----------------------------------------------------------")
    print("")
    
    viewflightscheckpoint=input("Enter anything to continue: ")
    print("")
    
    mainmenuuser()
    
#==============================================================================================
        
#Search Flights
        
#==============================================================================================

def searchflights():
    
    def searchflightsfirst():
        
        global searchuk
        global searchos
        
        searchuk=input("Departing Airport Code? ")
        searchos=input("Arrival Airport Code? ")
        
        searchflightsadvcheck()
    
    def searchflightsadvcheck():
        
        global advyn
        
        searchadv=input("Advanced Search? (y/n) ")
        print("")
        
        if searchadv == 'y' or searchadv == 'Y':
        
            print("Advanced Search Selected!")
            print("")
            
            advyn = '1'
            
            searchflightsadv()
        
        elif searchadv == 'n' or searchadv == 'N':
            
            print("Advance Search Skipped!")
            print("")
            
            print("Current Available Flights:")
            print("")
            
            advyn = '2'
        
            searchflightssec()
        
        else:
        
            print("Invalid Input! Please try again...")
            print("")
            
            searchflightsadvcheck()
            
    def searchflightsadv():
        
        global advoption
        global filterop
        global stanmax
        global firstmax
        global filterplane
        
        print("Enter '1' to Filter: Price")
        print("Enter '2' to Filter: Plane Model")
        print("Enter '3' to Cancel")
        
        print("")
        
        advchoice=input("Enter Option Number Here: ")
        print("")
        
        if advchoice == '1':
            
            print("Enter '1' to Filter: Standard Prices")
            print("Enter '2' to Filter: First Class Prices")
            print("Enter '3' to Cancel")
            print("")
            
            filteroption=input("Enter Option Number Here: ")
            print("")
            
            if filteroption == '1':
                
                stanmax=input("Enter filter price for Standard Class: ")
                
                print("")
                
                advoption = '11'
                
            elif filteroption == '2':
                
                firstmax=input("Enter filter price for First Class: ")
                
                print("")
                
                advoption = '12'
                
            elif filteroption == '4':
                
                print("Advanced Search Stopped!")
                print("")
                searchflightssec()
                
            else:
                
                print("Invalid Input, please try again...")
                print("")
                
                searchflightsadv()
                
        elif advchoice == '2':
            
            print("Enter '1' for: " +plane1)
            print("Enter '2' for: " +plane2)
            print("Enter '3' for: " +plane3)
            print("Enter '4' to Cancel")
            print("")
            
            filteroptionplane=input("Enter Option Number Here: ")
            print("")
            
            if filteroptionplane == '1':
                
                advoption = '21'
                filterplane = plane1
                
                print("Current Available Flights:")
                print("")
        
                searchflightssec()
            
            elif filteroptionplane == '2':
                
                advoption = '21'
                filterplane = plane2
                
                print("Current Available Flights:")
                print("")
        
                searchflightssec()
            
            elif filteroptionplane == '3':
                
                advoption = '21'
                filterplane = plane3
                
                print("Current Available Flights:")
        
                searchflightssec()
            
            elif filteroptionplane == '4':
                
                print("Advanced Search Stopped!")
                searchflightssec()
            
            else:
                
                print("Invalid Input, please try again...")
                
                searchflightsadv()
        
        elif advchoice == '3':
            
            print("Advanced Search Stopped!")
            print("")
            searchflightssec()
        
        else:
            
            print("Invalid Input, please try again...")
            print("")
        
        print("Current Available Flights:")
        print("")
        
        searchflightssec()
            
    def searchflightssec():
        
        if searchuk == ukairport1code or searchuk == ukairport1codelwr:

            if searchos == overseasairport1code or searchos == overseasairport1codelwr:
                
                if flight1ukcode == searchuk and flight1oscode == searchos or flight1ukcodelwr == searchuk and flight1oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight2ukcode == searchuk and flight2oscode == searchos or flight2ukcodelwr == searchuk and flight2oscodelwr == searchos:
                        
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight3ukcode == searchuk and flight3oscode == searchos or flight3ukcodelwr == searchuk and flight3oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                else:
                    
                    flightsearchno()
                    
            elif searchos == overseasairport2code or searchos == overseasairport2codelwr:
                
                if flight1ukcode == searchuk and flight1oscode == searchos or flight1ukcodelwr == searchuk and flight1oscodelwr == searchos:
                        
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                    
                elif flight2ukcode == searchuk and flight2oscode == searchos or flight2ukcodelwr == searchuk and flight2oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight3ukcode == searchuk and flight3oscode == searchos or flight3ukcodelwr == searchuk and flight3oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                else:
                    
                    flightsearchno()
                    
            elif searchos == overseasairport3code or searchos == overseasairport3codelwr:
                
                if flight1ukcode == searchuk and flight1oscode == searchos or flight1ukcodelwr == searchuk and flight1oscodelwr == searchos:
                        
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight2ukcode == searchuk and flight2oscode == searchos or flight2ukcodelwr == searchuk and flight2oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight3ukcode == searchuk and flight3oscode == searchos or flight3ukcodelwr == searchuk and flight3oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                else:
                    
                    flightsearchno()
                    
            elif searchos == overseasairport4code or searchos == overseasairport4codelwr:
                
                if flight1ukcode == searchuk and flight1oscode == searchos or flight1ukcodelwr == searchuk and flight1oscodelwr == searchos:
                        
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight2ukcode == searchuk and flight2oscode == searchos or flight2ukcodelwr == searchuk and flight2oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight3ukcode == searchuk and flight3oscode == searchos or flight3ukcodelwr == searchuk and flight3oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                else:
                    
                    flightsearchno()
                    
            elif searchos == overseasairport5code or searchos == overseasairport5codelwr:
                
                if flight1ukcode == searchuk and flight1oscode == searchos or flight1ukcodelwr == searchuk and flight1oscodelwr == searchos:
                        
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight2ukcode == searchuk and flight2oscode == searchos or flight2ukcodelwr == searchuk and flight2oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight3ukcode == searchuk and flight3oscode == searchos or flight3ukcodelwr == searchuk and flight3oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                else:
                    
                    flightsearchno()
                    
            else:
                
                flightsearchno()
                    
        elif searchuk == ukairport2code or searchuk == ukairport2codelwr:
            
            if searchos == overseasairport1code or searchos == overseasairport1codelwr:
                
                if flight1ukcode == searchuk and flight1oscode == searchos or flight1ukcodelwr == searchuk and flight1oscodelwr == searchos:
                        
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight2ukcode == searchuk and flight2oscode == searchos or flight2ukcodelwr == searchuk and flight2oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight3ukcode == searchuk and flight3oscode == searchos or flight3ukcodelwr == searchuk and flight3oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                else:
                    
                    flightsearchno()
                    
            elif searchos == overseasairport2code or searchos == overseasairport2codelwr:
                
                if flight1ukcode == searchuk and flight1oscode == searchos or flight1ukcodelwr == searchuk and flight1oscodelwr == searchos:
                        
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight2ukcode == searchuk and flight2oscode == searchos or flight2ukcodelwr == searchuk and flight2oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight3ukcode == searchuk and flight3oscode == searchos or flight3ukcodelwr == searchuk and flight3oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                else:
                    
                    flightsearchno()
                    
            elif searchos == overseasairport3code or searchos == overseasairport3codelwr:
                
                if flight1ukcode == searchuk and flight1oscode == searchos or flight1ukcodelwr == searchuk and flight1oscodelwr == searchos:
                        
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight2ukcode == searchuk and flight2oscode == searchos or flight2ukcodelwr == searchuk and flight2oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight3ukcode == searchuk and flight3oscode == searchos or flight3ukcodelwr == searchuk and flight3oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                else:
                    
                    flightsearchno()
                    
            elif searchos == overseasairport4code or searchos == overseasairport4codelwr:
                
                if flight1ukcode == searchuk and flight1oscode == searchos or flight1ukcodelwr == searchuk and flight1oscodelwr == searchos:
                        
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight2ukcode == searchuk and flight2oscode == searchos or flight2ukcodelwr == searchuk and flight2oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight3ukcode == searchuk and flight3oscode == searchos or flight3ukcodelwr == searchuk and flight3oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                else:
                    
                    flightsearchno()
                    
            elif searchos == overseasairport5code or searchos == overseasairport5codelwr:
                
                if flight1ukcode == searchuk and flight1oscode == searchos or flight1ukcodelwr == searchuk and flight1oscodelwr == searchos:
                        
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight2ukcode == searchuk and flight2oscode == searchos or flight2ukcodelwr == searchuk and flight2oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                elif flight3ukcode == searchuk and flight3oscode == searchos or flight3ukcodelwr == searchuk and flight3oscodelwr == searchos:
                    
                    if advyn == '1':
                    
                        if advoption == '11':
                                
                            if flight1standard < stanmax:
                                
                                flightsearchno()
                            
                        elif advoption == '12':
                            
                            if flight1first < firstmax:
                                
                                flightsearchno()
                        
                        elif advoption == '21':
                            
                            if flight1planechoice == filterplane:
                                
                                print("")
                                
                            else:
                                
                                flightsearchno()
                            
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first) 
                        
                        flightsearchagain()
                    
                    elif advyn == '2':
                        
                        print("FROM:")
                        print(flight1uk+ " (" +flight1ukcode+ ")")
                        print("TO:")
                        print(flight1os+ " (" +flight1oscode+ ")")
                        print("")
                        print("Plane Model - " +flight1planechoice)
                        print("")
                        print("Economy Class - Starting at: £" +flight1standard)
                        print("First Class - Starting at: £" +flight1first)
                        
                        flightsearchagain()
                        
                    else:
                        
                        print("Sorry! Something has gone wrong from our side, please try again...")
                        print("")
                        
                        mainmenuuser()
                    
                else:
                    
                    flightsearchno()
                    
        else:
            
            flightsearchno()

    print("Search Flights: ")
    print("")
    
    print("NOTE - Please Enter a VALID Airport Code!")
    print("")
    
    searchflightsfirst()
    
def flightsearchno():
    
    if advyn == '2':
        
        print("No Aircraft has been scheduled to leave from your selected airports (" +searchuk+ " & " +searchos+ ") according to our data.")
        print("")
        
        mainmenuuser()
        
    elif advyn == '1':
        
        print("No Aircraft has been scheduled to leave from your selected airports (" +searchuk+ " & " +searchos+ ") with your selected search parameters.")
        print("")
        
        mainmenuuser()
        
    else:
        
        print("Sorry! Something has gone wrong from our side, please try again...")
        print("")
        
        mainmenuuser()

def flightsearchagain():
    
    print("")
    checksearchagain=input("Would you like to do another search? (y/n) ")
    print("")
    
    if checksearchagain == 'y' or checksearchagain == 'Y':
        
        searchuk = ''
        searchos = ''
        
        searchflights()
        
    elif checksearchagain == 'n' or checksearchagain == 'N':
        
        print("Returning you back to the main menu...")
        print("")
        
        mainmenuuser()
        
    else:
        
        print("Invalid Input! Please try again...")
        print("")
        
        flightsearchagain()
    
#==============================================================================================
        
#File Air-Routes Database
        
#==============================================================================================
    
def filehandlesection():
    
    file = open('airlineflights.txt','w')
    file.write("Saved Flights:""\n")
    file.write("" "\n")
    
    file.write("FROM:""\n")
    file.write(flight1uk+ " (" +flight1ukcode+ ") \n")
    file.write("" "\n")
    file.write("TO:""\n")
    file.write(flight1os+ " (" +flight1oscode+ ") \n")
    file.write("" "\n")
    file.write("Aircraft model = " +flight1planechoice+ "\n")
    file.write("" "\n")
    file.write("Economy Ticket Price = £" +flight1standard+ "\n")
    file.write("First Class Ticket Price = £" +flight1first+ "\n")
    file.write("" "\n")
    file.write("-------------------------------------------""\n")
    
    file.write("" "\n")
    file.write("FROM:""\n")
    file.write(flight2uk+ " (" +flight2ukcode+ ") \n")
    file.write("" "\n")
    file.write("TO:""\n")
    file.write(flight2os+ " (" +flight2oscode+ ") \n")
    file.write("" "\n")
    file.write("Aircraft model = " +flight2planechoice+ "\n")
    file.write("" "\n")
    file.write("Economy Ticket Price = £" +flight2standard+ "\n")
    file.write("First Class Ticket Price = £" +flight2first+ "\n")
    file.write("" "\n")
    file.write("-------------------------------------------""\n")
    
    file.write("" "\n")
    file.write("FROM:""\n")
    file.write(flight3uk+ " (" +flight3ukcode+ ") \n")
    file.write("" "\n")
    file.write("TO:""\n")
    file.write(flight3os+ " (" +flight3oscode+ ") \n")
    file.write("" "\n")
    file.write("Aircraft model = " +flight3planechoice+ "\n")
    file.write("" "\n")
    file.write("Economy Ticket Price = £" +flight3standard+ "\n")
    file.write("First Class Ticket Price = £" +flight3first+ "\n")
    file.write("" "\n")
    file.write("-------------------------------------------""\n")
    
    file.close()
    
    print("The database file has also been updated! Please completely close the file and open it again for the updated version.")
    
    print("")
    mainmenu()
    
#==============================================================================================
        
#File Clear
        
#==============================================================================================
    
def fileclear():
    
    print("Please Note - Your data will NOT be cleared, only the file will be reset to its default state.")
    print("")
    
    fileclear2()
    
def fileclear2():
    
    checkfileclear=input("Are you sure you want to clear the file? (y/n) ")
    print("")
    
    if checkfileclear == 'y' or checkfileclear == 'Y':
        
        fileclear3()
        
    elif checkfileclear == 'n' or checkfileclear == 'N':
        
        print("Clear stopped! Returning you back to the main menu...")
        print("")
        
        dangerzone()
        
    else:
        
        print("Invalid Input! Please try again...")
        print("")
        
        fileclear2()
        
def fileclear3():
    
    file = open('airlineflights.txt','w')
    file.write("Saved Flights:""\n")
    file.write("" "\n")
    
    file.write("FROM:""\n")
    file.write("N/A \n")
    file.write("" "\n")
    file.write("TO:""\n")
    file.write("N/A \n")
    file.write("" "\n")
    file.write("Aircraft model = N/A \n")
    file.write("" "\n")
    file.write("Economy Ticket Price = £N/A \n")
    file.write("First Class Ticket Price = £N/A \n")
    file.write("" "\n")
    file.write("-------------------------------------------""\n")
    
    file.write("" "\n")
    file.write("FROM:""\n")
    file.write("N/A \n")
    file.write("" "\n")
    file.write("TO:""\n")
    file.write("N/A \n")
    file.write("" "\n")
    file.write("Aircraft model = N/A \n")
    file.write("" "\n")
    file.write("Economy Ticket Price = £N/A \n")
    file.write("First Class Ticket Price = £N/A \n")
    file.write("" "\n")
    file.write("-------------------------------------------""\n")

    file.write("" "\n")
    file.write("FROM:""\n")
    file.write("N/A \n")
    file.write("" "\n")
    file.write("TO:""\n")
    file.write("N/A \n")
    file.write("" "\n")
    file.write("Aircraft model = N/A \n")
    file.write("" "\n")
    file.write("Economy Ticket Price = £N/A \n")
    file.write("First Class Ticket Price = £N/A \n")
    file.write("" "\n")
    file.write("-------------------------------------------""\n")
    
    file.close()
    
    print("The database file has been cleared and set back to its default! Please completely close the file and open it again for the updated version.")
    
    print("")
    dangerzone()
    
#==============================================================================================
        
#User Create & Sign In (IN PROGRESS)
        
#==============================================================================================
    
def userserver():
    
    def usercreate():
        
        global newuserfirstname
        global newuserlastname
        global newuserusername
        global newuserpassword
        global newuseremail
        
        print("Welcome new user!")
        print("Please follow the questions below to continue...")
        print("")
        print("NOTE - Enter 'N' on ANY question to cancel and return to the main menu.")
        print("(*) = REQUIRED QUESTION")
        print("")
        
        newuserfirstname=input("(*)First Name? ")
        
        if newuserfirstname == 'N' or newuserfirstname == 'n':
            
            print("")
            print("Sign Up Canceled!")
            
            print("")
            usersigninmenu()
            
        elif newuserfirstname == '':
            
            print("")
            print("You left the question blank! Please try again...")
            
            print("")
            usersigninmenu()
        
        newuserlastname=input("(*)Last Name? ")
        
        if newuserlastname == 'N' or newuserlastname == 'n':
            
            print("")
            print("Sign Up Canceled!")
            
            print("")
            usersigninmenu()
            
        elif newuserlastname == '':
            
            print("")
            print("You left the question blank! Please try again...")
            
            print("")
            usersigninmenu()
        
        newuserusername=input("(*)Username? ")
        
        if newuserusername == 'N' or newuserusername == 'n':
            
            print("")
            print("Sign Up Canceled!")
            
            print("")
            usersigninmenu()
            
        elif newuserusername == '':
            
            print("")
            print("You left the question blank! Please try again...")
            
            print("")
            usersigninmenu()
        
        newuserpassword=input("(*)Password? ")
        
        if newuserpassword == 'N' or newuserpassword == 'n':
            
            print("")
            print("Sign Up Canceled!")
            
            print("")
            usersigninmenu()
            
        elif newuserpassword == '':
            
            print("")
            print("You left the question blank! Please try again...")
            
            print("")
            usersigninmenu()
        
        newuseremail=input("Email Address (Enter 'N' to skip)? ")
        
        if newuseremail == 'N' or newuseremail == 'n':
            
            print("")
            print("Email Skipped...")
            
            newusermenu()
            
        elif newuseremail == '':
            
            print("")
            print("You left the question blank! Please try again...")
            
            print("")
            usersigninmenu()
            
        else:
            
            newusermenu()
            
    def newusermenu():
        
        global userlist
        
        userdatabase = open('userdatabase.txt', 'a+')
        
        userdatabase.write(newuserfirstname+ ", ")
        userdatabase.write(newuserlastname+ ", ")
        userdatabase.write(newuserusername+ ", ")
        userdatabase.write(newuserpassword+ ", ")
        
        if newuseremail == 'n' or newuseremail == 'N':
            
            userdatabase.write("N/A")
            print("")
            
        else:
            
            print("")
            userdatabase.write(newuseremail)
        
        userdatabase.write("\n")
        
        userdatabase.close()
        
        print("Thank you for signing up " +newuserfirstname+ "!")
        print("You can now start booking flights and earning points! (Points coming soon...)")
        print("")
        print("Please sign in from the Main Menu!")
        print("")
        
        userserver()
        
    def usersignin():
        
        userdatabase = open("userdatabase.txt", "w")
        
        print("Welcome Back User!")
        print("")
        print("NOTE - Enter 'N' on ANY question to cancel and return to the main menu.")
        print("(*) = REQUIRED QUESTION")
        print("")
        
        oldusername=input("(*)Username? ")
        
        if oldusername == 'N' or oldusername == 'n':
            
            print("")
            print("Sign In Canceled!")
            
            print("")
            usersigninmenu()
            
        elif oldusername == '':
            
            print("")
            print("You left this question blank! Please try again...")
            
            print("")
            usersigninmenu()
        
        #if statement checking for match HERE
        
        oldpassword=input("(*)Password? ")
        
        if oldpassword == 'N' or oldpassword == 'n':
            
            print("")
            print("Sign In Canceled!")
            
            print("")
            usersigninmenu()
            
        elif oldpassword == '':
            
            print("")
            print("You left this question blank! Please try again...")
            
            print("")
            usersigninmenu()
        
        #if statement checking for match HERE
        
        print("")
        
        global usersignedin
        usersignedin = 'Y'
        
        userdatabase.close()
        
        mainmenuuser()
    
    def usersigninmenu():
    
        print("Main Menu:")
        
        print("Enter '1' To Create An Account")
        print("Enter '2' To Sign In To An Account")
        print("Enter '3' To Go Back To Main Menu (Final)")
        
        print("")
        
        usersigninsec()
    
    def usersigninsec():
    
        menuchoice=input("Enter option here: ")
        print("")
        
        if menuchoice == '1':
            
            usercreate()
            
        elif menuchoice == '2':
            
            usersignin()
            
        elif menuchoice == '3':
            
            print("Returining back to the main menu...")
            
            print("")
            mainmenuchoice()
            
        else:
            
            print("Invalid Input! Please try again...")
            print("")
            
            usersigninsec()
            
    usersigninmenu()
    
#==============================================================================================
        
#User Sign Out
        
#==============================================================================================
    
def signout():
    
    def signoutfinal():
        
        global userfirstname
        global userlastname
        global useremail
        global userpassword
        global usersignedin
        
        userfirstname = ''
        userlastname = ''
        useremail = ''
        userpassword = ''
        usersignedin = 'N'
        
        print("Sign Out Complete!")
        
        print("")
        userserver()
    
    checksignout=input("Are you sure you want to sign out? (y/n) ")
    print("")
    
    if checksignout == 'y' or checksignout == 'Y':
        
        signoutfinal()
        
    elif checksignout == 'n' or checksignout == 'N':
        
        print("Sign out stopped! Returning you back to the main menu...")
        print("")
        
        mainmenuuser()
        
    else:
        
        print("Invalid Input! Please try again...")
        print("")
        
        signout()
    
#==============================================================================================
        
#User Main Management (IN PROGRESS)
        
#==============================================================================================
    
def usermanagement():
    
    def userchangeusername():
        
        print("Enter 'N' at any point to Cancel")
        print("")
        
        change1=input("New Username: ")
        
        if change1 == 'n' or change1 == 'N':
            
            print("")
            print("Username change stopped!")
            print("")
            
            usermanagement()
        
        change2=input("Confirm Username: ")
        print("")
        
        if change1 == change2:
            
            checkchange=input("Are you sure that you want to change your username to, " +change2+ "? (y/n) ")
            print("")
            
            if checkchange == 'y' or checkchange == 'Y':
                
                #Line here changes users information
            
                print("Username change success!")
                print("")
                
                usermanagement()
                
            elif checkchange == 'n' or checkchange == 'N':
                
                print("Username change stopped!")
                print("")
                
                usermanagement()
                
        elif change2 == 'n' or change2 == 'N':
            
            print("Username change stopped!")
            print("")
            
            usermanagement()
                
        else:
            
            print("Usernames didn't match! Please try again..")
            print("")
            
            userchangeusername()
        
    def userchangepassword():
        
        print("Enter 'N' at any point to Cancel")
        print("")
        
        checkgo=input("Current Password: ")
        
        if checkgo == userpassword:
            
            print("")
            
        elif checkgo == 'n' or checkgo == 'N':
            
            print("")
            print("Password Change Cancelled!")
            print("")
            
            usermanagement()
            
        else:
            
            print("")
            print("Password is incorrect! Please try again...")
            print("")
            
            userchangepassword()
        
        change1=input("New Password: ")
        
        if change1 == 'n' or change1 == 'N':
            
            print("")
            print("Password change stopped!")
            print("")
            
            usermanagement()
            
        elif change1 == userpassword:
            
            print("")
            print("Sorry! Passwords cannot be the same as the previous...")
            print("")
            
            usermanagement()
        
        change2=input("Confirm Password: ")
        print("")
        
        if change2 == userpassword:
            
            print("Sorry! Passwords cannot be the same as the previous...")
            print("")
            
            usermanagement()
        
        if change1 == change2:
            
            checkchange=input("Are you sure that you want to change your password to, " +change2+ "? (y/n) ")
            print("")
            
            if checkchange == 'y' or checkchange == 'Y':
                
                #Line here changes users information
            
                print("Password change success!")
                print("")
                
                usermanagement()
                
            elif checkchange == 'n' or checkchange == 'N':
                
                print("Password change stopped!")
                print("")
                
                usermanagement()
                
        elif change2 == 'n' or change2 == 'N':
            
            print("Password change stopped!")
            print("")
            
            usermanagement()
                
        else:
            
            print("Passwords didn't match! Please try again..")
            print("")
            
            userchangepassword()
        
    def userchangename():
        
        print("Enter 'N' at any point to Cancel")
        print("")
        
        change1=input("First Name: ")
        
        if change1 == 'n' or change1 == 'N':
            
            print("")
            print("Username change stopped!")
            print("")
            
            usermanagement()
        
        change2=input("Confirm First Name: ")
        
        if change1 == 'n' or change1 == 'N':
            
            print("")
            print("Username change stopped!")
            print("")
            
            usermanagement()
            
        if change1 == change2:
            
            print("")
            
        else:
            
            print("")
            print("First Names do not match...")
            print("")
            
            userchangename()
            
        change3=input("Last Name: ")
        
        if change3 == 'n' or change3 == 'N':
            
            print("")
            print("Username change stopped!")
            print("")
            
            usermanagement()
        
        change4=input("Confirm Last Name: ")
        
        if change4 == 'n' or change4 == 'N':
            
            print("")
            print("Username change stopped!")
            print("")
            
            usermanagement()
            
        if change3 == change4:
            
            print("")
            
        else:
            
            print("")
            print("Last Names do not match...")
            print("")
            
            userchangename()
            
        checkchangename=input("Are you sure that you want to change your name to, " +change2+ " " +change4+ "? (y/n) ")
        print("")
        
        if checkchangename == 'y' or checkchangename == 'Y':
            
            #Line here changes users information
            
            print("Name change success!")
            print("")
            
            usermanagement()
            
        elif checkchangename == 'n' or checkchangename == 'N':
            
            print("Process stopped!")
            print("")
            
            usermanagement()
            
        else:
            
            print("Invalid Input! Please try again...")
            print("")
            
            usermanagement()
        
    def userdelete():
        
        print("")
        
    def menuchoicesshow():

        print("Enter '1' To Change Your Username")
        print("Enter '2' To Reset Your Password")
        print("Enter '3' To Change Your Name")
        print("Enter '4' To Delete Your Account")
        print("Enter '5' To Cancel (Final)")
        
        print("")
        
        menuchoices()
        
    def menuchoices():
        
        menuinput=input("Enter option here: ")
        print("")
        
        if menuinput == '1':
            
            userchangeusername()
            
        elif menuinput == '2':
            
            userchangepassword()
            
        elif menuinput == '3':
            
            userchangename()
            
        elif menuinput == '4':
            
            userdelete()
            
        elif menuinput == '5':
            
            mainmenuuser()
            
        else:
            
            print("Invalid Input! Please Try Again!")
            print("")
            
            menuchoices()
        
    menuchoicesshow()
    
#==============================================================================================
        
#Danger Zone (In progress)
        
#==============================================================================================
    
def dangerzone():
    
    def dangerzoneuserdatabase():
        
        print("Feature coming soon...") #Finish
        
        print("")
        dangerzone()
        
    def dangerzoneflightdatabase():
        
        fileclear()

    print("Enter '1' to DELETE every User Account")
    print("Enter '2' to DELETE every Saved Flight")
    print("Enter '3' to return to Main Menu")
    
    print("")
    
    menuchoice=input("Enter option here: ")
    
    print("")
    
    if menuchoice == '1':
        
        dangerzoneuserdatabase()
        
    elif menuchoice == '2':
        
        dangerzoneflightdatabase()
        
    elif menuchoice == '3':
        
        print("Retuning back to the Main Menu...")
        
        print("")
        mainmenuchoice()
        
    else:
        
        print("Invalid Input. Please try again...")
        print("")
        dangerzone()
    
#==============================================================================================
        
#Booking (IN PROGRESS)
        
#==============================================================================================
    
def booking():
    
    bookingflightnumber = '0'
    
    def bookingview():
    
        print("Current Available Flights:")
        print("")
        
        print("-----------------------------------------------------------")
        print("")
        
        print("Flight Number #1")
        print("")
        
        print("FROM:")
        print(flight1uk+ " (" +flight1ukcode+ ")")
        print("TO:")
        print(flight1os+ " (" +flight1oscode+ ")")
        print("")
        print("Plane Model - " +flight1planechoice)
        print("")
        print("Economy Class - Starting at: £" +flight1standard)
        print("First Class - Starting at: £" +flight1first)
        
        print("")
        print("-----------------------------------------------------------")
        print("")
        
        print("Flight Number #2")
        print("")

        
        print("FROM:")
        print(flight2uk+ " (" +flight2ukcode+ ")")
        print("TO:")
        print(flight2os+ " (" +flight2oscode+ ")")
        print("")
        print("Plane Model - " +flight2planechoice)
        print("")
        print("Economy Class - Starting at: £" +flight2standard)
        print("First Class - Starting at: £" +flight2first)
        
        print("")
        print("-----------------------------------------------------------")
        print("")
        
        print("Flight Number #3")
        print("")
        
        print("FROM:")
        print(flight3uk+ " (" +flight3ukcode+ ")")
        print("TO:")
        print(flight3os+ " (" +flight3oscode+ ")")
        print("")
        print("Plane Model - " +flight3planechoice)
        print("")
        print("Economy Class - Starting at: £" +flight3standard)
        print("First Class - Starting at: £" +flight3first)
        
        print("")
        print("-----------------------------------------------------------")
        print("")
        
        bookingsecfirst()
        
    def bookingsecfirst():
        
        print("(NOTE - Enter 'R' to display the available flights again...)")
        print("(NOTE - Enter 'N' to cancel the booking process and return back to the main menu...)")
        
        bookingsec()
        
    def bookingsec():
        
        global bookingflightnumber
        
        bookingchoice=input("Please Enter The Flight Number Of The Flight You Wish To Book (Without The Hashtag): ")
        print("")
        
        if bookingchoice == '1':
            
            bookingflightnumber = '1'
            
            bookinginfo()
            
        elif bookingchoice == '2':
            
            bookingflightnumber = '2'
            
            bookinginfo()
            
        elif bookingchoice == '3':
            
            bookingflightnumber = '3'
            
            bookinginfo()
            
        elif bookingchoice == 'R' or bookingchoice == 'r':

            bookingview()
            
        elif bookingchoice == 'N' or bookingchoice == 'n':
            
            bookingflightnumber = '0'
            
            print("Process Stopped! Returning you back to the main menu...")
            print("")
            
            mainmenuuser()
            
        else:
            
            print("Invalid Input! Please try again...")
            print("")
            
            bookingsec()
            
    def bookinginfo():
        
        print("")
    
    print("Booking Portal:")
    print("")
    
    print("Let's see where you are flying to today, " +userfirstname+ "!")
    print("")
    
    print("Available Flights:")
    print("")
    
    bookingview()
    
#==============================================================================================
        
#Cancel Booking (IN PROGRESS)
        
#==============================================================================================
    
def cancelbooking():
    
    def cancelbookingview():
        
        print("")
    
    print("Cancel Booking Portal:")
    print("")
    
    print("Available Flights:")
    print("")
    
    cancelbookingview()

start()
