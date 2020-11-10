import configparser 
from dronekit import Vehicle

config = configparser.ConfigParser()
config.read('valkyrie.cfg')

class CommandChannel():
    
    def __init__(self):    
        #super(CommandChannel,self).__init__(*args)
        """
        num: rc channel number which should control "command mode"
        min: lowest raw value that can be from the transmitter on this channel
        max: largest raw value that can be sent from the transmitter on this channel
        trim: median of min and max

        note - min, max and trim are all configured in your ground control software but slight variations occur 

        status: 0 if command mode is off, 1 if its on. Set to off by default.
        param_*: ardupilot parameter value names associated with the command channel
        """
        self.status = 0 
        self.num = config['COMMAND']['channel']
        self.min = int(config['COMMAND']['min'])
        self.max = int(config['COMMAND']['max'])
        self.trim = int(config['COMMAND']['trim'])     
        self.param_min = f'RC{self.num}_MIN'
        self.param_max = f'RC{self.num}_MAX'
        self.param_trim = f'RC{self.num}_TRIM'


class Valkyrie(Vehicle):
    def __init__(self, *args):
        super(Valkyrie, self).__init__(*args)

        # Create an Vehicle.raw_imu object with initial values set to None.
        self.command_channel = CommandChannel()
            
        #message listener for rc channel updates
        @self.on_attribute('channels')
        def toggle_command_mode(self,attr_name,value):
            """
            if command mode channel is toggled on this listener will set command mode status on
            padding of +-50 is given for the raw rc data 
            """             
            command_channel_val = value[self.command_channel.num]
            if command_channel_val >= (self.command_channel.max - 50):
                print('entering command mode')
                self.command_channel.status = 1
            elif command_channel_val <= (self.command_channel.min + 50):
                print('exiting command mode')
                self.command_channel.status = 0

            #self.notify_attribute_listeners('channels')
        
      

    #@property
    #def raw_imu(self):
    #    return self._raw_imu
