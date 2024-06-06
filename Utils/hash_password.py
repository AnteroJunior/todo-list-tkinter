from passlib.hash import pbkdf2_sha256

class HashPassword:
    
    @staticmethod
    def hash_password(password):
        return pbkdf2_sha256.hash(password)
    
    @staticmethod
    def check_password(password_db, password):
        password_valid = pbkdf2_sha256.verify(password, password_db)
        return password_valid