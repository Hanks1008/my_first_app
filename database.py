"""
This file defines the database session, database setup, and connection.
"""

# imports
import sqlite3 as sql


# create event table
def event():
    connection = sql.connect("to_do_list_database.db")
    cursor = connection.cursor()
    create_event = "CREATE TABLE IF NOT EXISTS " \
                   "event(entry_id INTEGER PRIMARY KEY AUTOINCREMENT, entry STRING, status INTEGER, date INTEGER)"
    cursor.execute(create_event)
    connection.commit()
    connection.close()



# initiating database as a whole
def initiate():
    event()


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

    # this part aims to change the separated date values into one integer
    yearTwoDigits = (Year % 100)
    month_dict = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
                  "July": 7, "August": 8, "September": 9, "October":10, "November": 11, "December": 12}
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
def updateStatus(ID, status):
    connection = sql.connect("to_do_list_database.db")
    cursor = connection.cursor()
    if status == 0:
        after = 1
    elif status == 1:
        after = 0
    cursor.execute(f"UPDATE event SET status={after} where entry_id = {ID}")
    connection.commit()
    connection.close()

def fetchOneEvent(ID):
    connection = sql.connect("to_do_list_database.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT entry FROM event WHERE entry_id = {ID}")
    eventChosen = cursor.fetchall()
    connection.commit()
    connection.close()
    return eventChosen
