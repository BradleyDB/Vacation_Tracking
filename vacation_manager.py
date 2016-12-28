##-------------------------------------------------#
## Title: <Employee Vacation Tracker>
## Dev:   <bbazhaw> & <DrewSauce>
## Date:  <11-18-2016>
## Desc: <Allows Manager to Manage Employees and their remaining Vacation>
## ChangeLog: (Who, When, What)
## <bbazhaw, 11-18-2016, initialized project, added pseudo code and some class structure with methods>
##<bbazhaw, 11-19-2016, added more methods, started vacation date method loop>
##<bbazhaw, 11-12-2016, refined vacation date method, stared adding methods to manager class>
##<bbazhaw, 12-27-2016, changed sub_menu_1 to static method, renamed 'Employee' variable to 'cog', changed method parameters, added new class 'employee_manifest'>

##-------------------------------------------------#

import datetime

class Employee():
    def __init__(self, last_name, first_name, employee_number, hire_date, max_vacation=12):
        self.employee_ID=employee_number
        self.first_name=first_name
        self.last_name=last_name
        self.hire_date=hire_date
        self.max_vacation=max_vacation
        self.dates_of_vacation=[]
        self.remaining_vacation=max_vacation


    def rename_last_name(self):
        new_last_name=input("Please enter the new Last Name: ")
        self.last_name=new_last_name.strip.title

    def rename_first_name(self):
        '''Allows you to change the first name of an employee'''
        new_first_name=input("Please enter the new First Name: ")
        self.first_name=new_first_name.strip.title


    def add_vacation_day(self):
        '''Manually increases baseline and available vacation by +1'''
        self.max_vacation +=1
        self.remaining_vacation +=1

    def add_temp_vacation_day(self):
        '''Manually increases available vacation for that year by +1'''
        self.remaining_vacation +=1

    def remove_temp_vacation_day(self):
        '''Manually decreases available vacation for that year by -1'''
        self.remaining_vacation -=1

    def remove_vacation_day(self):
        '''Manually decreases basline and available vacation by -1'''
        self.max_vacation -=1
        self.remaining_vacation -=1

    def check_dates(self, start_date):
        today=datetime.date.today()
        temp_date= self.hire_date
        temp_date.year=today.year
        if start_date < temp_date <= today:
            self.max_vacation += 1
            self.remaining_vacation = self.max_vacation

    def display_employee_info(self):
        print("Employee Number: " + self.employee_number)
        print("First Name: " + self.first_name)
        print("Last Name: " + self.last_name)
        print("Hire Date: " + self.hire_date)
        print("Maximum Vacation Days this year: " + str(self.max_vacation))
        print("Dates of Vacation Taken this year: " + self.dates_of_vacation.sort(reverse=True)[0:20])
        print("Vacation Days Remaining this year: " + str(self.remaining_vacation))

    def vacation_dates(self):
        #print("Enter in each day of vacation one at a time: \n")
        #self.dates_of_vacation=[]
        day=None
        month=None
        year=None
        while(True):#start of day block
            value = input('Enter the day e.g. "05": ')
            if not len(value) == 2:
                print("Please enter two digits \n")
            else:
                try:
                    day=int(value)
                    if type(day)==int:
                        if day < 0:
                            print("Please enter a valid day")
                        elif day > 32:
                            print("Please enter a valid day")
                        else:
                            break
                except ValueError:
                    print("Please try again")
        while(True):#start of month block
            value_2 = input('Enter the month e.g. "07": ')
            if not len(value_2) == 2:
                print("Please enter two digits \n")
            else:
                try:
                    month=int(value_2)
                    if type(month)==int:
                        if month < 0:
                            print("Please enter a valid month")
                        elif month > 12:
                            print("Please enter a valid month")
                        else:
                            break
                except ValueError:
                    print("Please try again")
        while(True):#start of year block
            value_3 = input('Enter the year e.g. "2016": ')
            if not len(value_3) == 4:
                print("Please enter two digits \n")
            else:
                try:
                    year=int(value_3)
                    if type(year)==int:
                        if year < 0:
                            print("Please enter a valid year")
                        else:
                            break
                except ValueError:
                    print("Please try again")
        date_of_vacay = datetime.date(year, month, day)
        self.dates_of_vacation.append(date_of_vacay)
        return (self.dates_of_vacation)

    @staticmethod
    def start_date():
        #print("Enter in each day of vacation one at a time: \n")
        #self.dates_of_vacation=[]
        day=None
        month=None
        year=None
        while(True):#start of day block
            value = input('Enter the day e.g. "05": ')
            if not len(value) == 2:
                print("Please enter two digits \n")
            else:
                try:
                    day=int(value)
                    if type(day)==int:
                        if day < 0:
                            print("Please enter a valid day")
                        elif day > 32:
                            print("Please enter a valid day")
                        else:
                            break
                except ValueError:
                    print("Please try again")
        while(True):#start of month block
            value_2 = input('Enter the month e.g. "07": ')
            if not len(value_2) == 2:
                print("Please enter two digits \n")
            else:
                try:
                    month=int(value_2)
                    if type(month)==int:
                        if month < 0:
                            print("Please enter a valid month")
                        elif month > 12:
                            print("Please enter a valid month")
                        else:
                            break
                except ValueError:
                    print("Please try again")
        while(True):#start of year block
            value_3 = input('Enter the year e.g. "2016": ')
            if not len(value_3) == 4:
                print("Please enter two digits \n")
            else:
                try:
                    year=int(value_3)
                    if type(year)==int:
                        if year < 0:
                            print("Please enter a valid year")
                        else:
                            break
                except ValueError:
                    print("Please try again")
        hire_date = datetime.date(year, month, day)
        return (hire_date)

