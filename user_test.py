import unittest
from user import User

class TestContact(unittest.TestCase):

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
    
    #Save the new User
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         user list.
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)




if __name__ == '__main__':
    unittest.main()
