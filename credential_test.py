import unittest
from credential import Credentials
import pyperclip

class TestCredential(unittest.TestCase):


    def setUp(self):
       
        self.new_credential  = Credentials("EspeIgira","******") 


    def test_init(self):

        self.assertEqual(self.new_credential.Username,"EspeIgira")
        self.assertEqual(self.new_credential.password,"******")

    
    def tearDown(self):
            
    
        Credentials.credential_list = [] 


    def test_save_multiple_credential(self):
            
            self.new_credential.save_credential()
            test_credential = Credentials("EspeIgira","******") # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credentials.credential_list),2)

          
    
    def test_delete_credential(self):
            
            self.new_credential.save_credential()
            test_credential = Credentials("KizaDy","@@@@@@*") # new credential
            test_credential.save_credential()
            self.new_credential.delete_credential()
            self.assertEqual(len(Credentials.credential_list),1)



    def test_credential_exists(self):
        

        self.new_credential.save_credential()
        test_credential = Credentials("KizaDy","@@@@@@*") # new credential
        test_credential.save_credential()

        credential_exists = Credentials.credential_exist("KizaDy")

        self.assertTrue(credential_exists)


    def test_display_all_credential(self):
        

        self.assertEqual(Credentials.display_credential(),Credentials.credential_list)

    #Pyperclip copy credentials to the clipboard.    

    def test_copy_Username (self):

        self.new_credential.save_credential()
        Credentials.copy_Username ("EspeIgira")

        self.assertEqual(self.new_credential.Username,pyperclip.paste())

    # def test_delete_credential(self):
        

    #     self.assertEqual(Credentials.delete_credential(),Credentials.credential_list)
     

if __name__ == '__main__':
    unittest.main()


