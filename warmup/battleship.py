from typing import List
import unittest


def get_hit_probability(R: int, C: int, G: List[List[int]]) -> float:
    """Computes the probability of hitting a battleship given the grid."""
    total_cells = R * C
    battleship_cells = sum(sum(row) for row in G)
    return battleship_cells / total_cells


class TestGetHitProbability(unittest.TestCase):

    def test_case_1(self):
        R = 2
        C = 3
        G = [[0, 0, 1], [1, 0, 1]]
        self.assertAlmostEqual(get_hit_probability(R, C, G), 0.5, places=7)

    def test_case_2(self):
        R = 2
        C = 2
        G = [[1, 1], [1, 1]]
        self.assertAlmostEqual(get_hit_probability(R, C, G), 1.0, places=7)

    def test_case_3(self):
        R = 3
        C = 3
        G = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertAlmostEqual(get_hit_probability(R, C, G), 1 / 9, places=7)

    def test_case_4(self):
        R = 4
        C = 4
        G = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
        self.assertAlmostEqual(get_hit_probability(R, C, G), 0.5, places=7)


if __name__ == '__main__':
    unittest.main()
