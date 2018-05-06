#!/usr/bin/env python3.6
import unittest
import pyperclip
import string
import random

from locker import userdata, Credentials


class TestUser(unittest.TestCase):
    """
    Test that defines test cases for the user class behaviour
    """
    def setUp(self):
        """
        set up method to run before each test cases
        """
        self.new_user = userdata("monroe", "babygirl", "monroe23@gmail.com")
    def test_init(self):
        """
        Test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.user_name,"monroe")
        self.assertEqual(self.new_user.password, "babygirl")
        self.assertEqual(self.new_user.email, "monroe23@gmail.com")

    def tearDown(self):
        """
        Method that cleans up after each case has run.
        """
        userdata.user_list = []

#     def test_user_save(self):
#         """
#         Test case to test if the user object is saved into the user_list.
#         """
#         self.new_user.user_save()

#         self.assertEqual(len(userdata.user_list),1)
#     def test_save_multiple_user(self):
#         """
#         Test to check whether we can save multiple user objects.
#         """
#         self.new_user.user_save()
#         test_user = User("kajuju","flower","kajuju@gmail.com")
#         test_user.user_save()
#         self.assertEqual(len(userdata.user_list),2)

#     def test_display_users(self):
#         self.assertEqual(userdata.display_users(),userdata.user_list)

# class TestCredentials(unittest.TestCase):
#     """
#     Test that define test cases for credentials.
#     """
#     def setUp(self):
#         """
#         set up method to run before each test cases
#         """
#         self.new_credential = Credentials("indimi","roses", "lovely")

#     def test_init(self):
#         """
#         Test case to test if the object is initialized properly.
#         """

#         self.assertEqual(self.new_credential.account_name,"indimi")
#         self.assertEqual(self.new_credential.account_username,"roses")
#         self.assertEqual(self.new_credential.account_password,"lovely")

#     def tearDown(self):
#         Credentials.credential_list = []

#     def test_save_account(self):
#         """
#         Test case to test if the credential object is saved in to credential_list.
#         """
#         self.new_credential.save_account()
#         self.assertEqual(len(Credentials.credential_list), 1)

#     def test_save_multiple_account(self):
#         """
#         Test case to test if we can save multiple credential objects.
#         """
#         self.new_credential.save_account()
#         test_account = Credentials("indimi","roses","kajuju")
#         test_account.save_account()
#         self.assertEqual(len(Credentials.credential_list),2)

#     def test_delete_account(self):
#         """
#         Test case to test if we can remove an account from credential list.
#         """
#         self.new_credential.save_account()
#         test_credential = Credentials("roses","indimi","kajuju")
#         test_credential.save_account()

#         self.new_credential.delete_account()

#         self.assertEqual(len(Credentials.credential_list),1)

#     def test_display_accounts(self):
#         """
#         Test case to test if lists of accounts are displayed.
#         """
#         self.assertEqual(Credentials.display_accounts(),Credentials.credential_list)

# if __name__ == '__main__':
#   unittest.main