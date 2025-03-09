import unittest
from typing import List


def max_additional_diners(n: int, k: int, s: List[int]) -> int:
    """Compute the maximum number of additional diners that can be seated."""
    # Sort the occupied seats.
    s.sort()
    additional: int = 0
    # Left gap: seats from 1 up to s[0]-1.
    left_gap: int = s[0] - 1
    additional += left_gap // (k + 1)
    # Middle gaps: for each adjacent pair, skip the k seats on the right
    # of the left diner. The gap between s[i] and s[i+1] is:
    #   gap = s[i+1] - s[i] - 1 - k
    # Only if gap is positive can we seat additional diners.
    for i in range(len(s) - 1):
        gap: int = s[i + 1] - s[i] - 1 - k
        if gap > 0:
            additional += gap // (k + 1)
    # Right gap: seats from s[-1]+1 up to n.
    right_gap: int = n - s[-1]
    additional += right_gap // (k + 1)
    return additional


class TestSocialDistancing(unittest.TestCase):

    def test_sample1(self) -> None:
        n: int = 10
        k: int = 1
        s: List[int] = [2, 6]
        expected: int = 3
        self.assertEqual(max_additional_diners(n, k, s), expected)

    def test_sample2(self) -> None:
        n: int = 15
        k: int = 2
        s: List[int] = [11, 6, 14]
        expected: int = 1
        self.assertEqual(max_additional_diners(n, k, s), expected)

    def test_no_gap(self) -> None:
        # Case where existing diners block all possible seats.
        n: int = 5
        k: int = 1
        s: List[int] = [2, 4]
        expected: int = 0
        self.assertEqual(max_additional_diners(n, k, s), expected)

    def test_k_zero(self) -> None:
        # With k = 0, all empty seats are available.
        n: int = 10
        k: int = 0
        s: List[int] = [2, 5, 7]
        expected: int = 7  # 10 - 3 occupied seats.
        self.assertEqual(max_additional_diners(n, k, s), expected)

    def test_edge_case(self) -> None:
        # Single diner at seat 10 in a 20-seat table with k = 2.
        n: int = 20
        k: int = 2
        s: List[int] = [10]
        # Left gap: (10-1)=9, 9//3 = 3.
        # Right gap: (20-10)=10, 10//3 = 3.
        # Total additional = 3 + 3 = 6.
        expected: int = 6
        self.assertEqual(max_additional_diners(n, k, s), expected)


if __name__ == '__main__':
    unittest.main()
