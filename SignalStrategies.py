# SignalStrategies.py
#
# Author: Yuhong Li
#
# Created on 02/20/2013
# Final Edited on 04/10/2017
# ----------------------------------------

import TwoIndicators


class SimpleMovingAverage:

    def __init__(self, priceList, period):
        self.priceList = priceList
        self.period = period
        self.days = len(priceList)

    def execute(self):
        signalList = []
        averageList, indicatorList = TwoIndicators.simpleMovingAverageIndicator(self.priceList, self.period)

        for day in range(1, self.days):
            # if indicator changes from '+' to '-'
            if indicatorList[day - 1] == '+' and indicatorList[day] == '-':
                signalList.append('SELL')

            # if indicator changes from '-' to '+'
            if indicatorList[day - 1] == '-' and indicatorList[day] == '+':
                signalList.append('BUY')

            else:
                signalList.append('')

        return averageList, signalList


class DirectionalIndicator:

    def __init__(self, priceList, period, buySignal, sellSignal):
        self.priceList = priceList
        self.period = period
        self.days = len(priceList)
        self.buySignal = buySignal
        self.sellSignal = sellSignal

    def execute(self):
        signalList = []
        indicatorList = TwoIndicators.directionalIndicator(self.priceList, self.period)

        for day in range(self.days):
            if indicatorList[day] > self.buySignal and day != 0:
                signalList.append('BUY')
            elif indicatorList[day] < self.sellSignal and day != 0:
                signalList.append('SELL')
            else:
                signalList.append('')

        return indicatorList, signalList
