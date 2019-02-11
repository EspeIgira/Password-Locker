import unittest
from credential import Credentials

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
        test_credential = Credentials("KizaDy","@@@@@@*") # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),2)

        

     

if __name__ == '__main__':
    unittest.main()
