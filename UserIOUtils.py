# UserIOUtils.py
#
# Author: Yuhong Li
#
# Created on 02/20/2013
# Final Edited on 09/07/2017
# ----------------------------------------


import datetime


'''
    Ask user to enter a stock symbol.
'''
def ask_for_stock_symbol():
    info = "Please enter the stock symbol: "
    user_input = ''
    while True:
        try:
            user_input = ask_for_user_input(info, "str").upper()
            check_input_contains_alphabet_only(user_input)
            return user_input
        except Exception as error:
            print("Invalid stock symbol. Please try again.")


'''
    Ask user for start date.
'''
def ask_for_start_date():
    info = "Please enter the start date in the format 'YYYY-MM-DD': "
    start_date = ""
    while True:
        try:
            start_date = input(info)
            check_correct_start_date(start_date)
            return transfer_date(start_date)
        except Exception as error:
            print("Invalid start date. Please try again.")


'''
    Ask user for end date.
     The end date should be after the start date, or it will be
     considered as an invalid date.
'''
def ask_for_end_date(start_date):
    info = "Please enter the end date in the format'YYYY-MM-DD': "
    end_date = ''
    while True:
        try:
            end_date = input(info)
            check_correct_end_date(end_date, start_date)
            return transfer_date(end_date)
        except Exception as error:
            print("Invalid end date. Please try again.")


'''
    Ask user for signal strategy.
'''
def ask_for_signal_strategy():
    info = "Please enter the signal strategy.\n\t1)Simple moving average;"\
           + "\n\t2)Directional indicator;\nYour choice (1/2): "
    strategy = -1
    while True:
        try:
            strategy = ask_for_user_input(info, "int")
            check_user_input_under_count_limit(strategy, 2)
            return strategy
        except Exception as error:
            print("Invalid strategy. Please try again.")


'''
    Ask user for how many days they want to check as a period.
'''
def ask_for_period():
    info = "Please enter how many days you want to check as a period: "
    period = -1
    while True:
        try:
            period = ask_for_user_input(info, "int")
            check_period_greater_than_zero(period)
            return period
        except Exception as error:
            print("Invalid period. Please try again.")


'''
    Ask user for buy and sell signals.
'''
def ask_for_buy_and_sell_signals():
    info1 = "Please enter buy signal: "
    info2 = "Please enter sell signal: "
    buy_signal, sell_signal = -1, -1
    while True:
        try:
            buy_signal = ask_for_user_input(info1, "int")
            sell_signal = ask_for_user_input(info2, "int")
            return buy_signal, sell_signal
        except Exception as error:
            print("Invalid buy/sell signal. Please try again.")


'''
    Ask user if he/she wants to restart.
'''
def ask_for_restart():
    info = "\nDone! Want to restart the program? 1) Yes; 2) No (1/2): "
    response = -1
    while True:
        try:
            response = ask_for_user_input(info, "int")
            check_user_input_under_count_limit(response, 2)
            return response
        except Exception as error:
            print("Invalid response. Please try again.")




#----------------------------------------------------------------


# INPUT STRING UTILS #


'''
    Asks user to enter the information in specific format.
     It will ask user to retry if he/she gives an invalid input.
'''
def ask_for_user_input(info, typeLimit):
    try:
        response = input(info)
        result = eval(typeLimit)(response)
        return result
    except Exception as Error:
        print("Invalid type. Please try again.")


'''
    Check if input contains letters only.
'''
def check_input_contains_alphabet_only(user_input):
    assert(user_input.isalpha())


'''
    Check if user input is under count limit.
'''
def check_user_input_under_count_limit(user_input, limit):
    assert(0 < user_input <= limit)




# INPUT DATE UTILS #


'''
    Check if start date's format is correct, and it is on or before today.
'''
def check_correct_start_date(start_date):
    check_correct_date_format(start_date)
    check_date_is_or_before_today(start_date)


'''
    Check if end date's format is correct, and it is later than start date
'''
def check_correct_end_date(end_date, start_date):
    check_correct_start_date(end_date)
    check_end_date_is_after_start_date(end_date, start_date)


'''
    Check if input date is in correct Date format (YYYY-MM-DD).
'''
def check_correct_date_format(date):
    datetime.datetime.strptime(date, "%Y-%m-%d")
    date_list = date.split('-')
    assert(len(date_list[0]) == 4 \
           and len(date_list[1]) == 2 and len(date_list[2]) == 2)


'''
    Check if the input date is on or before today.
'''
def check_date_is_or_before_today(date):
    input_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    current_date = datetime.datetime.today()
    assert(input_date <= current_date)


'''
    Check if the end date is after the start date.
'''
def check_end_date_is_after_start_date(end_date, start_date):
    starting_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    ending_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    assert(ending_date > starting_date)


'''
    Check if period is greater than 0.
'''
def check_period_greater_than_zero(period):
    assert(period > 0)


'''
    Transfer MM and/or DD from two digits to one if they are smaller than 10.
'''
def transfer_date(date):
    date_list = date.split('-')
    return date_list[0] + '-' + str(int(date_list[1])) + '-' + str(int(date_list[2]))




# OUTPUT UTILS #


'''
    Print result for simple moving average.
'''
def print_simple_moving_average(symbol, buy_signal, sell_signal, time_list, price_list, indicator_list, signal_list):
    strategy = "Simple Moving Average"
    print_helper(strategy, symbol, buy_signal, sell_signal, time_list, price_list, indicator_list, signal_list)


'''
    Print result for directional.
'''
def print_directional_indicator(symbol, buy_signal, sell_signal, time_list, price_list, indicator_list, signal_list):
    strategy = "Directional Indicator"
    print_helper(strategy, symbol, str(buy_signal), str(sell_signal), time_list, price_list, purify_indicator_list(indicator_list), signal_list)


'''
    Print helper.
'''
def print_helper(strategy, symbol, buy_signal, sell_signal, time_list, price_list, indicator_list, signal_list):
    title = "\nSYMBOL: " + symbol + "\nSTRATEGY: " + strategy
    title += "\nBuy Above " + str(buy_signal)
    title += ", Sell Below " + str(sell_signal)
    title += "\n\nDATE" + " " * 10 + "CLOSE" + " " * 8 + "INDICATOR" + " " * 6 + "SIGNAL"
    string_format = "{:10}" + " " * 4 + "{:6.2f}" + " " * 8 + "{:11}" + " " * 4 + "{}"

    print(len(time_list), len(price_list), len(indicator_list), len(signal_list))

    print(title)
    for i in range(len(time_list)):
        print(string_format.format(time_list[i], price_list[i], indicator_list[i], signal_list[i]))


'''
    Purify Directional Indicator's indicator_list.
'''
def purify_indicator_list(indicator_list):
    new_indicator_list = []
    for i in range(len(indicator_list)):
        if indicator_list[i] > 0:
            new_indicator_list.append('+' + str(indicator_list[i]))
        else:
            new_indicator_list.append(str(indicator_list[i]))
    return new_indicator_list
