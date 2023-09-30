# mm_wlan
A MicroPython module for connecting to a WLAN (WiFi network)

The module defines a couple of methods to simplify connecting to a 
wireless network. 

It makes a great companion to the [microdot](https://github.com/miguelgrinberg/microdot) light-weight web server.

I've only tested it on a Raspberry Pi Pico, but it should work on most WiFi-capable MicroPython boards.

# Installation

```
$ pip install mm_wlan
```

On a Pico W, you can either use Thonny's **Manage packages..** feature, or copy the file mm_wlan.py onto the Pico's file system. You can do the latter in Thonny using the **Save a Copy** option.

# Example

hello.py a minimal web server example using microdot.

``` python
from microdot import Microdot
import mm_wlan

ssid = 'my network name'
password = 'my passord'

app = Microdot()  
mm_wlan.connect_to_network(ssid, password)

@app.route('/')
def index(request):
    return 'Hello, from Pico'

app.run(port=80)
```

Make sure that both microdot.py and mm_wlan.py are copied onto your Pico W and then change **ssid** and **password** before you run hello.py. You should see something like this in your Shell. Progress is marked by dots until a connection is made or it gives up.
```
MicroPython v1.19.1 on 2022-08-11; Raspberry Pi Pico W with RP2040
Type "help()" for more information.
>>> %Run -c $EDITOR_CONTENT
Connecting to MONKMAKES_GUEST ......
Connected IP Address = 192.168.1.132
```

# Usage

```
connect_to_network(ssid, password, retries=10, verbose=True)
```

By default, the connection process will wait for 10 seconds before giving up. You can alter this by changing the optional `retries` paramater.
If you don't want the connecting messages cluttering up your Python console, then set the optional `verbose` parameter to `False`.

```
is_connected()
```
This returns True if you are connected.

For a more complex example take a look at [this example](https://github.com/monkmakes/pmon/blob/main/raspberry_pi_pico/pico_w_server.py) using the [MonkMakes Plant Monitor](https://www.monkmakes.com/pmon.html).
