import sys
import os
import trader
name_code, param_console = sys.argv

def main():
    if param_console == "RESTART":
        trader.restart_param()
        print("The game is restarted, enter INFO to output commands")
    elif param_console == "NEXT":
        if os.stat("sys.json").st_size == 0:
            print("Enter RESTART")
        else:
            print("Course updated:", trader.next_param())
            trader.write_file_sys()
    elif param_console == "RATE":
        print(trader.rate_param())
    elif param_console == "BUY":
        trader.buy_param()
        trader.write_file_sys()
    elif param_console == "BUY_UAH":
        trader.buy_uah_param()
        trader.write_file_sys()
    elif param_console == "BUY_ALL":
        trader.buy_all_param()
        trader.write_file_sys()
    elif param_console == "AVAILABLE":
        trader.available_param()
    elif param_console == "SELL_ALL":
        trader.sell_all_param()
        trader.write_file_sys()
    elif param_console == "INFO":
        trader.info_param()
    else: print("There is no such command, enter INFO")

sys.exit(main()) if __name__ == '__main__' else print("error")
