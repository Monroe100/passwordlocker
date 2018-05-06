import unittest #importing the unittest module
from locker import userdata #importing the userdata class
class Testuserdata(unittest.TestCase):
    '''
    This test class defines test cases for the behaviour of the userdata class
    '''
    def setUp(self):
        '''
        set up method to run before each test cases
        '''
        self.new_data = userdata("monroe","babygirl","facebook")
        #create data object

        def test_init(self):
            '''
            used to test if the object has been initialized properly
            '''
            