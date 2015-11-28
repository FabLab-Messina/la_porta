from evtmgr import EventManager

from webservice import WebService


def open_porta( who ):
    print('porta aperta!')


event_manager = EventManager()
mod_webserver = WebService( event_manager )

event_manager.listen_event('on_porta_unlock_request', open_porta)

mod_webserver.start()
