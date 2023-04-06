import ufirestore.ufirestore as firebase
from machine import Pin
import pzem

import time

# Project parameters
url = "https://central-manager-4d063-default-rtdb.firebaseio.com/"


OFFSET_TIME = 1*60*60  # GMT+1

error_led = Pin(2, Pin.OUT)
# firebase configuration
firebase.setURL(url)
# response = firebase.push("/test","dk", id=0)
# print(response)
while True:
    error_led.value(True)
    [year, month, day, hour, minute, seconde, x,
        xx] = time.localtime(time.time()+OFFSET_TIME)
    try:
        idd = year+month+day+hour*24*60+minute*60+seconde
        # read electrical mesure
        measures = pzem.json_measures()
        # print(measures)
        # d = json.loads(measures)
        response = firebase.put("/electrical_values/" +
                                str(idd), measures, bg=False, id=0)
        error_led.value(False)
    except:
        error_led.value(True)
        # print("some error occured")

    time.sleep(0.2)
