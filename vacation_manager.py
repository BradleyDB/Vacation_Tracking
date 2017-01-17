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
##<bbazhaw & DrewSauce>, 01-08-2016, abstracted what are now set_vacation_dates and get_date, added set_hire_date, changed Employee obj __str__,
##other minor functional improvements, data shelving, ability to create employee obj, dict to hold employee obj, cleaned up menues>
##<bbazhaw, 01-14-2017, added instance of VacationManager so that program can be called, added .items() to display_machine method, strip and title case to
##add employee method, minor output formatting changes for consistancy.
##Tested that works: Adding employee (all initial fields), removing employee, calling edit_employee menu from main menu, going back to main menu from editor>
##<bbazhaw, 01-16-2017, made functional updates to submenu after testing. Options 3,5,7-9 in edit_employee_menu() are functioning.>
##-------------------------------------------------##

import datetime
import shelve
import os



class Employee():
    def __init__(self, last_name, first_name, employee_id, hire_date, max_vacation=12):
        self.employee_id=employee_id
        self.first_name=first_name
        self.last_name=last_name
        self.hire_date=hire_date
        self.max_vacation=max_vacation
        self.dates_of_vacation= []
        self.remaining_vacation=max_vacation


    def rename_last_name(self):
        '''Allows you to change the last name of an employee'''
        new_last_name=input("Please enter the new Last Name: ")
        self.last_name=new_last_name.strip().title()

    def rename_first_name(self):
        '''Allows you to change the first name of an employee'''
        new_first_name=input("Please enter the new First Name: ")
        self.first_name=new_first_name.strip().title()


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
        '''Manually decreases baseline and available vacation by -1'''
        self.max_vacation -=1
        self.remaining_vacation -=1

    def check_dates(self, start_date):
        '''Does a date check on program launch, and at one year will
        add one day to the maximum vacation'''
        today=datetime.date.today()
        temp_date= self.hire_date
        temp_date.year=today.year
        if start_date < temp_date <= today:
            self.max_vacation += 1
            self.remaining_vacation = self.max_vacation

    def __str__(self):
        '''returns object properties when asked to define itself'''
        print("Employee Number: ", self.employee_id)
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Hire Date:", self.hire_date)
        print("Maximum Vacation Days this year:", self.max_vacation)
        print("Dates of Vacation Taken this year:", self.dates_of_vacation.sort(reverse=True)[0:20])
        print("Vacation Days Remaining this year:", self.remaining_vacation)



class DumbassError(Exception):
    pass


