import ufirestore.ufirestore as firebase
from ufirestore.json import FirebaseJson
import json
import pzem
#Project parameters
url = "https://central-manager-4d063-default-rtdb.firebaseio.com/"


#firebase configuration
firebase.setURL(url)
response = firebase.put("/test","dk", id=0)
print(response)
if True:
    try:
        #read all measures in one time
        all_measures = pzem.read_measures()
        print(all_measures)
        #split and print measues
        voltage = all_measures[0]/10.0
        print('U = ' + str(voltage) + ' V')
        current = ((all_measures[2]<<16) |  (all_measures[1]))/1000.0
        print('I = ' + str(current) + ' A')
        power = ((all_measures[4]<<16) |  (all_measures[3]))/10.0
        print('P = ' + str(power) + 'W')
        energy = ((all_measures[6]<<16) |  (all_measures[5]))/1000.0
        print('E = ' + str(energy) + 'kWh')
        freq = all_measures[7]/10.0
        print('freq@@@@ = ' + str(freq) + ' Hz')
        pf = all_measures[8]/10.0
        print('power factor = ' + str(pf))
        data =json.load('{"voltage":"'+voltage+'"}')
        response = firebase.put("/test",data, id=0)
    except:
        #something wrong
        print('pzem04 reading error')
        
    #delay some seconds
    time.sleep(5)
