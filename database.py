"""
This file defines the database session, database setup, and connection.
"""

# imports
import sqlite3 as sql


# establishing connection
def databaseInit():
    connection = sql.connect("to_do_list_database.db")
    cursor = connection.cursor()


# create event table
def event():
    connection = sql.connect("to_do_list_database.db")
    cursor = connection.cursor()
    create_event = "CREATE TABLE IF NOT EXISTS " \
                   "event(entry_id INTEGER PRIMARY KEY AUTOINCREMENT, entry STRING, status INTEGER, date INTEGER)"
    cursor.execute(create_event)
    connection.commit()
    connection.close()


# create date tables that can store values by their unique entry id(that will not be presented to the user) to the
# date folder
# def date():
#     connection = sql.connect("to_do_list_database.db")
#     cursor = connection.cursor()
#     create_date_folder = "CREATE TABLE IF NOT EXISTS " \
#                          "date(date_num INTEGER, entry_id INTEGER," \
#                          "FOREIGN KEY(entry_id) references date(entry_id))"
#     cursor.execute(create_date_folder)
#     connection.commit()
#     connection.close()


# if nothing exists in the database, create an empty entry as an object
def createEmptyEntry():
    connection = sql.connect("to_do_list_database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM event")
    dateEntryList = cursor.fetchall()
    if not dateEntryList:
        create_empty_entry_event = "INSERT INTO event(entry, status, date) VALUES (0, 'Null', 0, 0)"
        cursor.execute(create_empty_entry_event)
        connection.commit()
    connection.close()


# initiating database as a whole
def initiate():
    event()
    # createEmptyEntry()


# view values
def viewValues():
    connection = sql.connect("to_do_list_database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM event")
    resultsE = cursor.fetchall()
    print(resultsE)
    connection.commit()
    connection.close()


# inserting values
def insertNewEntry(Year, Month, Day, Event, status):
    connection = sql.connect("to_do_list_database.db")
    cursor = connection.cursor()

    # this part aims to find the latest entry id and add one to find the newest entry id
    # cursor.execute("SELECT * FROM event")
    # dateEntryList = cursor.fetchall()

    # latestEntryID = dateEntryList[-1][0]
    # newEntryID = latestEntryID+1

    # this part aims to change the separated date values into one integer
    yearTwoDigits = (Year % 100)

    month_dict = {"January": 1,
                  "February": 2, "March":3, "April":4, "May":5, "June":6,
                  "July":7, "August":8, "September":9, "October":10, "November": 11, "December" :12}
    monthTwoDigits = month_dict[Month]
    dateID = yearTwoDigits*10000 + monthTwoDigits*100 + Day
    print(dateID)
    insertToEvent = "INSERT INTO event(entry, status, date) VALUES('"+str(Event)+"', 0, "+str(dateID)+")"
    cursor.execute(insertToEvent)
    connection.commit()
    connection.close()




# get entry from a certain day
def getEntry(Year, Month, Day):
    # create six digit id
    yearTwoDigits = (Year % 100)
    month_dict = {"January": 1,
                  "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
                  "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    monthTwoDigits = month_dict[Month]
    dateID = yearTwoDigits * 10000 + monthTwoDigits * 100 + Day
    print(dateID)
    # establish connection and create cursor
    connection = sql.connect("to_do_list_database.db")
    cursor = connection.cursor()

    # get all the date tables in the database

    cursor.execute(f"SELECT entry, entry_id, status FROM event WHERE date={dateID};")
    rightEvent = cursor.fetchall()
    connection.close()
    return rightEvent


#updates an event's status
def updateStatus(ID):
    connection = sql.connect("to_do_list_database.db")
    cursor = connection.cursor()

    cursor.execute(f"UPDATE entry SET status=1 where entry_id = {ID}")
    connection.commit()
    connection.close()