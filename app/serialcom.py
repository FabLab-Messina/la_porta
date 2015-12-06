from serial import Serial

targets = {
    'porta': {
        'id': 0x01,
        
        'actions': {
            'unlock': 0x01
        }
    }
}

class SerialCom:

    def __init__(self, event_manager, port='/dev/ttyS0', baud=9600):

        self._event_manager = event_manager
        #self._event_manager.register_event('on_porta_unlock') TODO

        self._port = port
        self._baud = baud
        self._serial = Serial( self._port, self._baud )
        self._busy = False


    def get_status(self):
        pass


    def send_packet(self, target, action=None, payload=None):
        if action == None and payload == None:
            raise Exception('Need to specify an action or a payload for the given target.')
        # if an action is specified will override the payload usage
        
        if target in targets:
            if action != None and action in targets[target]['actions']:
                if not self._busy: self._busy = True # quick and dirty

                packet = bytearray( '\xAA' )
                packet += bytearray( [ targets[target]['id'] ] )
                packet += bytearray( [ 1, targets[target]['actions'][action] ] )
                packet += bytearray( '\xBB\xCC\xDD' )

                self._serial.write(packet)

                self._busy = False
                return True
                
            elif payload != None and action in targets[target]:
                pass
                
                #return True

            else:
                return False
        else:
            return False


    def receive_packet(self):
        pass

