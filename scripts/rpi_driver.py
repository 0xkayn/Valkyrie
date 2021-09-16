from connection import *
from mavsh_exceptions import * 
import asyncio

rpi = MavshCompanion('/dev/ttyS0')
print(rpi)
heartbeat = rpi.wait_heartbeat()
print(heartbeat)

try:
    rpi.message_loop()
    rpi.loop.run_forever()

except SessionExistsException:
    pass
