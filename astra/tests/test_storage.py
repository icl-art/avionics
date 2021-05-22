import unittest
from unittest.mock import Mock

from src.serialisation import storage

class TestStorage(unittest.TestCase):
    
    def test_data_not_dumped_when_not_full(self):
        file = Mock()
        st = storage(5*8, file)

        for _ in range(4):
            st.write([1.0, 2.0])
        file.write.assert_not_called()

    def test_data_dumped_on_full(self):
        file = Mock()
        st = storage(5*8, file)

        for _ in range(6):
            st.write([1.0, 2.0])

        file.write.assert_called_once()

    def test_data_dumped_on_close(self):
        file = Mock()
        st = storage(5*8, file)
        st.write([1.0, 2.0])
        st.close()

        file.write.assert_called_once()
        file.close.assert_called_once()