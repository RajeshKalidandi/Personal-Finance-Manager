import hashlib
from database.db_manager import DatabaseManager

class AuthService:
    def __init__(self):
        self.db = DatabaseManager()
        self.current_user = None

    def register(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        hashed_password = self._hash_password(password)
        
        try:
            self.db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            self.db.commit()
            print("Registration successful!")
        except:
            print("Username already exists. Please try again.")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        hashed_password = self._hash_password(password)
        
        self.db.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
        user = self.db.fetchone()
        
        if user:
            self.current_user = user
            print("Login successful!")
        else:
            print("Invalid username or password.")

    def logout(self):
        self.current_user = None
        print("Logged out successfully.")

    def is_logged_in(self):
        return self.current_user is not None

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()