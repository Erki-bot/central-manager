import ufirestore.ufirestore as firebase
from ufirestore.json import FirebaseJson
import json
import pzem
from time import sleep as delay
import random
#Project parameters
url = "https://central-manager-4d063-default-rtdb.firebaseio.com/"


#firebase configuration
firebase.setURL(url)
# response = firebase.push("/test","dk", id=0)
# print(response)
while True:
    try:
        # read electrical mesure
        measures = pzem.json_measures()
        response = firebase.push("/electrical_value",measures, id=0,bg = False)
    except:
        print("some error occured")
    
    delay(2)
  
