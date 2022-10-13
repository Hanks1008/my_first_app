# get suffix of date
def getSuffix(todayDay):
    if todayDay == 1 or todayDay == 21:
        todaySuffix = "st"
    elif todayDay == 2 or todayDay == 22:
        todaySuffix = "nd"
    elif todayDay == 3 or todayDay == 23:
        todaySuffix = "rd"
    else:
        todaySuffix = "th"
    return todaySuffix


# initializing future year list to pass into HTML files
def createFutureYearList(todayYear, yearLimit):
    futureYearList = []
    counter = 0
    while counter < yearLimit:
        futureYearList.append(todayYear+counter)
        counter += 1
    return futureYearList

def createPastYearList(todayYear, yearLimit):
    pastYearList = []
    counter = 0
    while counter < yearLimit:
        pastYearList.append(todayYear-counter)
        counter += 1
    return pastYearList


# month list
def getMonthList():
    global monthList
    monthList = ["January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November", "December"]
    return monthList


# initializing month list and month string to pass into HTML files
def getMonthString(todayMonth):
    todayMonthString = monthList[todayMonth-1]
    return todayMonthString

# initializing day list to pass into HTML files
def createDayList(todayYear, todayMonth):
    month30 = [4, 6, 9, 11]
    leapYear = False
    if todayYear % 4 == 0:  # check for leap year
        leapYear = True
        if todayYear % 100 == 0 and todayYear % 400 != 0:
            leapYear = False

    if todayMonth in month30:
        dayCount = 30
    elif todayMonth == 2 and leapYear:
        dayCount = 29
    elif todayMonth == 2:
        dayCount = 28
    else:
        dayCount = 31

    dayList = []
    counter = 0
    while counter < dayCount:
        dayList.append(counter+1)
        counter += 1
    return dayList
