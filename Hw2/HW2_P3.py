year = input("Please input a Year:")            #lets users input the desired year
month = input("Please input a Month:")          #let users input the desired month
cal_format = '%s %s %s %s %s %s %s'             #the format for the Calender Days. Using format makes it so that we don't need to retype all 7 days of the week everytime
cal_header = 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' #the words that's going to replace the string formatting, which is the 7 days of the week
day_30 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30      #integers to fill 30 days month format
day_31 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31  #integers to fill 31 days month format
day_feb = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28             #integers to fill 28 days month format
day_leap = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29        #integers to fill 29 days month format
if month.isdigit() and year.isdigit():          
    month = int(month)                          
    year = int(year)
    if 0 < month <= 12:                         
        t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]  
        year -= month < 3                         
        day = (year + year // 4 - year // 100 + year // 400 + t[month - 1] + 1) % 7 
        if month == 4 or month == 6 or month == 9 or month == 11:                   
            if day == 0:                                                            
                day_format = "%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d"
                print(cal_format % cal_header)  #day_format is the string formatting for the numbered days of the calendar, which will will be different depending on month and day
                                                #The one above is for sundays
                print(day_format % day_30)      #use the string formatting operator to insert the integers contained in day_30 to the day_format for sundays on 30 day months
            elif day == 1:                      #"elif" coniditon for mondays
                day_format = "    %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d"
                print(cal_format % cal_header)  #The day_format above is the format for mondays on 30 day months
                print(day_format % day_30)
            elif day == 2:                      #"elif" condition for tuesdays
                day_format = "        %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d"
                print(cal_format % cal_header)  #the day_format above is the format for tuesdays on 30 day months
                print(day_format % day_30)
            elif day == 3:                      #"elif" condition for wednesdays
                day_format = "            %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d  %02d"
                print(cal_format % cal_header)  #the day_format above is the format for wednesdays on 30 day months
                print(day_format % day_30)
            elif day == 4:                      #"elif" condition for thursdays
                day_format = "                %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d  %02d  %02d"
                print(cal_format % cal_header) #the above day_format is for thursdays on 30 day months
                print(day_format % day_30)
            elif day == 5:                      #"elif" condition for fridays
                day_format = "                    %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d  %02d  %02d  %02d"
                print(cal_format % cal_header)  #the above day_format is for fridays on 30 day months
                print(day_format % day_30)
            elif day == 6:                      #"elif" condition for saturdays
                day_format = "                        %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d  %02d  %02d  %02d  \n%02d"
                print(cal_format % cal_header)  #the above day_format is for saturdays on 30 day months
                print(day_format % day_30)
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:  #"elif" condition specifically for 31 day months
            if day == 0:
                day_format = "%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d"
                print(cal_format % cal_header)  #the above day_format is for sundays on 31 day months
                print(day_format % day_31)
            elif day == 1:
                day_format = "    %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d"
                print(cal_format % cal_header)  #The day_format above is the format for mondays on 31 day months
                print(day_format % day_31)
            elif day == 2:
                day_format = "        %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d  %02d"
                print(cal_format % cal_header)  #the day_format above is the format for tuesdays on 31 day months
                print(day_format % day_31)
            elif day == 3:
                day_format = "            %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d  %02d  %02d"
                print(cal_format % cal_header)  #the day_format above is the format for wednesdays on 31 day months
                print(day_format % day_31)
            elif day == 4:
                day_format = "                %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d  %02d  %02d  %02d"
                print(cal_format % cal_header)  #the above day_format is for thursdays on 31 day months
                print(day_format % day_31)
            elif day == 5:
                day_format = "                    %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d"
                print(cal_format % cal_header)  #the above day_format is for fridays on 31 day months
                print(day_format % day_31)
            elif day == 6:
                day_format = "                        %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d  %02d  %02d  %02d  \n%02d  %02d"
                print(cal_format % cal_header)  #the above day_format is for saturdays on 31 day months
                print(day_format % day_31)
        elif month == 2 and (year + 1) % 4 != 0 or (
                (year + 1) % 4 == 0 and (year + 1) % 100 == 0 and (year + 1) % 400 != 0):
            if day == 0:
                day_format = "%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d"
                print(cal_format % cal_header)  #the above day_format is for sundays on non-leap year february
                print(day_format % day_feb)
            elif day == 1:
                day_format = "    %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d"
                print(cal_format % cal_header)  #the above day_format is for mondays on non-leap year february
                print(day_format % day_feb)
            elif day == 2:
                day_format = "        %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d"
                print(cal_format % cal_header)  #the above day_format is for tuesdays on non-leap year february
                print(day_format % day_feb)
            elif day == 3:
                day_format = "            %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d"
                print(cal_format % cal_header)  #the above day_format is for wednesdays on non-leap year february
                print(day_format % day_feb)
            elif day == 4:
                day_format = "                %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d"
                print(cal_format % cal_header) #the above day_format is for thursdays on non-leap year february
                print(day_format % day_feb)
            elif day == 5:
                day_format = "                    %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d  %02d"
                print(cal_format % cal_header)  #the above day_format is for fridays on non-leap year february
                print(day_format % day_feb)
            elif day == 6:
                day_format = "                        %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d  %02d  %02d"
                print(cal_format % cal_header)  #the above day_format is for saturdays on non-leap year february
                print(day_format % day_feb)
        elif month == 2 and ((year + 1) % 4 == 0 and (year + 1) % 100 != 0) or (
                (year + 1) % 4 == 0 and (year + 1) % 100 == 0 and (year + 1) % 400 == 0):
            if day == 0:
                day_format = "%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d"
                print(cal_format % cal_header)  #the above day_format is for sundays on leap year february
                print(day_format % day_leap)
            elif day == 1:
                day_format = "    %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d"
                print(cal_format % cal_header)  #the above day_format is for mondays on leap year february
                print(day_format % day_leap)
            elif day == 2:
                day_format = "        %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d"
                print(cal_format % cal_header)  #the above day_format is for tuedays on leap year february
                print(day_format % day_leap)
            elif day == 3:
                day_format = "            %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d"
                print(cal_format % cal_header)  #the above day_format is for wednesdays on leap year february
                print(day_format % day_leap)
            elif day == 4:
                day_format = "                %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d  %02d"
                print(cal_format % cal_header)  #the above day_format is for thursdays on leap year february
                print(day_format % day_leap)
            elif day == 5:
                day_format = "                    %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d  %02d  %02d"
                print(cal_format % cal_header)  #the above day_format is for fridays on leap year february
                print(day_format % day_leap)
            elif day == 6:
                day_format = "                        %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d \n%02d  %02d  %02d  %02d  %02d  %02d  %02d\n%02d  %02d  %02d  %02d  %02d  %02d  %02d"
                print(cal_format % cal_header)  #the above day_format is for saturdays on leap year february
                print(day_format % day_leap)
    else:
        print("Please input a month between 1 to 12 (January to December)!")        #error message if user inputs months that do not exist
else:
    print("Please input a whole number to represent the month and year desired!")   #error message if user inputs non-integers
    