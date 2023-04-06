'''
Micropython in esp32 simple example for use PZEM04t V3 in default modbus address 0xF8
whitout modbus library. Use UART1 or UART2.
2020-05-22
Jaume Nogues, jnogues@gmail.com
'''

from machine import UART
import time
import struct
import json

OFFSET_TIME = 1*60*60  # GMT+1


uart = UART(2, 9600, tx=13, rx=14)  # UART2, tx=gpio13 rx=gpio14

count = 0


def read_measures():
    signed = True
    uart.write(b'\xF8\x04\x00\x00\x00\x0A\x64\x64')  # read all raw measures
    time.sleep(0.2)
    payload = uart.read()
    # print (payload)
    payload = payload[3:-2]
    response_quantity = int(len(payload) / 2)
    fmt = '>' + (('h' if signed else 'H') * response_quantity)
    return struct.unpack(fmt, payload)


def json_measures():
    # read all measures in one time
    all_measures = read_measures()
    # print(all_measures)
    # split and print measues
    voltage = all_measures[0]/10.0
    # print('U = ' + str(voltage) + ' V')
    current = ((all_measures[2] << 16) | (all_measures[1]))/1000.0
    # print('I = ' + str(current) + ' A')
    power = ((all_measures[4] << 16) | (all_measures[3]))/10.0
    # print('P = ' + str(power) + 'W')
    energy = ((all_measures[6] << 16) | (all_measures[5]))/1000.0
    # print('E = ' + str(energy) + 'kWh')
    freq = all_measures[7]/10.0
    # print('freq@@@@ = ' + str(freq) + ' Hz')
    pf = all_measures[8]/10.0
    # print('power factor = ' + str(pf))

    # read the current date and time

    [year, month, day, hour, minute, seconde, x,
        xx] = time.localtime(time.time()+OFFSET_TIME)

    data = '{"datas":{"voltage":"'+str(voltage)+'",'
    data += '"current":"'+str(current)+'",'
    data += '"power":"'+str(power)+'",'
    data += '"energy":"'+str(energy)+'",'
    data += '"frequency":"'+str(freq)+'",'
    data += '"power_factor":"'+str(pf)+'"},'
    data += '"date":{"date":"'+str(day)+'/'+str(month)+'/'+str(year)+'",'
    data += '"time":"'+str(hour)+':'+str(minute)+':'+str(seconde)+'"},'

    d = json.loads(data)

    return d
