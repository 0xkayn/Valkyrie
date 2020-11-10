#from pymavlink import mavutil
from dronekit import connect,Vehicle
from valkyrie import Valkyrie

vehicle = connect('/dev/ttyACM0',vehicle_class=Valkyrie)
#print(vehicle.parameters[f'RC{command_channel}_MIN'])

while True:
    continue

