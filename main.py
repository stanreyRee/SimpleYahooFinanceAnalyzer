# main.py
#
# Author: Yuhong Li
#
# Created on 02/20/2013
# Final Edited on 04/10/2017
# ----------------------------------------


import DownloadData
import SignalStrategies
import UserIOUtils


def executeProgram():
    while True:
        stockSymbol, timeList, priceList = buildConnection()
        strategy, period, buySignal, sellSignal, indicatorList, signalList = indicatorAndSignal(priceList)

        if strategy == 1:
            UserIOUtils.printSimpleMovingAverage(stockSymbol, buySignal, sellSignal, timeList, priceList,indicatorList, signalList)
        else:
            UserIOUtils.printDirectionalIndicator(stockSymbol, buySignal, sellSignal, timeList, priceList, indicatorList, signalList)

        response = UserIOUtils.askForRestart()
        if response == 2:
            print("\nThank you! Have a nice day!")
            break


'''
    Ask user for input, connect to the Internet, and download data.
'''
def buildConnection():
    while True:
        try:
            stockSymbol = UserIOUtils.askForStockSymbol()
            startDate = UserIOUtils.askForStartDate()
            endDate = UserIOUtils.askForEndDate(startDate)

            timeList, priceList = DownloadData.downloadDataFromServer(stockSymbol, startDate, endDate)

            return stockSymbol, timeList, priceList
        except Exception as error:
            print("Data download failed. Please try again.")
    print("Data download successfully.")



'''
    It takes priceList and returns a list of indicators and a list of signals.
'''
def indicatorAndSignal(priceList):
    while True:
        try:
            strategy = UserIOUtils.askForSignalStrategy()
            period = UserIOUtils.askForPeriod()

            if strategy == 1:
                buySignal, sellSignal = '+', '-'
                SMA = SignalStrategies.SimpleMovingAverage(priceList, period)
                indicatorList, signalList = SMA.execute()
            else:
                buySignal, sellSignal = UserIOUtils.askForBuyAndSellSignals()
                DI = SignalStrategies.DirectionalIndicator(priceList, period, buySignal, sellSignal)
                indicatorList, signalList = DI.execute()

            break
        except Exception as error:
            print("Invalid @ indicatorAndSignal. Please try again.")
            raise error

    return strategy, period, buySignal, sellSignal, indicatorList, signalList


if __name__=='__main__':
    executeProgram()
