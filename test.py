import unittest
import rockPaperScissors as rps
from rockPaperScissors import Options,Result

class rockPaperScissorsTest(unittest.TestCase):
    def test_draw(self):
        result = rps.compare_choices(Options.ROCK, Options.ROCK)
        self.assertEqual(result, Result.DRAW)
        result = rps.compare_choices(Options.PAPER, Options.PAPER)
        self.assertEqual(result, Result.DRAW)
        result = rps.compare_choices(Options.SCISSORS, Options.SCISSORS)
        self.assertEqual(result, Result.DRAW)

    def test_win(self):
        result = rps.compare_choices(Options.ROCK, Options.SCISSORS)
        self.assertEqual(result, Result.WIN)
        result = rps.compare_choices(Options.SCISSORS, Options.PAPER)
        self.assertEqual(result, Result.WIN)
        result = rps.compare_choices(Options.PAPER, Options.ROCK)
        self.assertEqual(result, Result.WIN)

    def test_loss(self):
        result = rps.compare_choices(Options.ROCK, Options.PAPER)
        self.assertEqual(result, Result.LOSS)
        result = rps.compare_choices(Options.PAPER, Options.SCISSORS)
        self.assertEqual(result, Result.LOSS)
        result = rps.compare_choices(Options.SCISSORS, Options.ROCK)
        self.assertEqual(result, Result.LOSS)

if __name__ == '__main__':
    unittest.main()