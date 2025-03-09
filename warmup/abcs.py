import unittest


def getSum(A: int, B: int, C: int) -> int:
    """Returns the sum of three integers."""
    return A + B + C


class TestGetSum(unittest.TestCase):

    def test_cases(self):
        self.assertEqual(getSum(1, 2, 3), 6)
        self.assertEqual(getSum(100, 100, 100), 300)
        self.assertEqual(getSum(85, 16, 93), 194)
        self.assertEqual(getSum(10, 20, 30), 60)
        self.assertEqual(getSum(50, 50, 50), 150)


if __name__ == '__main__':
    unittest.main()
