from microdot import Microdot, send_file, abort
from machine import ADC, Pin
from ldr_reader import LDR
import dht


DEBUG = False

photocell_pin = LDR(33)
relay_pin = Pin(26, Pin.OUT)
dht11_pin = Pin(5, Pin.IN)
dht11 = dht.DHT11(dht11_pin)
relay_pin.off()
relay_state = False

app = Microdot()


@app.route('/')
def index(request):
    return send_file('./index.html')


@app.route('/static/<path:path>')
def static(request, path):
    if '..' in path:
        abort(404)
    return send_file('static/' + path)


@app.route('/monitor/get-states')
def get_states(request):
    dht11.measure()
    temp = dht11.temperature()
    humidity = dht11.humidity()
    photocell_value = int(photocell_pin.value())

    return {
        "temperature": temp,
        "humidity": humidity,
        "light": photocell_value
    }


@app.route('/switch', methods=["GET", "POST"])
def get_states(request):
    global relay_state
    if request.method == 'GET':
        return {"state": relay_state}
    elif request.method == 'POST':
        if relay_state:
            relay_pin.off()  # Make it low
            relay_state = False
        else:
            relay_pin.on()  # Make it high
            relay_state = True

        return {"state": relay_state}


@app.errorhandler(404)
def not_found(request):
    return {'error': 'resource not found'}, 404


if DEBUG:
    app.run(debug=True)
else:
    app.run(debug=False, port=80)
