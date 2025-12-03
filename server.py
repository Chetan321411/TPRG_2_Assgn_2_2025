import socket
import os
import json

# Create socket server
s = socket.socket()
host = ''       # listen on all interfaces
port = 5000
s.bind((host, port))
s.listen(5)

print("Server running... waiting for client")

# ---- FUNCTIONS FOR 5 PARAMETERS ----

def get_temp():
    t = os.popen("vcgencmd measure_temp").readline()
    return t.strip()

def get_voltage():
    v = os.popen("vcgencmd measure_volts").readline()
    return v.strip()

def get_clock():
    c = os.popen("vcgencmd measure_clock arm").readline()
    return c.strip()

def get_gpu_freq():
    g = os.popen("vcgencmd measure_clock v3d").readline()
    return g.strip()

def get_mem():
    m = os.popen("vcgencmd get_mem arm").readline()
    return m.strip()

# MAIN SERVER LOOP
while True:
    c, addr = s.accept()
    print("Connected from:", addr)

    data_dict = {
        "Temperature": get_temp(),
        "Voltage": get_voltage(),
        "ARM Clock": get_clock(),
        "GPU Clock": get_gpu_freq(),
        "ARM Memory": get_mem()
    }

    json_bytes = json.dumps(data_dict).encode('utf-8')
    c.send(json_bytes)
    c.close()
