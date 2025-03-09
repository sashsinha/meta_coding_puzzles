import unittest


def getWrongAnswers(N: int, C: str) -> str:
    """Returns a string of incorrect answers for the given correct answer C."""
    return ''.join('B' if ch == 'A' else 'A' for ch in C)


class TestGetWrongAnswers(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(getWrongAnswers(3, 'ABA'), 'BAB')

    def test_case_2(self):
        self.assertEqual(getWrongAnswers(5, 'BBBBB'), 'AAAAA')

    def test_case_3(self):
        self.assertEqual(getWrongAnswers(4, 'ABAB'), 'BABA')

    def test_case_4(self):
        self.assertEqual(getWrongAnswers(2, 'AA'), 'BB')

    def test_case_5(self):
        self.assertEqual(getWrongAnswers(6, 'BAABAB'), 'ABBABA')


if __name__ == '__main__':
    unittest.main()
