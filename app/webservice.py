from bottle import Bottle, route


class WebService:

    def __init__(self, event_manager):

        self._event_manager = event_manager
        self._event_manager.register_event('on_porta_open_request')

        self._webservice = Bottle()
        self._setup_routing()


    def _setup_routing(self):
        self._webservice.route('/fablab/porta/<action>', method="GET", callback=self._manage_porta)
        

    def get_status(self):

        # restituisce informazioni su quale sia lo status del servizio
        # in modo strutturato (verra' tramutato in json)

        pass


    def start(self, host='localhost', port=8080):
        self._host = host
        self._port = port
        self._webservice.run( host=self._host, port=self._port )


    def _manage_porta(self, action):
        if action == 'open':
            self._event_manager.trigger_event('on_porta_open_request', self)

