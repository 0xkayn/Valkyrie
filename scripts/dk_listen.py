from pymavlink import mavutil
from dronekit import connect

# Connect to the Vehicle using dronekit "connection string" (in this case an address on network)
vehicle = connect('udp:0.0.0.0:14550')

# Wait for the first heartbeat 
# This sets the system and component ID of remote system for the link

#Create a message listener for all messages.

@vehicle.on_message('HEARTBEAT')
def listener(self, name, message):
    print(f'message: {message}')

@vehicle.on_message('RC_CHANNELS')
def rc_channel(self, name, message):
    pass

@vehicle.on_message('PARAM_VALUE')
def params(self, name, message):
    pass

#@vehicle.on_message('*')
#def other(self, name, message):
#    print(f'message: {message}')

while True:
    continue


    
