from microdot import Microdot
import mm_wlan
import gc

ssid = 'my network name'
password = 'my passord'

ssid = 'Network'
password = 'password'

app = Microdot()  
mm_wlan.connect_to_network(ssid, password)

@app.route('/')
def index(request):
    return 'Hello, from Pico'

@app.route('memory')
def index(request):
    response = '<h1>Free Memory={} bytes</hi>'.format(gc.mem_free())
    return response, {'Content-Type': 'text/html'}

app.run(port=80)   
