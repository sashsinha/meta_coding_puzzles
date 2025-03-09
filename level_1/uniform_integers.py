import unittest


def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    """Return the count of uniform integers between a and b (inclusive)."""
    count = 0
    # Determine the maximum length based on B.
    max_length = len(str(B))
    # Iterate over all possible digit lengths.
    for L in range(1, max_length + 1):
        # For each digit from 1 to 9, generate the uniform number.
        for d in range(1, 10):
            num = int(str(d) * L)
            if A <= num <= B:
                count += 1
    return count


class TestCountUniformIntegers(unittest.TestCase):
    """Unit tests for the count_uniform_integers function."""

    def test_sample1(self) -> None:
        """Test case 1: A = 75, B = 300 -> Expected output: 5."""
        self.assertEqual(getUniformIntegerCountInInterval(75, 300), 5)

    def test_sample2(self) -> None:
        """Test case 2: A = 1, B = 9 -> Expected output: 9."""
        self.assertEqual(getUniformIntegerCountInInterval(1, 9), 9)

    def test_sample3(self) -> None:
        """Test case 3: A = 999999999999, B = 999999999999 -> Expected output: 1."""
        self.assertEqual(
            getUniformIntegerCountInInterval(999999999999, 999999999999), 1)


if __name__ == '__main__':
    unittest.main()
