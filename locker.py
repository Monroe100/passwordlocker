# import os,csv,pyperclip
class userdata:
    '''
    Class that contains the users data such as username, password and the category of the account(gmail,facebook etc)
    '''
    data_list = [] #empty data list
    
    def __init__(self,username,password,category):
        self.username = username
        self.password = password
        self.category = category


