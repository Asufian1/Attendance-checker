# input: none
# output: list of students in a class: lastname, firstnam
def fill_roster():
    newRoster = list()
    newRoster.append("Hamilton, Eric") #early, signed in, signed out
    newRoster.append("Lupoli, Shawn") #early, signed in, signed out
    newRoster.append("Allgood, Nick") #late, signed in
    newRoster.append("Arsenault, Al") #no show
    newRoster.append("Aja, Richard") #early, signed in, signed out
    newRoster.append("Asad, Hamza") #late, signed in
    newRoster.append("Barot, Bharg") #early, signed in, signed out
    newRoster.append("Cajudoy, Janeiyah") #late, signed in, signed out
    newRoster.append("Chen, Kevin") #early, signed in, signed out
    newRoster.append("Cleary, Miranda") #late, signed in, signed out
    newRoster.append("Diaz, Sergio") #early, signed in, signed out
    newRoster.append("Dove, Ellie") #late, signed in
    newRoster.append("Dulce, Alexander John") #early, signed in, signed out
    newRoster.append("Gaither, Oliver") #early, signed in, signed out
    newRoster.append("Gunaseelan, Adith") #late, signed in, signed out
    newRoster.append("Hambrecht, Matt") #early, signed in, signed out
    newRoster.append("Hassanein, Magdi") #early, signed in, signed out
    newRoster.append("Henderson, Sean") #early, signed in, signed out
    newRoster.append("Ilamni, Jazlyn") #late, signed in, signed out
    newRoster.append("Jacob, Ify") #late, signed in
    newRoster.append("Lare, George") #early, signed in, signed out
    newRoster.append("Mammel, Sammie") #no show
    newRoster.append("Odeseye, Ayodele")  #early, signed in, signed out
    newRoster.append("Ortiz, Joseph") #early, signed in, signed out
    newRoster.append("Othman, Youssef") #early, signed in, signed out
    newRoster.append("Pham, Matthew") #late, signed in, signed out
    newRoster.append("Premkumar, David") #early, signed in, signed out
    newRoster.append("Robinson, Edward") #early, signed in, signed out
    newRoster.append("Tang, Hieu") #late, signed in
    newRoster.append("Turner, Jessica") #early, signed in, signed out
    newRoster.append("Vantran, Luke")  #late, signed in, signed out
    newRoster.append("Vedasendur Senthilvel, Pranav") #late, signed in, signed out
    newRoster.append("Yahaya, Idris") #early, signed in, signed out
    newRoster.append("Zheng, Kelvin") #early, signed in, signed out
    newRoster.append("Zhuang, Michael") #late, signed in
    newRoster.append("Sheldon, Simon") #no show

    return newRoster

