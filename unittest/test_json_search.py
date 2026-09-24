import unittest
from policy import *
from recursive_json_search import *
from test_data import *

class json_search_test(unittest.TestCase):
    '''test module to test search function in `recursive_json_search.py`'''
    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([]!=json_search(key1,data, role="admin"))
    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([]==json_search(key2,data, role="admin"))
    def test_is_a_list(self):
        '''Should return a list'''
        self.assertIsInstance(json_search(key1,data, role="admin"),list)
    def test_search_unauthorized(self):
        '''Security Test: Role guest should be blocked and return empty list'''
        self.assertEqual([], json_search("apiKey", data, role="guest"))
    
if __name__ == '__main__':
    unittest.main()
