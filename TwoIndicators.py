# TwoIndicators.py
#
# Author: Yuhong Li
#
# Created on 02/20/2013
# Final Edited on 09/07/2017
# ----------------------------------------


'''
    Calculate and return a list of indicators like '', '+', or '-'.
'''
def simple_moving_average_indicator(price_list, period):
    average_list = ['' for i in range(period - 1)]
    indicator_list = ['' for i in range(period - 1)]
    period_end_day = -1

    days = len(price_list)

    for period_start_day in range(days - period + 1):
        period_end_day = period_start_day + period - 1

        average_of_period = sum(price_list[period_start_day : period_end_day + 1]) / period
        average_list.append("%.2f" % average_of_period)

        if price_list[period_end_day] > average_of_period:
            indicator_list.append('+')
        elif price_list[period_end_day] < average_of_period:
            indicator_list.append('-')
        else:
            indicator_list.append('')
    return average_list, indicator_list


'''
    Calculate and return a list of indicators like 0, n, or -n.
'''
def directional_indicator(price_list, period):
    indicator_list = []
    temp_list = [0] # first day contains 0.
    days = len(price_list)
    period_end_day = -1

    for new_day in range(1, days):
        if price_list[new_day] > price_list[new_day - 1]:
            temp_list.append(1)
        elif price_list[new_day] < price_list[new_day - 1]:
            temp_list.append(-1)
        else:
            temp_list.append(0)

    for day in range(days):
        if day < period:
            indicator_list.append(sum(temp_list[: day + 1]))
        else:
            indicator_list.append(sum(temp_list[day - period + 1 : day + 1]))

    return indicator_list
