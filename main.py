# main.py
#
# Author: Yuhong Li
#
# Created on 02/20/2013
# Final Edited on 09/07/2017
# ----------------------------------------


import DownloadData
import SignalStrategies
import UserIOUtils


def execute_program():
	while True:
		stock_symbol, time_list, price_list = build_connection()
		strategy, period, buy_signal, sell_signal, indicator_list, signal_list = indicator_and_signal(price_list)

		if strategy == 1:
			UserIOUtils.print_simple_moving_average(stock_symbol, buy_signal, sell_signal, time_list, price_list, indicator_list, signal_list)
		else:
			UserIOUtils.print_directional_indicator(stock_symbol, buy_signal, sell_signal, time_list, price_list, indicator_list, signal_list)

		response = UserIOUtils.ask_for_restart()
		if response == 2:
			print("\nThank you! Have a nice day!")
			break


'''
    Ask user for input, connect to the Internet, and download data.
'''
def build_connection():
	while True:
		try:
			stock_symbol = UserIOUtils.ask_for_stock_symbol()
			start_date = UserIOUtils.ask_for_start_date()
			end_date = UserIOUtils.ask_for_end_date(start_date)
			time_list, price_list = DownloadData.download_data_from_server(stock_symbol, start_date, end_date)
			return stock_symbol, time_list, price_list
		except Exception as error:
			print("Data download failed. Please try again.")
	print("Data download successfully.")


'''
    It takes priceList and returns a list of indicators and a list of signals.
'''
def indicator_and_signal(price_list):
	while True:
		try:
			strategy = UserIOUtils.ask_for_signal_strategy()
			period = UserIOUtils.ask_for_period()

			if strategy == 1:
				buy_signal, sell_signal = '+', '-'
				SMA = SignalStrategies.simple_moving_average(price_list, period)
				indicator_list, signal_list = SMA.execute()
			else:
				buy_signal, sell_signal = UserIOUtils.ask_for_buy_and_sell_signals()
				DI = SignalStrategies.directional_indicator(price_list, period, buy_signal, sell_signal)
				indicator_list, signal_list = DI.execute()
			return strategy, period, buy_signal, sell_signal, indicator_list, signal_list
		except Exception as error:
			print("Invalid @ indicatorAndSignal. Please try again.")
            #raise error




#-----------------------
if __name__=='__main__':
    execute_program()