class VacationManager():
    '''Manages the employee data objects'''
    def __init__(self):
        '''initiates file and opens it if already available'''
        if os.path.exists('cicd_info.db.dat'):
            s = shelve.open('cicd_info.db')
            try:
                self.machine = s['machine_dict']
            except KeyError:
                self.machine = {}
            finally:
                s.close()
        else:
            self.machine = {}

    def save(self):
        '''saves data and closes file'''
        s = shelve.open('cicd_info.db')
        s['machine_dict'] = self.machine
        s.close()

    def add_employee(self):
        '''Adds an employee'''
        first_name = input('Please enter Employee First Name:\n').strip().title()
        last_name = input('Please enter Employee Last Name:\n').strip().title()
        try:
            employee_id = int(input('Please enter an Employee ID Number:\n'))
        except ValueError:
            print('Please make sure employee number is a valid integer value.')
            try:
                employee_id = int(input('Please enter Employee ID Number:\n'))
            except:
                print('Dude... no.')
                raise DumbassError
        print("Please enter the start date of the new Employee:\n")
        hire_date = self.get_date()
        cog = Employee(last_name=last_name, first_name=first_name, employee_id=employee_id, hire_date=hire_date)
        self.machine.update({cog.employee_id: cog})
        self.save()



    def set_vacation_dates(self, employee_id):
        '''allows you to add employee vacation dates'''
        date_list = []
        while True:
            if input('Type "Stop" when you are finished entering dates ').strip().lower()== 'stop':
                break
            date_list.append(self.get_date())
        self.machine[employee_id].dates_of_vacation.extend(date_list)
        self.save()


    def set_hire_date(self, employee_id):
        '''sets the date of hire for the employee'''
        self.machine[employee_id].hire_date = self.get_date()
        self.save()

        # #print("Enter in each day of vacation one at a time: \n")
        # #self.dates_of_vacation=[]
        # day=None
        # month=None
        # year=None
        # while(True):#start of day block
        #     value = input('Enter the day e.g. "05": ')
        #     if not len(value) == 2:
        #         print("Please enter two digits \n")
        #     else:
        #         try:
        #             day=int(value)
        #             if type(day)==int:
        #                 if day < 0:
        #                     print("Please enter a valid day")
        #                 elif day > 32:
        #                     print("Please enter a valid day")
        #                 else:
        #                     break
        #         except ValueError:
        #             print("Please try again")
        # while(True):#start of month block
        #     value_2 = input('Enter the month e.g. "07": ')
        #     if not len(value_2) == 2:
        #         print("Please enter two digits \n")
        #     else:
        #         try:
        #             month=int(value_2)
        #             if type(month)==int:
        #                 if month < 0:
        #                     print("Please enter a valid month")
        #                 elif month > 12:
        #                     print("Please enter a valid month")
        #                 else:
        #                     break
        #         except ValueError:
        #             print("Please try again")
        # while(True):#start of year block
        #     value_3 = input('Enter the year e.g. "2016": ')
        #     if not len(value_3) == 4:
        #         print("Please enter two digits \n")
        #     else:
        #         try:
        #             year=int(value_3)
        #             if type(year)==int:
        #                 if year < 0:
        #                     print("Please enter a valid year")
        #                 else:
        #                     break
        #         except ValueError:
        #             print("Please try again")
        #date_of_vacay = datetime.date(year, month, day)
        #dates_of_vacation.append(date_of_vacay)
        #return (dates_of_vacation)

    @staticmethod
    def get_date():
        '''this is a date input validation method'''
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
                print("Please enter four digits \n")
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
        new_date = datetime.date(year, month, day)
        return (new_date)

    def remove_employee(self, employee_id):
        '''removes an employee'''
        #add error handling if an invalid ID is entered or non valid integer
        del self.machine[int(input ('Please enter the Employee ID of the Employee you would like to remove: '))]
        self.save()

    def display_machine(self):
        '''display employee ID and employee info'''
        for key,value in self.machine.items():
            print (value)

    def main_menu(self):
        '''Main User Interface'''
        choice = None
        while choice != 'exit':
            choice = input('''
------------------------------------
Please make a selection.
1:\tDisplay List of Employee ID Numbers and Names
2:\tDisplay Vacation info for all Employees
3:\tEdit Existing Employee Information
4:\tAdd a New Employee
Exit:\tExit menu.
------------------------------------

''').strip()

            if choice == '1':
                for k, v in self.machine.items(): #added.items() so that the employee ID's would iterate
                    print ("ID #: ",k,"\nLast Name, First Name: ", v.last_name,",", v.first_name)
            elif choice == '2':
                self.display_machine()
            elif choice == '3':
                employee_id=int(input("Type an Employee ID from the list to modify their information: ").strip())
                self.edit_employee_menu(employee_id)
            elif choice == '4':
                self.add_employee()
            elif choice == 'exit':
                break
            else:
                print ('I\'m sorry Dave, I can\'t do that')

    def edit_employee_menu(self, employee_id):
        '''interface allowing user to manipulate a selected employee object'''
        choice= None
        cog = self.machine[employee_id]
        while choice != "back":
            choice = input('''
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
9:\tDelete Existing Employee
Back:\t Back to Main menu.
------------------------------------

''').strip().lower()

            if choice == '1':
                #how to get this to display cog object info??
                print ("I'm not ready yet")
            elif choice == '2':#takes the input but does not add to any list
                self.set_vacation_dates(employee_id=employee_id)
            elif choice == '3':#working
                cog.add_vacation_day()
            elif choice == '4':
                cog.add_temp_vacation_day()
            elif choice == '5': #working
                cog.remove_vacation_day()
            elif choice == '6':
                cog.remove_temp_vacation_day()
            elif choice == '7':#working
                cog.rename_last_name()
            elif choice == '8':#working
                cog.rename_first_name()
            elif choice == '9':#working
                self.remove_employee(employee_id=employee_id)
            elif choice == 'back':
                self.main_menu()
            else:
                print ('I\'m sorry Dave, I can\'t do that')


vm = VacationManager()
vm.main_menu()



