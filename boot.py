# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
import wifi

wifi.do_connect()

import upip
#print("installation.........")
#upip.install("micropython-firebase-firestore")