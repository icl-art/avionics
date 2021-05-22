import unittest

from src.ring_buffer import RingBuffer


class TestRingBuffer(unittest.TestCase):

    def test_adding_below_max_doesnt_overrite(self):
        rb = RingBuffer(5, 1)
        for i in range(3):
            rb.add([i])

        for (i, rbi) in zip(range(3), list(rb)):
            self.assertEqual(i, rbi[0])


    def test_adding_above_max_overrites_data(self):
        rb = RingBuffer(5, 1)
        for i in range(7):
            rb.add([i])
        
        rb = list(rb)
        self.assertEqual(rb[0][0], 5)
        self.assertEqual(rb[1][0], 6)
        self.assertEqual(rb[2][0], 2)
        self.assertEqual(rb[3][0], 3)
        self.assertEqual(rb[4][0], 4)


if __name__ == "__main__":
    unittest.main(arv=["first-arg-is-ignored"], exit=False)