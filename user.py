class User:
    '''
    Class that generates new instances of users
    '''
    user_list = []

    def __init__(self,user_account,Username,password,email):
        
        # docstring to document

        self.user_account = user_account
        self.Username = Username
        self.password = password
        self.email = email