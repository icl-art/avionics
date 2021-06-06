
import unittest
from unittest.mock import Mock
from random import random
import timeout_decorator
import io

#These 2 lines allow the test to import files from src
from sys import path
path[0] += "/src"

from state_machine import preflight, flight, postflight
from serialisation import RING, NORMAL

class TestStates(unittest.TestCase):
    
    #Preflight tests
    def test_preflight_uses_ring_buffer(self):
        buffer = Mock()
        sensors = Mock()
        sensors.get = Mock(return_value = [100]*9)
        state = preflight(buffer, sensors)
        state.run()

        buffer.set_mode.assert_called_once_with(RING)


    def test_preflight_ends_when_acceleration_gt_ACCEL_THRESH(self):
        buffer = Mock()
        sensors = Mock()
        state = preflight(buffer, sensors)
        
        n = 10
        data = []
        for _ in range(n-1):
            x, y, z = random(), random(), random()
            while x*x + y*y + z*z > state.ACCEL_THRESH:
                x, y, z = random(), random(), random()
            data.append([0, 0, 0, x, y, z, 0, 0, 0])
        root_mag = (state.ACCEL_THRESH/3) ** 0.5
        data.append([0, 0, 0, root_mag, root_mag, root_mag, 0, 0, 0])

        sensors.get = Mock(side_effect=data)
        next_state = state.run()

        assert sensors.get.call_count == n
        assert buffer.write.call_count == n
        assert isinstance(next_state, flight)

    
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

        buffer.set_mode.assert_called_once_with(RING)

    
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
