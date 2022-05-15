# Unit testing is a way to test individual units of code
# - Typically automated
# - Gain confidence that individual parts of our software is working
# - Key part of refactoring

import unittest

class TestStringOperations(unittest.TestCase):
    # write our tests...

    def test_length_name_is_6(self):
        name = "Wesley"
        self.assertEqual(len(name), 6)

    def test_x_npt_in_string(self):
        sent = "On Earth, gravity gives weight to physical objects, and"
        is_x_in_sent = "x" in sent
        self.assertFalse(is_x_in_sent)