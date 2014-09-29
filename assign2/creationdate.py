# open each creation file and pull the creation date
# create a file called "creation_date"
# file output:
#     <fileNumber> '\t' <age in days>

import time
import calendar

# returns the number of days based on a date (Day Month Year)
#  received.
def age((year, month, day)):
    days = year*365                  # years, roughly
    days = days + (year+3)//4        # plus leap years, roughly
    days = days - (year+99)//100     # minus non-leap years every century
    days = days + (year+399)//400    # plus leap years every 4 centirues
    for i in range(1, month):
        if i == 2 and calendar.isleap(year):
            days = days + 29
        else:
            days = days + calendar.mdays[i]
    days = days + day
    return days

fout = open('creation_date', 'w+')

for x in range(1,1001): #open every file
    try:
        f = open(str(x), 'r')
    except:
        print "ERROR"
        continue

    date = f.readlines()
    #print x

    if not date:
        fout.write(str(x) + "\t" + "0\n")
        continue
  
    sub = "\"Estimated Creation Date\": "
    
    for string in date:
        if sub in string:   
            age = string.split('"')[3]
            if (age == ""):
                fout.write(str(x) + "\t0\n")
            else:
                age=age.split("T")[0]
                age=age.split("-")
                
                year = int(age[0])
                month = int(age[1])
                day = int(age[2])
               
                estCreation = (year, month, day)
                daysalive =  age(estCreation)

                todaydate = time.localtime()[:3]
                todaydate = age(todaydate)

                fout.write(str(x) + "\t" + str(todaydate-daysalive)+"\n") #prints age to the file

                
fout.close()