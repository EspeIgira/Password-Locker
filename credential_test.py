import unittest
from credential import Credential

class TestCredential(unittest.TestCase):

    def setUp(self):

        self.new_credential = Credential("EspeIgira","******") # create Credential object
    
    def test_init(self):

        self.assertEqual(self.new_user.Username,"EspeIgira")
        self.assertEqual(self.new_user.password,"******")
    
    def test_save_credential(self):
        
        self.new_credential.save_credential() 
        self.assertEqual(len(Credential.credential_list),1)
