import ufirestore.ufirestore as firebase
from machine import Pin
import pzem
from time import sleep as delay

#Project parameters
url = "https://central-manager-4d063-default-rtdb.firebaseio.com/"


error_led = Pin(2,Pin.OUT)
#firebase configuration
firebase.setURL(url)
# response = firebase.push("/test","dk", id=0)
# print(response)
while True:
    error_led.value(True)
    try:
        # read electrical mesure
        measures = pzem.json_measures()
        response = firebase.push("/electrical_value",measures,bg = False, id = 0  )
        error_led.value(False)
    except:
        error_led.value(True)
        print("some error occured")
    
    delay(2)
  



