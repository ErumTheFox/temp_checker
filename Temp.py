from time import sleep
import os

while True:
    sleep(3)
    os.system('vcgencmd measure_temp')