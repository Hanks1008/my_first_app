"""
This will be the main file that takes care of all the API and structure things for the web.
"""

# import things
import uvicorn
from datetime import date
from fastapi import FastAPI, Query, Request, Form, Body, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import sqlite3
import database
import initializeDateTime


# Creating app instance
app = FastAPI()

# Creating an API Router, to help us separate code into separate files
general_pages_router = APIRouter()

# templating and routing template directory
templates = Jinja2Templates(directory="templates")

# SetUp database
# database.databaseInit()
database.initiate()


# create values for the current day
yearLimit = 10
today = date.today()
todayYear = today.year
todayMonth = today.month
todayDay = today.day
todaySuffix = initializeDateTime.getSuffix(todayDay)  # variable that stores what comes after day, e.g., 1st, 23rd, etc.


# initialize date lists
monthList = initializeDateTime.getMonthList()
futureYearList = initializeDateTime.createFutureYearList(todayYear, yearLimit)
pastYearList = initializeDateTime.createPastYearList(todayYear, yearLimit)
todayMonthString = initializeDateTime.getMonthString(todayMonth)
dayList = initializeDateTime.createDayList(todayYear, todayMonth)



# main page, main purpose: presents current to-do of the day, gives user possible ways of navigating to other pages
# other pages include: today's list, creating new event, view past todos, etc.
@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("mainPage.html", {"request": request, "day": todayDay, "month": todayMonthString,
                                                        "year": todayYear, "suffix": todaySuffix})


# page that showcases current day's list
@app.get("/todaysList", response_class=HTMLResponse)
async def todayTodo(request: Request):
    return templates.TemplateResponse("todayTodo.html", {"request": request})


# page that shows that event entered has been saved/stored
@app.get("/saved")
async def results(request: Request, Year: int, Month: str, Day: int, Event: str):
    status = False
    database.insertNewEntry(Year, Month, Day, Event, status)  # saves this entry into the database
    return templates.TemplateResponse("results.html", {"request": request, "Year": Year, "Month": Month,
                                                       "Day": Day, "Event": Event})

# page that creates new event
# important parameters that the user needs to input - date, status(defaulted to unfinished)
@app.get("/newEvent", response_class=HTMLResponse)
async def createNewEvent(request: Request):
    return templates.TemplateResponse("createNew.html", {"request": request, "futureYearList": futureYearList,
                                                         "monthList": monthList, "dayList": dayList})


# page that allows user to view past todos - in a list of the days that has todos
# Has buttons that can click - year, and then month, and then date
@app.get("/viewPastToDos/", response_class=HTMLResponse)
async def viewPastToDos(request: Request):
    return templates.TemplateResponse("viewPast.html", {"request": request, "pastYearList": pastYearList,
                                                        "monthList": monthList, "dayList": dayList})


# page that allows user to view future todos - in a list of the days that has todos
# Has buttons that can click - year, and then month, and then date
@app.get("/viewFutureToDos/", response_class=HTMLResponse)
async def viewFutureToDos(request: Request):
    return templates.TemplateResponse("viewFuture.html", {"request": request, "futureYearList": futureYearList,
                                                          "monthList": monthList, "dayList": dayList})


@app.get("/Info", response_class=HTMLResponse)
async def info(request: Request, Year: int, Month: str, Day: int):
    entryList = database.getEntry(Year, Month, Day)
    # finalEntryIDList = []
    # finalIDList = []
    # for entry in entryList:
    #     finalEntryList.append(entry[0])
    #     finalIDList.append(entry[1])


    # check if it's today and pass in a different header set if it is
    if Year == todayYear and Month == todayMonthString and Day == todayDay:
        headerWords = "Today's To-Dos!"
        titleWords = "Today's To-Dos!"
        instructWords = "Today's To-Dos include..."
    else:
        headerWords = "View To-Dos"
        titleWords = f"Events for {Month} {Day} of {Year}"
        instructWords = f"Events for {Month} {Day} of {Year} include..."



    return templates.TemplateResponse("viewTodo.html", {"request": request, "Year": Year,
                                                        "Month": Month, "Day": Day, "entryList": entryList,
                                                        "headerWords": headerWords, "titleWords": titleWords,
                                                        "instructWords": instructWords, "todayDay": todayDay,
                                                        "todayYear": todayYear, "todayMonth": todayMonthString})


@app.get("/checkedToDo", response_class=HTMLResponse)
async def checked(request:Request, ID: int):
    return templates.TemplateResponse("updated.html", {"request": request, "futureYearList": futureYearList,
                                                          "monthList": monthList, "dayList": dayList})