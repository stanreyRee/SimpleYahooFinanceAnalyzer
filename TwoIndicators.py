# TwoIndicators.py
#
# Author: Yuhong Li
#
# Created on 02/20/2013
# Final Edited on 04/10/2017
# ----------------------------------------

'''
    Calculate and return a list of indicators like '', '+', or '-'.
'''
def simpleMovingAverageIndicator(priceList, period):
    averageList = ['' for i in range(period - 1)]
    indicatorList = ['' for i in range(period - 1)]
    periodEndDay = -1

    days = len(priceList)

    for periodStartDay in range(days - period + 1):
        periodEndDay = periodStartDay + period - 1

        averageOfPeriod = sum(priceList[periodStartDay : periodEndDay + 1]) / period
        averageList.append("%.2f" % averageOfPeriod)

        if priceList[periodEndDay] > averageOfPeriod:
            indicatorList.append('+')
        elif priceList[periodEndDay] < averageOfPeriod:
            indicatorList.append('-')
        else:
            indicatorList.append('')
    return averageList, indicatorList


'''
    Calculate and return a list of indicators like 0, n, or -n.
'''
def directionalIndicator(priceList, period):
    indicatorList = []
    tempList = [0] # first day contains 0.
    days = len(priceList)
    periodEndDay = -1

    for newDay in range(1, days):
        if priceList[newDay] > priceList[newDay - 1]:
            tempList.append(1)
        elif priceList[newDay] < priceList[newDay - 1]:
            tempList.append(-1)
        else:
            tempList.append(0)

    for day in range(days):
        if day < period:
            indicatorList.append(sum(tempList[: day + 1]))
        else:
            indicatorList.append(sum(tempList[day - period + 1 : day + 1]))

    return indicatorList
