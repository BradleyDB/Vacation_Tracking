#-------------------------------------------------#
# Title: EmployeeApp
# Dev:   bbazhaw
# Date:  12/05/2016
# Desc: This application manages customer data
# ChangeLog: (Who, When, What)
#
#-------------------------------------------------#
if __name__ == "__main__":
    import vacation_manager
else:
    raise Exception("This file was not created to be imported")

#-- Data --#
# declare variables and constants
objE = None #an employee object
intId = 0 #an employee
gIntLastId = 0 #Records the last Employee used in the client
strFirstName = "" #a Customer's first name
strLastName = "" #an Customer's last name
strInput = "" #temporary user input

#-- Processing --#
#perform tasks
def ProcessNewEmployeeData(last_name, first_name, Id, hire_date):
    try:
        objE.employee_number=Id
        objE.first_name= first_name
        objE.last_name= last_name
        objE.hire_date= hire_date
        objE.max_vacation=12
        objE.dates_of_vacation=[]
        objE.remaining_vacation=self.max_vacation
        #Create Customer object
        objE = vacation_manager.Employee()
        #Customers.CustomerList.AddCustomer(objE)
    except Exception as e:
        print(e)

#def SaveDataToFile():
#    try:
#        objF = DataProcessor.File()
#        objF.FileName = "CustomerData.txt"
#        objF.TextData = Customers.CustomerList.ToString()
#        print("Reached here")
#        objF.SaveData()
#    except Exception as e:
#        print(e)

#-- Presentation (I/O) --#
#__main__

#get user input
strUserInput = ""
while(True):
  strUserInput = input("Would you like to add a New Employee?")
  if(strUserInput().lower() == "yes"):
      #Get Employee number from the User
      intId = int(input("Enter an Employee ID (Last ID was " + str(gIntLastId) + "): "))
      gIntLastId = intId
      #Get Customer FirstName from the User
      strFirstName = str(input("Enter the Employees First Name: "))
      #Get Customer LastName from the User
      strLastName = str(input("Enter the Employees Last Name: ") )
      #Process input
      vacation_manager.Employee(intId, strFirstName, strLastName)
  else:
      break

#send program output
print("The Current Data is: ")
print("------------------------")
print(Customers.CustomerList.ToString())

#get user input
strInput = input("Would you like to save this data to the dat file?(y/n)")
if(strInput == "y"):
    SaveDataToFile()
    #send program output
    print("data saved in file")
else:
    print("data was not saved")

print("This application has ended. Thank you!")
