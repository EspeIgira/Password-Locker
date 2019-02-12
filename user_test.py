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


    #Save the multiple Users
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_save_multiple_user(self):
            
            self.new_user.save_user()
            test_user = User("Instagram","WeraSu","@@@@@@","werasu@user.com")
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    #Delete user object

    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Instagram","WeraSu","@@@@@@","werasu@user.com") 
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(User.user_list),1)

    #Find user information
    def test_find_user_by_email(self):
      

        self.new_user.save_user()
        test_user = User("Instagram","WeraSu","@@@@@@","werasu@user.com") 
        test_user.save_user()

        found_user = User.find_by_email("werasu@user.com")

        self.assertEqual(found_user.Username,test_user.Username)


    #Existing user
    def test_user_exists(self):
        

        self.new_user.save_user()
        test_user = User("Instagram","WeraSu","@@@@@@","werasu@user.com") # new user
        test_user.save_user()
        user_exists = User.user_exist("werasu@user.com")
        self.assertTrue(user_exists)
   
    #Display user information

    def test_display_all_user(self):
        

        self.assertEqual(User.display_user(),User.user_list)




if __name__ == '__main__':
    unittest.main()

