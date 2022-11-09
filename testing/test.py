import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.dostuff(test_param)
        self.assertEqual(result, 15)


unittest.main()
