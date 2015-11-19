
class EventManager:

    def __init__(self):
        """Sets up the structures to manage all event interaction"""
        
        self._registered_events = []
        self._listening_tasks = {}


    def register_event(self, event_name):
        """Registers all the events that may occur"""

        if event_name not in self._registered_events:
            self._registered_events.append( event_name )
            self._listening_tasks.update( { event_name: [] } )
            
            return True
        else:
            return False


    def listen_event(self, event_name, callback):
        """Stores the procedure to execute as the event occurs"""

        if event_name in self._registered_events:
            
            if callback not in self._listening_tasks[ event_name ]:
                self._listening_tasks[ event_name ].append( callback )

                return True                   
            else:
                return False
        else:
            return False

    def trigger_event(self, event_name, who):
        """Make the event occur and executes all the associated callbacks"""

        if event_name in self._registered_events:
            for callback in self._listening_tasks[ event_name ]:
                callback(who)
            
            return True
        else:
            return False
