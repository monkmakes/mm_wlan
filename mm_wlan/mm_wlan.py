"""
mm_wlan
--------
The ``mm_wlan`` module defines a couple of methods to simplify connecting to a 
wireless network. https://github.com/monkmakes/mm_wlan

"""


import network, time, sys

wlan = network.WLAN(network.STA_IF)

def connect_to_network(ssid, password, retries=10, verbose=True):
    wlan.active(True)
    if sys.platform != 'esp32':
        wlan.config(pm = 0xa11140)  # Disable power-save mode
    wlan.connect(ssid, password)
    if verbose: print('Connecting to ' + ssid, end=' ')
        
    while retries > 0 and wlan.status() != network.STAT_GOT_IP:
        retries -= 1
        if verbose: print('.', end='')
        time.sleep(1)    
        
    if not is_connected():
        if verbose: print('\nConnection failed. Check ssid and password')
        raise RuntimeError('WLAN connection failed')
    else:
        if verbose: print('\nConnected. IP Address = ' + get_ip())

def get_ip():
    if is_connected():
        return wlan.ifconfig()[0]
    else:
        if verbose: print('\nNot connected')
        return None
        

def is_connected():
    return wlan.status() == network.STAT_GOT_IP

