from selenium import webdriver
from interval import Interval
from selenium.webdriver.chrome.options import Options
from fundamentals import Fundamentals
from technical_indicators import TechnicalIndicators
from gainers import Gainers
from overbought import Overbought

import urllib.request

import threading
import time

NUM_LOOPS = 500


def dispatch_fd(driver):
    index = 0
    while index < NUM_LOOPS:
        fd = Fundamentals("SIRI", driver)
        fd_data = fd.get_data()

        # Write received data to file
        with open("/srv/fundamentals", "w+") as file:
            file.write("SIRI: \n")
            for key in fd_data:
                file.write(key + ": ")
                file.write("".join(fd_data[key]) + "\n")
                file.write("\n")
        index = index + 1
    print("Fundamentals loop complete.")


def dispatch_ti(driver):
    index = 0
    while index < NUM_LOOPS:
        ti = TechnicalIndicators("SIRI", "NASDAQ", Interval.INTERVAL_1MIN, driver)
        ti_data = ti.get_data()

        # Write received data to file
        with open("/srv/technical_indicators", "w+") as file:
            file.write("SIRI: \n")
            for key in ti_data:
                file.write(key + ": ")
                file.write(" ".join(ti_data[key]) + "\n")
                file.write("\n")
        index = index + 1
    print("Technical Indicators loop complete.")


def dispatch_gr():
    index = 0
    while index < NUM_LOOPS:
        gr = Gainers()
        gr_data = gr.get_data()

        # Write received data to file
        with open("/srv/top_gainers", "w+") as file:
            for key in gr_data:
                file.write(key + ": ")
                file.write(" ".join(gr_data[key]) + "\n")
                file.write("\n")
        index = index + 1
    print("Gainers loop complete.")


def dispatch_ob():
    index = 0
    while index < NUM_LOOPS:
        ob = Overbought()
        ob_data = ob.get_data()

        # Write received data to file
        with open("/srv/overbought", "w+") as file:
            for key in ob_data:
                file.write(key + ": ")
                file.write(" ".join(ob_data[key]) + "\n")
                file.write("\n")
        index = index + 1
    print("Overbought loop complete.")


options = Options()
options.headless = True
# driver_ti = webdriver.Chrome(options=options)
driver_fd = webdriver.Chrome(options=options)

# Enter data gathering stage
# Dispatch threads to update each data set
fd_thread = threading.Thread(target=dispatch_fd, args=(driver_fd, ))
# ti_thread = threading.Thread(target=dispatch_ti, args=(driver_ti, ))
gr_thread = threading.Thread(target=dispatch_gr, args=())
ob_thread = threading.Thread(target=dispatch_ob, args=())

print("Dispatching threads...")
fd_thread.start()
# ti_thread.start()
gr_thread.start()
ob_thread.start()

# Wait for all threads to complete before proceeding with next iteration
fd_thread.join()
# ti_thread.join()
gr_thread.join()
ob_thread.join()

# driver_fd.quit()
# driver_ti.quit()
# driver_gr.quit()
# driver_ob.quit()


