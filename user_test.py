import unittest
from user import User

class TestUser(unittest.TestCase):

    #New User information

    def setUp(self):

        self.new_user = User("Facebook","EspeIgira","******","espeigira@ms.com") # create user object

  
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_account,"Facebook")
        self.assertEqual(self.new_user.Username,"EspeIgira")
        self.assertEqual(self.new_user.password,"******")
        self.assertEqual(self.new_user.email,"espeigira@ms.com")
    
    #Save the new User Account

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         user list.
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)

    #Delete user object

     def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = user("Instagram","WeraSu","@@@@@@","werasu@user.com") # new contact
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(User.user_list),1)





if __name__ == '__main__':
    unittest.main()
