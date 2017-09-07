# DownloadData.py
#
# Author: Yuhong Li
#
# Created on 02/20/2013
# Final Edited on 09/07/2017
# ----------------------------------------

import urllib.request


class InvalidError(Exception):
    pass


'''
   Receive data according to the input symbol, start date, and end date.
    If it fails, an error will be raised.
'''
def download_data_from_server(symbol, start_date, end_date):
	start_year, start_month, start_day = date_converter(start_date)
	end_year, end_month, end_day = date_converter(end_date)

	# According to the Yahoo Finance API, we need to modify the startMonth and
    #  endMonth to get correct data.
	start_month = int(start_month) - 1
	end_month = int(end_month) - 1

	urlInfo = "http://ichart.yahoo.com/table.csv?" + "s={0}&a={1}&b={2}&c={3}&d={4}&e={5}&f={6}&g=d"
	url = urlInfo.format(symbol, start_month, start_day, start_year, end_month, end_day, end_year)

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
def date_converter(date):
	date_info = date.split('-')
	year, month, day = date_info[0], date_info[1], date_info[2]
	return year, month, day


'''
    It takes decoded data downloaded from the Internet, seperate
     date and closed price out, and returns a dateList and priceList.
'''
def get_time_list_and_price_list(reversed_decoded_data):
	time_list, price_list = [], []

	for raw_daily_info in reversed_decoded_data[1:]:
		daily_info = raw_daily_info.strip('\n').split(',')
		time_list.append(daily_info[0])
		price_list.append(eval(daily_info[4]))

	time_list.reverse()
	price_list.reverse()

	return time_list, price_list