class employee_manafest():
    employee_dict={}



class Vacation_Manager():
    def __init__(self):
        self.report_days=None
        self.add_employee=None
        self.remove_employee=None
        self.menu=None


    def main_menu(self):
        choice = None
        while choice != 'exit':
            choice = input('''
------------------------------------
Please make a selection.
1:\tDisplay List of Employee Names
2:\tDisplay Vacation info for all Employees
3:\tEdit Existing Employee Information
4:\tAdd a New Employee
5:\tRemove Existing Employee
Exit:\tExit menu.
------------------------------------

''').strip()

            if choice == '1':
                #print list of employees names and ID's
                print('not ready')
            elif choice == '2':
               #for employee in employeelist
               #print(Employee.display_employee_info(employee))
               # Employee.display_employee_info(self)
                print('Not ready yet')
            elif choice == '3':
                new_choice=input("Type a name from the list to modify their information: ").strip().title()
                Vacation_Manager.sub_menu_1(cog)
            elif choice == '4':
                print('not ready')
            elif choice == '5':
                print('not ready')
            elif choice == 'exit':
                break
            else:
                print ('I\'m sorry Dave, I can\'t do that')

    @staticmethod
    def sub_menu_1(cog):
        choice_1= None
        while choice_1 != "back":
            choice_1 = input('''
------------------------------------
What would you like to do with this employee?
1:\tDisplay current vacation info
2:\tAdd a new day of vacation
3:\tManually increase baseline vacation and current year available vacation
4:\tManually increase available vacation (current year only)
5:\tManually decrease baseline vacation and current year available vacation
6:\tManually decrease available vacation (current year only)
7:\tChange Employee Last Name
8:\tChange Employee First Name
Back:\t Back to Main menu.
------------------------------------

''').strip()

            if choice_1 == '1':
                cog.display_employee_info()
            elif choice_1 == '2':
                while(True):
                    cog.vacation_dates()
                    add_more=input("Type 'continue' to add more or 'back' to go to") #I want to add variable that give's first name of the employees info they've been editing
                    if add_more.lower()== 'back':
                        break
                    else:
                        continue
            elif choice_1 == '3':
                cog.add_vacation_day()
                break
            elif choice_1 == '4':
                cog.add_temp_vacation_day()
                break
            elif choice_1 == '5':
                cog.remove_vacation_day()
                break
            elif choice_1 == '6':
                cog.remove_temp_vacation_day()
                break
            elif choice_1 == '7':
                cog.rename_last_name()
                break
            elif choice_1 == '8':
                cog.rename_first_name()
                break
            elif choice_1 == 'back':
                break
            else:
                print ('I\'m sorry Dave, I can\'t do that')

            #want 1) submenue
            #type a name to display employees current vacation information
            #type 'back' to go to the main menue
        #menu
        #view all employees and data at once
        #view list of employees (just names)
        #enter employee name and view all data on employee
        #

employee_obj=Employee(Firstname='', input('Please enter last name: ').strip().title(),ID , Employee.start_date())
employee_obj.employee_number += 1

employee_obj.first_name=input("Please enter first name:").strip().title()
employee_obj.last_name=input('Please enter last name: ').strip().title()
employee_obj.hire_date=Employee.start_date()
employee_obj.max_vacation=12
employee_obj.dates_of_vacation=[]
employee_obj.remaining_vacation=employee_obj.max_vacation
employee_obj=Employee(employee_obj.first_name, employee_obj.last_name, employee_obj.employee_number, employee_obj.hire_date)








