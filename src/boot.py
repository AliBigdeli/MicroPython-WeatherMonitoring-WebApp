import network

ssid = 'MicroPython-AP'
password = '123456789'

ap_wlan = network.WLAN(network.AP_IF)
ap_wlan.active(True)
ap_wlan.config(essid=ssid, password=password)

while ap_wlan.active() == False:
  pass

print('Connection successful')
print(ap_wlan.ifconfig())