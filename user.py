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
    
    #Save user method
 
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    #Delete user method
    def delete_user(self):

        '''
        delete_user method deletes a saved user from user_list
        '''

        User.user_list.remove(self)
    
    
    # To let user information to pass
    @classmethod
    def find_by_email(cls,email):
     

     for user in cls.user_list:
        if user.email == email:
            return user 
