import re
from Utils.hash_password import HashPassword

class Validators:
    @staticmethod
    def verify_email(email):
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            return True
        return False
    
    @staticmethod
    def verify_password(password):
        if(len(password) >= 6):
            return True
        return False
    
    @staticmethod
    def verify_name(name):
        if(len(name) >= 3 and re.search(r'^[a-zA-Z]+(?: [a-zA-Z]+)*$', name)):
            print(name)
            return True
        return False