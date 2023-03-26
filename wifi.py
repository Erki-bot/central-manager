def do_connect():
    import network
    
    # SSID and password
    ssid = "Redmi Note 10"
    password = "00949612"
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())