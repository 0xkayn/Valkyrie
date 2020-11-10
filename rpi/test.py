from pymavlink import mavutil
from dronekit import connect


"""
Command Channel
    channel_number -
    min
    max
    trim

    RC8
    RC8_MAX
    RC8_MIN
"""
#mavutil.mavlink20

# Start a connection listening to a UDP port
#conn = mavutil.mavlink_connection('udpin:172.16.123.173:14550')


# Connect to the Vehicle using dronekit "connection string" (in this case an address on network)
#conn = connect('udp:0.0.0.0:14550')
#vehicle = connect('/dev/ttyACM0')


# Wait for the first heartbeat 
#   This sets the system and component ID of remote system for the link
#xconn.wait_heartbeat()

#print("Heartbeat from system (system %u component %u)" % (conn.target_system, conn.target_system))

# Once connected, use 'the_connection' to get and send messages

    #while True:
    #print(conn.recv_match(blocking=True))
    #print()
#Create a message listener for all messages.

#def start_scan():

# decorator to access channel values through mavlink
"""
@vehicle.on_message('RC_CHANNELS_RAW')
def rc(self, name, message):
    #print(f'{message}')    
    print(f'c8: {message.chan8_raw}')

    # to control the commands we need the command channels low, trim and high values
    # if value high run command, if value low then stop


    # if command channel is toggled on, run the command 
    # if command was run then dont do anything until the command channel is toggled off
    # once OFF, kill the child process and save results of command to file
    # store command results in a buffer 
"""

command_channel = 8
#command_min = vehicle.parameters[f'RC{command_channel}_MIN']
command_min = f'RC{command_channel}_MIN'
command_max = f'RC{command_channel}_MAX'
command_trim = f'RC{command_channel}_TRIM'


print(command_min)
print(vehicle.parameters[f'RC{command_channel}_MIN'])



@vehicle.on_attribute('channels')
def ch8(self,attr_name,value):
    print(value)
    print(value['8'])
#for value in vehicle.parameters.items():
#    print(value)
while True:
    continue
    #print(vehicle.channels['8'])
    