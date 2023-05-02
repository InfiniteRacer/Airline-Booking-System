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
#=============
ukairport2 = 'Bournemouth International'
ukairport2code = 'BOH'

#Overseas Airports
overseasairport1 = 'John F Kennedy International'
overseasairport1code = 'JFK'
overseasairport1lpl = '5326'
overseasairport1boh = '5486'
#===================
overseasairport2 = 'Paris-Orly'
overseasairport2code = 'ORY'
overseasairport2lpl = '629'
overseasairport2boh = '379'
#===================
overseasairport3 = 'Adolfo Suarez Madrid- Barajas'
overseasairport3code = 'MAD'
overseasairport3lpl = '1428'
overseasairport3boh = '1151'
#===================
overseasairport4 = 'Amsterdam Schiphol'
overseasairport4code = 'AMS'
overseasairport4lpl = '526'
overseasairport4boh = '489'
#===================
overseasairport5 = 'Cairo International'
overseasairport5code = 'CAI'
overseasairport5lpl = '3779'
overseasairport5boh = '3584'

#User Inputs
global ukairportchoice
ukairportchoice = ''
#====================
global ukairportchoicecode
ukairportchoicecode = ''
#====================
global overseasairportchoice
overseasairportchoice = ''
#====================
global overseasairportchoicecode
overseasairportchoicecode = ''
#====================
global distance
distance = ''
#====================
global planechoice
planechoice = ''
#====================
global planechoicerun
planechoicerun = ''
#====================
global planechoicerange
planechoicerange = ''
#====================
global planechoicecap
planechoicecap = ''
#====================
global planechoiceminfirst
planechoiceminfirst = ''
#====================
global maxrange
maxrange = ''
#====================
global runcost
runcost = ''
#====================
global capallstandard
capallstandard = ''
#====================
global firstclassseasts
firstclassseats = ''
#====================
global firstclassseastsmax
firstclassseatsmax = ''
#====================
global standadseatsnumb
standardseatsnumb = ''
#====================
global pricestandard
pricestandard = ''
#====================
global pricefirst
pricefirst = ''
#====================
global flightcostperseat
flightcostperseat = ''
#====================
global flightcost
flightcost = ''
#====================
global flightincome
flightincome = ''
#====================
global flightprofit
flightprofit = ''

#Flights
global flight1
flight1 = 'No Flight Scheduled.'
#====================
global flight1uk
flight1uk = ''
#====================
global flight1os
flight1os = ''
#====================
global flight1standard
flight1standard = ''
#====================
global flight1first
flight1first = ''
#====================
global flight1planechoice
flight1planechoice = ''
#====================
global flight2
flight1 = 'No Flight Scheduled.'
#====================
global flight2uk
flight1uk = ''
#====================
global flight2os
flight1os = ''
#====================
global flight2standard
flight1standard = ''
#====================
global flight2first
flight1first = ''
#====================
global flight2planechoice
flight1planechoice = ''
#====================
global flight3
flight1 = 'No Flight Scheduled.'
#====================
global flight3uk
flight1uk = ''
#====================
global flight3os
flight1os = ''
#====================
global flight3standard
flight1standard = ''
#====================
global flight3first
flight1first = ''
#====================
global flight3planechoice
flight1planechoice = ''
#====================
global flight4
flight1 = 'No Flight Scheduled.'
#====================
global flight4uk
flight1uk = ''
#====================
global flight4os
flight1os = ''
#====================
global flight4standard
flight1standard = ''
#====================
global flight4first
flight1first = ''
#====================
global flight4planechoice
flight1planechoice = ''
#====================
global flight5
flight1 = 'No Flight Scheduled.'
#====================
global flight5uk
flight1uk = ''
#====================
global flight5os
flight1os = ''
#====================
global flight5standard
flight1standard = ''
#====================
global flight5first
flight1first = ''
#====================
global flight5planechoice
flight1planechoice = ''

#==============================================================================================

#Main Menu / Start

#==============================================================================================

def start():
    
    print("First Time Instructions:")
    print("Please select an option below. Type the number and press enter.")
    print("")
    
    mainmenu()
    
def mainmenu():
    
    print("Main Menu:")
    
    print("Enter '1' To Enter Airport Details")
    print("Enter '2' To Enter Flight Details")
    print("Enter '3' To Enter Price Plan And Calculate Profit")
    print("Enter '4' To Clear Data")
    print("Enter '5' To Quit")
    
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
        
        quitsec()
        
    else:
        
        print("Invalid Input! Please Try Again!")
        print("")
        
        mainmenuchoices()
        
