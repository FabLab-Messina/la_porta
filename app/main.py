from evtmgr import EventManager

from webservice import WebService
from serialcom import SerialCom


def open_porta( who ):
    if mod_arduino.send_packet('porta', action='unlock'):
        print('porta aperta! ;)')
    else:
        print('porta chiusa :(')


event_manager = EventManager()
mod_webserver = WebService( event_manager )
mod_arduino = SerialCom( event_manager, '/dev/ttyATH0', 115200 )

event_manager.listen_event('on_porta_unlock_request', open_porta)

mod_webserver.start()