# creates a list of attendance data in this particular class.
# Notice, students SHOULD be listed twice, signing in, and signing out
# input: none
# output: list of students in a class: lastname, firstname
def fill_attendance_data():
    newData = list()

    #early people
    newData.append("Chen, Kevin, 08:55:34, 10/20/2022")
    newData.append("Diaz, Sergio, 08:55:44, 10/20/2022")
    newData.append("Dulce, Alexander John, 08:55:54, 10/20/2022")
    newData.append("Gaither, Oliver, 08:56:10, 10/20/2022")
    newData.append("Hambrecht, Matt, 08:56:11, 10/20/2022")
    newData.append("Hassanein, Magdi, 08:56:12, 10/20/2022")
    newData.append("Henderson, Sean, 08:56:13, 10/20/2022")
    newData.append("Lare, George, 08:56:14, 10/20/2022")
    newData.append("Hamilton, Eric, 08:50:34, 10/20/2022")
    newData.append("Lupoli, Shawn, 08:55:14, 10/20/2022")
    newData.append("Aja, Richard, 08:55:14, 10/20/2022")
    newData.append("Barot, Bharg, 08:55:24, 10/20/2022")
    newData.append("Odeseye, Ayodele, 08:57:14, 10/20/2022")
    newData.append("Ortiz, Joseph, 08:57:15, 10/20/2022")
    newData.append("Othman, Youssef, 08:57:16, 10/20/2022")
    newData.append("Premkumar, David, 08:57:17, 10/20/2022")
    newData.append("Robinson, Edward, 08:57:18, 10/20/2022")
    newData.append("Turner, Jessica, 08:57:19, 10/20/2022")
    newData.append("Yahaya, Idris, 08:57:20, 10/20/2022")
    newData.append("Zheng, Kelvin, 08:57:21, 10/20/2022")

    #late people
    newData.append("Allgood, Nick, 09:02:14, 10/20/2022")
    newData.append("Asad, Hamza, 09:03:14, 10/20/2022")
    newData.append("Cajudoy, Janeiyah, 09:04:14, 10/20/2022")
    newData.append("Cleary, Miranda, 09:05:14, 10/20/2022")
    newData.append("Dove, Ellie, 09:06:14, 10/20/2022")
    newData.append("Gunaseelan, Adith, 09:07:14, 10/20/2022")
    newData.append("Ilamni, Jazlyn, 09:02:15, 10/20/2022")
    newData.append("Jacob, Ify, 09:02:16, 10/20/2022")
    newData.append("Pham, Matthew, 09:02:17, 10/20/2022")
    newData.append("Tang, Hieu, 09:02:18, 10/20/2022")
    newData.append("Vantran, Luke, 09:02:21, 10/20/2022")
    newData.append("Vedasendur Senthilvel, Pranav, 09:02:22, 10/20/2022")
    newData.append("Zhuang, Michael, 09:02:23, 10/20/2022")

    #signed out
    newData.append("Aja, Richard, 09:15:34, 10/20/2022")
    newData.append("Barot, Bharg, 09:16:34, 10/20/2022")
    newData.append("Cajudoy, Janeiyah, 09:17:34, 10/20/2022")
    newData.append("Chen, Kevin, 09:18:34, 10/20/2022")
    newData.append("Cleary, Miranda, 09:19:34, 10/20/2022")
    newData.append("Diaz, Sergio, 09:15:35, 10/20/2022")
    newData.append("Dulce, Alexander John, 09:15:36, 10/20/2022")
    newData.append("Gaither, Oliver, 09:15:37, 10/20/2022")
    newData.append("Gunaseelan, Adith, 09:15:38, 10/20/2022")
    newData.append("Hambrecht, Matt, 09:15:39, 10/20/2022")
    newData.append("Hassanein, Magdi, 09:01:34, 10/20/2022")
    newData.append("Henderson, Sean, 09:02:34, 10/20/2022")
    newData.append("Ilamni, Jazlyn, 09:03:34, 10/20/2022")
    newData.append("Lare, George, 09:04:34, 10/20/2022")
    newData.append("Odeseye, Ayodele, 09:05:34, 10/20/2022")
    newData.append("Ortiz, Joseph, 09:06:34, 10/20/2022")
    newData.append("Othman, Youssef, 09:07:34, 10/20/2022")
    newData.append("Pham, Matthew, 09:08:34, 10/20/2022")
    newData.append("Premkumar, David, 09:09:34, 10/20/2022")
    newData.append("Robinson, Edward, 09:10:34, 10/20/2022")
    newData.append("Turner, Jessica, 09:11:34, 10/20/2022")
    newData.append("Vantran, Luke, 09:12:34, 10/20/2022")
    newData.append("Vedasendur Senthilvel, Pranav, 09:13:34, 10/20/2022")
    newData.append("Yahaya, Idris, 09:14:34, 10/20/2022")
    newData.append("Zheng, Kelvin, 09:16:34, 10/20/2022")
    newData.append("Hamilton, Eric, 09:08:24, 10/20/2022")
    newData.append("Lupoli, Shawn, 09:20:14, 10/20/2022")

    # Nick never signed out
    # newData.append("Allgood, Nick, 09:10:14, 10/20/2022")
    #notice, no Al

    return newData


"""
File: p1.py
Author: Abdullah Sufian
Date: 11/03/22
Lab Section: Dis sec 33
Email:  asufian1@umbc.edu
Description:  This program shows the layout of code in a Python file, it also gets functions and
prints out people not in class, who arrived first, checking in and out, and checks if people sign in or not
"""

''' ***** LEAVE THE LINES BELOW ALONE ***************                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
********* LEAVE THE LINES BELOW ALONE ***************                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
********* LEAVE THE LINES BELOW ALONE *************** '''




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
   for i in classRoster:
      if i not in attendData:
         not_in_class_list.append(i)

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
   for i in list_two:
      if name in (i[:]):
         list_two.append(i)

   return(check_in)
def list_all_times_checked_in(attendData):
   """
   This function returns a list of when all student(s) FIRST swipe in.
   :param attendData:  This is the list where people atteneded class
   :none:
   :return: this returns all the times where people checked in
   """
   check_in = list()
   for i in attendData:
      check_in.append(i[0:33])

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

    return('{}, {}'.format(earliestStudent_name[0],earliestStudent_name[1]))






def printList(value):
    """
    Simply prints the list. The function should not be able to change any
    values of that list passed in.
    :param value: This is just so it can print out the function that is called
    :none:
    :return: returns the list that will be called in the if name = main part
    """
    #makes a list
    print_list = list()
    #for loop to make sure it prints out all values and not just one
    for i in print_list:
       print_list.append(i)

    return(value)

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



