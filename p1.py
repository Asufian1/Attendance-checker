"""
File: p1.py
Author: YOUR NAME
Date: THE DATE
Lab Section: YOUR LAB Section
Email:  YOUREMAIL@umbc.edu
Description:  This program shows the layout of code in a Python file, and greets
the user with the name of the programmer
"""

''' ***** LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE *************** '''
debug = False

from dataEntry import fill_roster
from dataEntry import fill_attendance_data

''' ***** LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE *************** '''

def list_students_not_in_class(classRoster, attendData):
   """
   Compare the swipe log with the given course roster. Place those students that
   did not show up for class into a list.
   :param classRoster: This is the entire classRoster
   :param attendData: This is the people who signed into class
   :return: This returns the list of the people who are not in class
   """
   # this makes the list then uses a for loop to check each person if they arrived to class or not then appends them to a list
   not_in_class_list = list()
   name_list = list()
   roster_name = list()
   list_o = list()
   #This is splitting and getting the names from attendance
   for i in (attendData):
       token = i.split(',')
       
       name_list.append(token[0])
    # this is splitting and getting the names from the classroster   
   for i in classRoster:
        new_name = i.split(',')
        roster_name.append(new_name[0])
    # this checks if roster name is in name list then appends if its not    
   for i in roster_name:
       if i not in name_list:
           list_o.append(i)
    
    # This checks if the name from the attendance is in the classRoster       
   for i in list_o:
        name = i
        for i in classRoster:
            if name in (i[:]):
                not_in_class_list.append(i)
    #returns the function
   return(not_in_class_list)

def list_all_times_checking_in_and_out(value, attendData):
   """
   Looking at the swiping log, this function will list all in and outs for a
   particular Student. Please note, as coded in the p1.py file given, this
   function was called three times with different student values.
   : Value: This is for the specific person to see if they signed in and signed out
≈   : attendData: This is the list where people atteneded class
   :: this returns the check in times and check out (if they did both)
   """
   #this gets two list
   check_in = list()
   name = value
   list_two = list()
   # this appends evryone in attendata into the check in list
   for i in attendData:
      check_in.append(i)
   #This sees if the person also checked out and puts into second list
   for i in check_in:
      if name in (i[:]):
         list_two.append(i)

   return(list_two)

def list_all_times_checked_in(attendData):
   """
   This function returns a list of when all student(s) FIRST swipe in.
   :param attendData:  This is the list where people atteneded class
   :none:
   :return: this returns all the times where people checked in
   """
   check_in = list()
   list_two = list()
   list_three = list()
   
   for i in attendData:
       check_in.append(i)
   for i in attendData:
        value = i.split(',')
        
        if value[0] not in list_three:
            list_two.append(i)
            list_three.append(value[0])
   return(list_two)    
    
def list_students_late_to_class(time, attendData):
    """
    When given a timestamp string and the swipe log, a list of those records
    of students who swiped in late into the class is produced. This function
    returns a list of when all student(s) FIRST swipe in.
    :param time: this is for the late times over 9:00:00
    :param attendData: This is the list where people atteneded class
    :return: this returns the people who are late to class
    """
    # this makes the lists
    time = time
    late_to_class = list()
    list_two = []
    list_three = []
    list_four = []

    # This appends everyone in attendData into a list
    for i in attendData:
       late_to_class.append(i)
   # this tokenizes the string in each value in the list
    for i in attendData:
       value = i.split(',')

      # this checks if the name is not in list three then appends it to list 4, and then appends the name to list 3
       if value[0] not in list_three:
            list_four.append(i)
            list_three.append(value[0])
   # this splits the string agaian and gets the time
    for i in list_four:
       token = i.split(',')
       new_token = token[2]
      # This then checks if the time is late theb appends to list two which are the late time
       if time[0:2] in new_token[0:3]:
          list_two.append(i)

    return(list_two)

def get_first_student_to_enter(attendData):
    """
    Simply, this function returns the student that swiped in first. Note,
    the order of the data entered into the swipe log as not the earliest
    student to enter.
    :param attendData: This is the list where people atteneded class
    : none:
    :return: returns the first student who enters first name and last name only
    """
    # This is splitting the attenData string
    earliestTimeStr    = attendData[0].split(', ')[-2]
    earliestTimeSec    = 0
   # this splits the time by ':'
    comps = earliestTimeStr.split(':')
   #This converts the time into int and then into seconds
    earliestTimeSec += int(comps[0])*60*60
    earliestTimeSec += int(comps[1])*60
    earliestTimeSec += int(comps[2])

   #sets value
    earliestTime_index = 0

   # Splits the attendData in each string
    for i in range(len(attendData)):
       arrivalTimeStr = attendData[i].split(', ')[-2]
       arrivalTimeSec = 0
       #same as top
       comps = arrivalTimeStr.split(':')
       arrivalTimeSec += int(comps[0])*60*60
       arrivalTimeSec += int(comps[1])*60
       arrivalTimeSec += int(comps[2])

      #This checks for the lowest time
       if(arrivalTimeSec < earliestTimeSec):
          earliestTimeSec    = arrivalTimeSec
          earliestTime_index = i
   # This helps get only the student name and not the whole string
    earliestStudent_name = attendData[earliestTime_index].split(', ')[0:2]
    #returns function with format first and last name
    return('{}, {}'.format(earliestStudent_name[0],earliestStudent_name[1]))
    


def printList(value):
    """
    Simply prints the list. The function should not be able to change any
    values of that list passed in.
    :param value: This is just so it can print out the function that is called
    :none:
    :return: returns the list that will be called in the if name = main part
    """
    print(*value, sep = '\n')
    
''' ***** LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE *************** '''

if __name__ == '__main__':
    # Example, Dr. NIcholas, 9am class    
    
    # load class roster here into a list
    classRoster = fill_roster()

    #figure out which attendance data file to load here
    
    #load data
    attendData = fill_attendance_data()
    
    #use different tests 
    # make sure roster was filled 
    #printList(classRoster)
    # make sure attendance data was loaded
    #printList(attendData)
    
    #list all those missing
    print("****** Students missing in class *************")    
    printList(list_students_not_in_class(classRoster, attendData))
    #list signin/out times for a student
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Lupoli, Shawn", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Allgood, Nick", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Arsenault, Al", attendData))  
    #display when students first signed in (and in attendance)
    print("****** Check in times for all students who attended***")
    printList(list_all_times_checked_in(attendData))  
    #display all of those students late to class
    print("****** Students that arrived late ********************")
    printList(list_students_late_to_class("09:00:00", attendData))
    #display first student to enter class
    print("******* Get 1st student to enter class ****************")    
    print(get_first_student_to_enter(attendData))
    
''' ***** LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE *************** '''
