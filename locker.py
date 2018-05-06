#usr/bin/env python3.6 app.py
import pyperclip
import random
import string

global user_list
class userdata:
  """
  Class that generates new instances of  a user
  """

  user_list = [] #empty user list
  def __init__(self, user_name, password,email):
    self.user_name = user_name
    self.password = password
    self.email = email

#   def user_save(self):
#     """
#     saves user object into user object.
#     """
#     userdata.user_list.append(self)
#   @classmethod
#   def display_users(cls):
#     return cls.user_list


# class Credentials:
#   """
#   Class that generates new instances of  a credential object.
#   """
#   global user_list
#   credential_list =[]
#   def __init__(self, account_name, account_username, account_password):
#     self. account_name = account_name
#     self.account_username = account_username
#     self.account_password = account_password
#   @classmethod
#   def check_user_exist(cls,user_name,password):
#     """
#     Method that checks if a user exist from user list.
#     """
#     for user in userdata.user_list:
#       if user.user_name == user_name and user.password == password:
#         return True
#       return False

#   def save_account(self):
#     """
#     save_account saves credentials into credential object.
#     """
#     Credentials.credential_list.append(self)

#   def delete_account(self):
#     """
#     delete_account method removes a saved cretential from credential list.
#     """
#     Credentials.credential_list.remove(self)

#   @classmethod
#   def display_accounts(cls):
#     """
#     Method that returns the credential list.
#     """
#     return cls.credential_list
  