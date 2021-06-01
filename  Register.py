import random

database = {} #dictionary

balance = 2000

def init():

    print("Welcome to BankPHP")
    haveAccount = int(input("Do you have an account with us: 1 (yes),  2(no) ")) 
    
    
    if (haveAccount == 1):
        login()

    elif (haveAccount ==2):  
        print(register())

    else:
        print("You have selected an invalid option")
        init()


def login():
    print ("\n******** LOGIN ********")

    accountNumberFromUser = int(input("What is your acount number?\n"))
    password = input("What is your password? \n")

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if (userDetails[3] == password):
                bankOpperation(userDetails)         
    else:
        print("Invalid account or password")
        login()


def register():
    print("***** Register ******")
    email = input("What is you email address?\n")
    first_name = input( "What is you first name?\n")
    last_name = input( "What is you last name?\n")
    password = input("Create a password\n")

    accountnumber = generateAnAccountNumber()

    database[accountnumber] = [ first_name, last_name, email, password]
    print("Your account have been created.\n")
    print("== === ==== ===== ==== === ==")
    print("Your account number is %d" % accountnumber)
    print("Make sure you keep your account number safe")
    print("== === ==== ===== ==== === ==")

    login()

    

def bankOpperation(user):
    print("\n•••••••• Welcome %s %s ••••••••" % ( user[0], user[1]))
    userOptions()

def userOptions():    
    selectedOption = int(input(" \nPlease select a transaction. \n (1) Balance \n (2) Deposit \n (3) Withdrawal \n (4) Complaint \n (5) Logout\n (6) Exit\n"))
        
    if(selectedOption == 1):
        startingBalance(balance)
    
    elif(selectedOption == 2):
        depositOperation(balance)
    
    elif(selectedOption == 3):
      withdrawalOperation(balance)

    elif(selectedOption == 4):
      complaint()
    
    elif(selectedOption == 5):
        login()
    
    elif(selectedOption == 6):
      exit()
    
    else:
        print("invalid option selecte")
        userOptions()

def startingBalance(balance):
    print(f"Your balance is {balance}")

    anotherTrasaction = int (input("Would you like another transaction? (1) YES (2) NO"))
    if anotherTrasaction == 1: 
      userOptions()
    else:
        logout()

def depositOperation(balance):
    deposit = int(input("How much would you like to deposit? "))
    balance += deposit
    print(f"Your new balance is {balance}")

    anotherTrasaction = int (input("Would you like another transaction? (1) YES (2) NO "))
    if anotherTrasaction == 1: 
        userOptions()
    else:
        logout()

    

def withdrawalOperation(balance):
    print("You have Selected option 1")
    withdrawal = int(input("How much would you like to Withdrawal? \n"))

    if balance >= withdrawal:
        balance -= withdrawal
        print (f"Your new balance is {balance}")
        print("Please take your cash.")
    else:
        print("Insurficiant Funds")

    anotherTrasaction = int (input("Would you like another transaction? (1) YES (2) NO"))
    if anotherTrasaction == 1: 
        userOptions()
    else:
        logout()

def complaint():

    complaint = input("What is Your Complaint?")
    submitComplaint = int(input(f"Would You like to submit \n' {complaint} ' \n (1) Yes  (2) No (3) Exit Complaint"))

    if submitComplaint == 1:
      print("Thanks for your feedback")
      userOptions()
    elif submitComplaint == 2:
      complaint()
    else: 
      userOptions()
      
def logout():
    login()

def exit():
    init()



def generateAnAccountNumber():

    print("Generating Account number")
    return random.randrange(1111111111,9999999999)


### BANKING SYSTEM ###


init()