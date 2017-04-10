# DownloadData.py
#
# Author: Yuhong Li
#
# Created on 02/20/2013
# Final Edited on 04/10/2017
# ----------------------------------------

import urllib.request


class InvalidError(Exception):
    pass


'''
   Receive data according to the input symbol, start date, and end date.
    If it fails, an error will be raised.
'''
def downloadDataFromServer(symbol:str, startDate:str, endDate:str):
    startYear, startMonth, startDay = dateConverter(startDate)
    endYear, endMonth, endDay = dateConverter(endDate)

    # According to the Yahoo Finance API, we need to modify the startMonth and
    #  endMonth to get correct data.
    startMonth = int(startMonth) - 1
    endMonth = int(endMonth) - 1

    urlInfo = "http://ichart.yahoo.com/table.csv?" + "s={0}&a={1}&b={2}&c={3}&d={4}&e={5}&f={6}&g=d"

    url = urlInfo.format(symbol, startMonth, startDay, startYear, endMonth, endDay, endYear)

    try:
        response = urllib.request.urlopen(url)
        undecodedData = response.readlines()
        response.close()

        reversedDecodedData = [i.decode(encoding='utf-8') for i in undecodedData]
        return getTimeListAndPriceList(reversedDecodedData)

    except Exception as error:
        print(error)
        raise InvalidError


'''
    Seperate date into year, month, and day.
     Notice that the accepted date format is YYYY-MM-DD.
'''
def dateConverter(date:str):
    dateInfo = date.split('-')
    year, month, day = dateInfo[0], dateInfo[1], dateInfo[2]
    return year, month, day


'''
    It takes decoded data downloaded from the Internet, seperate
     date and closed price out, and returns a dateList and priceList.
'''
def getTimeListAndPriceList(reversedDecodedData):
    timeList, priceList = [], []

    for rawDailyInfo in reversedDecodedData[1:]:
        dailyInfo = rawDailyInfo.strip('\n').split(',')
        timeList.append(dailyInfo[0])
        priceList.append(eval(dailyInfo[4]))

    timeList.reverse()
    priceList.reverse()

    return timeList, priceList
