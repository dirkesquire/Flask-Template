from hashlib import md5

def hash_password(username, password):
    return md5(password.encode('utf-8')).hexdigest()
