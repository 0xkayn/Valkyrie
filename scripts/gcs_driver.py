from connection import *


#gcs = MavshGCS('/dev/ttyACM0')
gcs = MavshGCS('udpout:192.168.1.4:8888')
print(gcs)
heartbeat = gcs.wait_heartbeat()
print(heartbeat)
# i think we need to init inside the loop
import sys

try:        
    gcs.loop.run_forever()

except KeyboardInterrupt:
    gcs.request_mavsh_shutdown()

"""
try:
    gcs.mavsh_init()
    gcs.message_loop()
"""
