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
        self.assertEqual(self.new_data.username,"monroe")
        self.assertEqual(self.new_data.password,"babygirl")
        self.assertEqual(self.new_data.category,"facebook")

if __name__ == '__main__':
    unittest.main()        

    def test_save_data(self):
        '''
        this is a test used to test if the data object has been saved in the data list
        '''
        self.new_data.save_data()    #saving the new data
        self.assertEqual(len(userdata.new_data),1)

if __name =='__main__':
    unittest.main