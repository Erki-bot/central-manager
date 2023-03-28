def do_connect():
    import network
    from time import sleep
    # SSID and password
    #ssid = "Redmi Note 10"
    #password = "00949612"
    
    ssid = "RightNetwork"
    password = "#80b42C8q@9vhqJHb5XtX1"
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...',end = "...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            print(end = ".")
            sleep(1)
            pass
    print('network config:', wlan.ifconfig())