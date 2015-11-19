
import unittest

from evtmgr import EventManager

class EventManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.event_manager = EventManager()


    def test_register_events(self):
        self.assertTrue( self.event_manager.register_event('on_test1') )
        self.assertTrue( self.event_manager.register_event('on_test2') )
        self.assertFalse( self.event_manager.register_event('on_test2') ) #multiple insertion


    def test_listening(self):
        self.event_manager.register_event('on_test1')
        self.event_manager.register_event('on_test2')

        self.assertTrue( self.event_manager.listen_event('on_test1', self.func1) )
        self.assertTrue( self.event_manager.listen_event('on_test2', self.func1) )
        self.assertFalse( self.event_manager.listen_event('on_test3', self.func1) ) #event not registered
        self.assertFalse( self.event_manager.listen_event('on_test1', self.func1) ) #multiple listening


    def func1(self, who):
        who._itworks = True
        

    def test_triggering(self):
        self.event_manager.register_event('on_test1')
        self.event_manager.register_event('on_test2')
        self.event_manager.register_event('on_test3')
        self.event_manager.listen_event('on_test1', self.func1)
        self.event_manager.listen_event('on_test2', self.func1)

        self.assertTrue( self.event_manager.trigger_event('on_test1', self) )
        self.assertTrue( self.event_manager.trigger_event('on_test2', self) )
        self.assertTrue( self.event_manager.trigger_event('on_test3', self) ) #no one listening
        self.assertFalse( self.event_manager.trigger_event('on_test7', self) ) #event not registered

        self.assertTrue( self._itworks ) #function has executed if true


if __name__ == '__main__':
    unittest.main()
