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

    

   