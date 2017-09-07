# SignalStrategies.py
#
# Author: Yuhong Li
#
# Created on 02/20/2013
# Final Edited on 09/07/2017
# ----------------------------------------


import TwoIndicators


class SimpleMovingAverage:

	def __init__(self, price_list, period):
		self.price_list = price_list
		self.period = period
		self.days = len(price_list)

	def execute(self):
		signal_list = []
		average_list, indicator_list = TwoIndicators.simple_moving_average_indicator(self.price_list, self.period)

		for day in range(1, self.days):
			# if indicator changes from '+' to '-'
			if indicator_list[day - 1] == '+' and indicator_list[day] == '-':
				signal_list.append('SELL')

            # if indicator changes from '-' to '+'
			if indicator_list[day - 1] == '-' and indicator_list[day] == '+':
				signal_list.append('BUY')

			else:
				signal_list.append('')

		return average_list, signal_list


class DirectionalIndicator:

	def __init__(self, price_list, period, buy_signal, sell_signal):
		self.price_list = price_list
		self.period = period
		self.days = len(price_list)
		self.buy_signal = buy_signal
		self.sell_signal = sell_signal

	def execute(self):
		signal_list = []
		indicator_list = TwoIndicators.directional_indicator(self.price_list, self.period)

		for day in range(self.days):
			if indicator_list[day] > self.buy_signal and day != 0:
				signal_list.append('BUY')
			elif indicator_list[day] < self.sell_signal and day != 0:
				signal_list.append('SELL')
			else:
				signal_list.append('')

		return indicator_list, signal_list