#==============================================================================================
        
#Sections Start Here
        
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
        
        if overseasairportchoicenon == overseasairport1code:
            
            overseasaiportchoicecode = overseasairport1code
            
            overseasairportchoice = overseasairport1
            
            if ukairportchoicecode == ukairport1code:
                
                distance = overseasairport1lpl
                
            elif ukairportchoicecode == ukairport2code:
                
                distance = overseasairport1boh
                
            else:
                
                print("Error! Please try again. Somethings gone wrong from our side...")
                
                print("")
                mainmenu()
            
            print("")
            airportdetailsfinal()
            
        elif overseasairportchoicenon == overseasairport2code:
            
            overseasairportchoicecode = overseasairport2code
            
            overseasairportchoice = overseasairport2
            
            if ukairportchoicecode == ukairport1code:
                
                distance = overseasairport2lpl
                
            elif ukairportchoicecode == ukairport2code:
                
                distance = overseasairport2boh
                
            else:
                
                print("Error! Please try again. Somethings gone wrong from our side...")
                
                print("")
                mainmenu()
            
            print("")
            airportdetailsfinal()
            
        elif overseasairportchoicenon == overseasairport3code:
            
            overseasairportchoicecode = overseasairport3code
            
            overseasairportchoice = overseasairport3
            
            if ukairportchoicecode == ukairport1code:
                
                distance = overseasairport3lpl
                
            elif ukairportchoicecode == ukairport2code:
                
                distance = overseasairport3boh
                
            else:
                
                print("Error! Please try again. Somethings gone wrong from our side...")
                
                print("")
                mainmenu()
            
            print("")
            airportdetailsfinal()
            
        elif overseasairportchoicenon == overseasairport4code:
            
            overseasairportchoicecode = overseasairport4code
            
            overseasairportchoice = overseasairport4
            
            if ukairportchoicecode == ukairport1code:
                
                distance = overseasairport4lpl
                
            elif ukairportchoicecode == ukairport2code:
                
                distance = overseasairport4boh
                
            else:
                
                print("Error! Please try again. Somethings gone wrong from our side...")
                
                print("")
                mainmenu()
            
            print("")
            airportdetailsfinal()
            
        elif overseasairportchoicenon == overseasairport5code:
            
            overseasairportchoicecode = overseasairport5code
            
            overseasairportchoice = overseasairport5
            
            if ukairportchoicecode == ukairport1code:
                
                distance = overseasairport5lpl
                
            elif ukairportchoicecode == ukairport2code:
                
                distance = overseasairpor5boh
                
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
    
    if ukairportchoicenon == ukairport1code:
        
        ukairportchoicecode = ukairport1code
        
        ukairportchoice = ukairport1
        
        print("")
        airportdetailsnext()
        
    elif ukairportchoicenon == ukairport2code:
        
        ukairportchoicecode = ukairport2code
        
        ukairportchoice = ukairport2
        
        print("")
        airportdetailsnext()
        
    else:
        
        print("Invalid Input. Please check the code and try again.")
        print("")
        
        mainmenu()        
    
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
            
        elif float(firstclassseats) < 8:
            
            print("You need to enter all the details (Including About First Class) before continuing.")
            print("")
            mainmenu() 
            
        else:
            
            priceplancheck4()
        
    def priceplancheck4():
        
        if maxrange == distance:
            
            print("You need to select a different aircraft! It isn't possible to complete the route with the selected aircraft.")
            print("")
            mainmenu()
            
        if maxrange > distance:
            
            print("You need to select a different aircraft! It isn't possible to complete the route with the selected aircraft.")
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
        
        savecheckpoint()
        
    def savecheckpoint():
        
        print("Enter '1' to return to the main menu.")
        print("Enter '2' to save a flight.")
        
        saveflightcheckpoint=input("Enter choice here: ")
        print("")
        
        if saveflightcheckpoint == '1'
        
            mainmenu()
            
        elif saveflightcheckpoint == '2'
        
            saveflight()
            
        else:
            
            print("Invalid Input! Please try again...")
            print("")
            
            savecheckpoint()
    
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
    
def saveflight():
    
    global ukairportchoice
    global ukairportchoicecode
    global overseasairportchoice
    global overseasairportchoicecode
    global planechoice
    global pricestandard
    global pricefirst
    
start()