import pyperclip
class Credentials:
    '''
    Class that generates new instances of Credential
    '''
    credential_list = []

    def __init__(self,Username,password):
        
        # docstring to document

        self.Username = Username
        self.password = password
    

    def save_credential(self):

        
        Credentials.credential_list.append(self)


    def delete_credential(self):


        Credentials.credential_list.remove(self)

    @classmethod
    def find_by_Username(cls,Username):
        

        for credential in cls.credential_list:
            if credential.Username == Username:
              return credential

    @classmethod
    def credential_exist(cls,Username):
        
        for credential in cls.credential_list:
            if credential.Username== Username:
                    return True

        return False

    @classmethod
    def display_credential(cls):
        
        return cls.credential_list


    @classmethod
    def copy_Username (cls,Username):
        credential_found = Credentials.find_by_Username(Username)
        pyperclip.copy(credential_found.Username )
    
   
    

   