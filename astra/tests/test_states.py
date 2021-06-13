
import unittest
from unittest.mock import Mock
import timeout_decorator
import io

#These 2 lines allow the test to import files from src
from sys import path
path[0] += "/src"

from state_machine import flight, postflight
from serialisation import NORMAL

class TestStates(unittest.TestCase):
    
    #Flight tests
    def test_flight_uses_normal_buffer(self):
        buffer = Mock()
        sensors = Mock()
        state = flight(buffer, sensors)

        sensors.get = Mock(return_value = [100]*9)
        @timeout_decorator.timeout(0.01)
        def run_state():
            state.run()
        run_state()

        buffer.set_mode.assert_called_once_with(NORMAL)

    
    #Note this is subject to change
    def test_flight_uses_postflight_when_buffer_full(self):
        ...
    
    @timeout_decorator.timeout(0.01)
    def run_postflight(self, state):
        #Disables printing for this code
        with unittest.mock.patch('sys.stdout', new = io.StringIO()):
            state.run()

    #Postflight tests
    def test_nothing_happens_in_postflight(self):
        buffer = Mock()
        sensors = Mock()
        state = postflight()

        try:
            self.run_postflight(state)
        except timeout_decorator.timeout_decorator.TimeoutError:
            pass

        sensors.get.assert_not_called()
        buffer.write.get.assert_not_called()
