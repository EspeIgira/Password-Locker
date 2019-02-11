import unittest
from credential import Credentials

class TestCredential(unittest.TestCase):


    def setUp(self):
       
        self.new_credential  = Credentials("EspeIgira","******") 


    def test_init(self):

        self.assertEqual(self.new_credential.Username,"EspeIgira")
        self.assertEqual(self.new_credential.password,"******")



    def test_save_credential(self):
        
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),1)

        

     

if __name__ == '__main__':
    unittest.main()
