# UserIOUtils.py
#
# Author: Yuhong Li
#
# Created on 02/20/2013
# Final Edited on 04/10/2017
# ----------------------------------------


import datetime


'''
    Ask user to enter a stock symbol.
'''
def askForStockSymbol() -> str:
    info = "Please enter the stock symbol: "
    userInput = ''
    while True:
        try:
            userInput = askForUserInput(info, 'str').upper()
            checkInputContainsAlphabetOnly(userInput)
            return userInput
        except Exception as error:
            print("Invalid stock symbol. Please try again.")


'''
    Ask user for start date.
'''
def askForStartDate() -> str:
    info = "Please enter the start date in the format'YYYY-MM-DD': "
    startDate = ''
    while True:
        try:
            startDate = input(info)
            checkCorrectStartDate(startDate)
            return transferDate(startDate)
        except Exception as error:
            print("Invalid start date. Please try again.")


'''
    Ask user for end date.
     The end date should be after the start date, or it will be
     considered as an invalid date.
'''
def askForEndDate(startDate:str) -> str:
    info = "Please enter the end date in the format'YYYY-MM-DD': "
    endDate = ''
    while True:
        try:
            endDate = input(info)
            checkCorrectEndDate(endDate, startDate)
            return transferDate(endDate)
        except Exception as error:
            print("Invalid end date. Please try again.")


'''
    Ask user for signal strategy.
'''
def askForSignalStrategy() -> int:
    info = "Please enter the signal strategy.\n\t1)Simple moving average;"\
           + "\n\t2)Directional indicator;\nYour choice (1/2): "
    strategy = -1
    while True:
        try:
            strategy = askForUserInput(info, 'int')
            checkUserInputUnderCountLimit(strategy, 2)
            return strategy
        except Exception as error:
            print("Invalid strategy. Please try again.")


'''
    Ask user for how many days they want to check as a period.
'''
def askForPeriod() -> int:
    info = "Please enter how many days you want to check as a period: "
    period = -1
    while True:
        try:
            period = askForUserInput(info, 'int')
            checkPeriodGreaterThanZero(period)
            return period
        except Exception as error:
            print("Invalid period. Please try again.")


'''
    Ask user for buy and sell signals.
'''
def askForBuyAndSellSignals():
    info1 = "Please enter buy signal: "
    info2 = "Please enter sell signal: "
    buySignal, sellSignal = -1, -1
    while True:
        try:
            buySignal = askForUserInput(info1, 'int')
            sellSignal = askForUserInput(info2, 'int')
            return buySignal, sellSignal
        except Exception as error:
            print("Invalid buy/sell signal. Please try again.")


'''
    Ask user if he/she wants to restart.
'''
def askForRestart() -> int:
    info = "\nDone! Want to restart the program? 1) Yes; 2) No (1/2): "
    response = -1
    while True:
        try:
            response = askForUserInput(info, 'int')
            checkUserInputUnderCountLimit(response, 2)
            return response
        except Exception as error:
            print("Invalid response. Please try again.")




# INPUT STRING UTILS #


'''
    Asks user to enter the information in specific format.
     It will ask user to retry if he/she gives an invalid input.
'''
def askForUserInput(info:str, typeLimit:str):
    try:
        response = input(info)
        result = eval(typeLimit)(response)
        return result
    except Exception as Error:
        print("Invalid type. Please try again.")


'''
    Check if input contains letters only.
'''
def checkInputContainsAlphabetOnly(userInput:str):
    assert(userInput.isalpha())


'''
    Check if user input is under count limit.
'''
def checkUserInputUnderCountLimit(userInput:int, limit:int):
    assert(0 < userInput <= limit)




# INPUT DATE UTILS #


'''
    Check if start date's format is correct, and it is on or before today.
'''
def checkCorrectStartDate(startDate:str):
    checkCorrectDateFormat(startDate)
    checkDateIsOrBeforeToday(startDate)


'''
    Check if end date's format is correct, and it is later than start date
'''
def checkCorrectEndDate(endDate:str, startDate:str):
    checkCorrectStartDate(endDate)
    checkEndDateIsAfterStartDate(endDate, startDate)


'''
    Check if input date is in correct Date format (YYYY-MM-DD).
'''
def checkCorrectDateFormat(date:str):
    datetime.datetime.strptime(date, "%Y-%m-%d")
    dateList = date.split('-')
    assert(len(dateList[0]) == 4 \
           and len(dateList[1]) == 2 and len(dateList[2]) == 2)


'''
    Check if the input date is on or before today.
'''
def checkDateIsOrBeforeToday(date:str):
    inputDate = datetime.datetime.strptime(date, "%Y-%m-%d")
    currentDate = datetime.datetime.today()
    assert(inputDate <= currentDate)


'''
    Check if the end date is after the start date.
'''
def checkEndDateIsAfterStartDate(endDate:str, startDate:str):
    startingDate = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    endingDate = datetime.datetime.strptime(endDate, "%Y-%m-%d")
    assert(endingDate > startingDate)


'''
    Check if period is greater than 0.
'''
def checkPeriodGreaterThanZero(period:int):
    assert(period > 0)


'''
    Transfer MM and/or DD from two digits to one if they are smaller than 10.
'''
def transferDate(date:str):
    dateList = date.split('-')
    return dateList[0] + '-' + str(int(dateList[1])) + '-' + str(int(dateList[2]))




# OUTPUT UTILS #


'''
    Print result for simple moving average.
'''
def printSimpleMovingAverage(symbol, buySignal, sellSignal, timeList, priceList, indicatorList, signalList):
    strategy = "Simple Moving Average"
    printHelper(strategy, symbol, buySignal, sellSignal, timeList, priceList, indicatorList, signalList)


'''
    Print result for directional.
'''
def printDirectionalIndicator(symbol, buySignal, sellSignal, timeList, priceList, indicatorList, signalList):
    strategy = "Directional Indicator"
    printHelper(strategy, symbol, str(buySignal), str(sellSignal), timeList, priceList, purifyIndicatorList(indicatorList), signalList)


'''
    Print helper.
'''
def printHelper(strategy, symbol, buySignal, sellSignal, timeList, priceList, indicatorList, signalList):
    title = "\nSYMBOL: " + symbol + "\nSTRATEGY: " + strategy
    title += "\nBuy Above " + str(buySignal)
    title += ", Sell Below " + str(sellSignal)
    title += "\n\nDATE" + " " * 10 + "CLOSE" + " " * 8 + "INDICATOR" + " " * 6 + "SIGNAL"
    stringFormat = "{:10}" + " " * 4 + "{:6.2f}" + " " * 8 + "{:11}" + " " * 4 + "{}"

    print(len(timeList), len(priceList), len(indicatorList), len(signalList))

    print(title)
    for i in range(len(timeList)):
        print(stringFormat.format(timeList[i], priceList[i], indicatorList[i], signalList[i]))


'''
    Purify Directional Indicator's indicatorList.
'''
def purifyIndicatorList(indicatorList):
    newIndicatorList = []
    for i in range(len(indicatorList)):
        if indicatorList[i] > 0:
            newIndicatorList.append('+' + str(indicatorList[i]))
        else:
            newIndicatorList.append(str(indicatorList[i]))
    return newIndicatorList
