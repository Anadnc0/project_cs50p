import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        self.assertEqual(main.do_stuff(10), 15)

if __name__ == '__main__':
    unittest.main()