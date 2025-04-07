from hashlib import sha256

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password):
    return stored_logins.get(email) == hash_password(password)

def main():
    stored_logins = {email: hash_password(pwd) for email, pwd in {
        "example@gmail.com": "password",
        "code_in_placer@cip.org": "Karel",
        "student@stanford.edu": "123!456?789"
    }.items()}
    
    test_cases = [
        ("example@gmail.com", "word"),
        ("example@gmail.com", "password"),
        ("code_in_placer@cip.org", "Karel"),
        ("code_in_placer@cip.org", "karel"),
        ("student@stanford.edu", "password"),
        ("student@stanford.edu", "123!456?789")
    ]
    
    print([login(email, stored_logins, pwd) for email, pwd in test_cases])
main()
