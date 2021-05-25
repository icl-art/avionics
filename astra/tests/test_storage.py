from typing import Tuple
import unittest
from unittest.mock import Mock
import struct

from src.serialisation import storage, NORMAL, RING

class TestStorage(unittest.TestCase):

    def init_normal_buffer(self) -> Tuple[Mock, storage]:
        file = Mock()
        st = storage(2*5*4, 0, file)
        st.set_mode(NORMAL)
        return file, st

    def init_ring_buffer(self) -> Tuple[Mock, storage]:
        file = Mock()
        st = storage(0, 5*4, file)
        st.set_mode(RING)
        return file, st        

    #Normal Mode tests
    def test_data_not_dumped_when_not_full(self):
        file, st = self.init_normal_buffer()
        for _ in range(4):
            st.write([1.0, 2.0])
        file.write.assert_not_called()
 
    def test_data_dumped_on_full(self):
        file, st = self.init_normal_buffer()
        for _ in range(6):
            st.write([1.0, 2.0])

        file.write.assert_called_once()

    def test_data_dumped_on_close(self):
        file, st = self.init_normal_buffer()
        st.write([1.0, 2.0])
        st.close()

        file.write.assert_called_once()
        file.close.assert_called_once()

    #Ring Mode tests
    #Note normal python runs with 64 bit floats rather than 32 bit floats that micropython uses
    def test_adding_below_max_doesnt_overrite(self):
        file, st = self.init_ring_buffer()

        buf = bytearray(5*4)
        for i in range(3):
            st.write([i])
            buf[4*i:] = struct.pack("f", i)
        
        st.flush()

        file.write.assert_called_once_with(buf)

    def test_adding_above_max_overrites_data(self):
        file, st = self.init_ring_buffer()

        buf = bytearray(5*4)
        for i in range(6):
            st.write([i])
            buf[4*i:] = struct.pack("f", i)
        
        st.flush()

        try:
            file.write.assert_called_once_with(buf)
        except AssertionError:
            return

        raise Exception("Expected buffer to overflow")