
import unittest
from unittest.mock import Mock

# from src.main import preflight, flight, postflight

class TestStates(unittest.TestCase):
    
    #Preflight tests
    def test_preflight_uses_ring_buffer(self):
        ...

    def test_preflight_ends_when_acceleration_gt_ACCEL_THRESH(self):
        ...
    
    #Flight tests
    def test_flight_uses_normal_buffer(self):
        ...
    
    #Note this is subject to change
    def test_flight_uses_ends_when_buffer_full(self):
        ...
    
    #Postflight tests
    def test_nothing_happens_in_postflight(self):
        ...
