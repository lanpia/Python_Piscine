import pandas as pd

class User:
    def __init__(self):
        self.db = pd.DataFrame(columns=["user_id", "username", "password", "failed_attempts", "is_locked"])
        
    def register_user(self, user_id, username, password):
        self.db = pd.concat([self.db, pd.DataFrame({
            "user_id": [user_id], 
            "username": [username], 
            "password": [password], 
            "failed_attempts": [0], 
            "is_locked": [False]
        })], ignore_index=True)
    
    def reset_failed_attempts(self, id):
        self.db.loc[self.db["user_id"] == id, "failed_attempts"] = 0

    def increase_failed_attempts(self, id):
        self.db.loc[self.db["user_id"] == id, "failed_attempts"] += 1
        
    def lock_account(self, id):
        self.db.loc[self.db["user_id"] == id, "is_locked"] = True

    def login(self, username, password):
        user = self.db[self.db["username"] == username]
        return user


class AuthenticationSystem:
    def __init__(self):
        self.users = User()

    def register_user(self, user_id, username, password):
        self.users.register_user(user_id, username, password)
        print(f"User {username} registered successfully")
    
    # Never alter this login function
    def login(self, username, password):
        user = self.users.login(username, password)
        if user.empty:
            print(f"User {username} not found")
            return

        user = user.iloc[0]
        if user["is_locked"]:
            print(f"Account for {username} is locked. Please contact support.")
            return
        
        if user["password"] == password:
            self.users.reset_failed_attempts(user["user_id"])
            print(f"User {username} logged in successfully")
        else:
            self.users.increase_failed_attempts(user["user_id"])
            print(f"Failed attempts for {username}: {user['failed_attempts']}")
            if user["failed_attempts"] >= 3:
                self.users.lock_account(user["user_id"])
                print(f"Account for {username} has been locked due to too many failed login attempts.")
        print(f"User {username}'s data updated.")


auth_system = AuthenticationSystem()
auth_system.register_user(1, "neena", "password123") 
auth_system.register_user(2, "helios", "mysecurepassword") 

auth_system.login("neena", "password321")  
auth_system.login("Neena", "password123")  
auth_system.login("neena", "password123")  

auth_system.login("neena", "password321")  
auth_system.login("neena", "password321")  
auth_system.login("neena", "password321")  
auth_system.login("neena", "password321")  
auth_system.login("neena", "password123")  

auth_system.login("helios", "password321") 
auth_system.login("helios", "mysecurepassword") 

auth_system.login("helios", "MySecurePassword") 
auth_system.login("helios", "MYSECUREPASSWORD") 

# import pandas as pd

# class User:
#     def __init__(self, user_id, username, password, failed_attempts=0, is_locked=False):
#         self.user_id = user_id
#         self.username = username
#         self.password = password
#         self.failed_attempts = failed_attempts
#         self.is_locked = is_locked

#     def reset_failed_attempts(self):
#         self.failed_attempts = 0
#         print(f"Failed attempts reset for user {self.username}.")

#     def increment_failed_attempts(self):
#         self.failed_attempts += 1
#         print(f"Failed attempts for {self.username}: {self.failed_attempts}")
#         if self.failed_attempts >= 3:
#             self.lock_account()

#     def lock_account(self):
#         self.is_locked = True
#         print(f"Account for {self.username} has been locked due to too many failed login attempts.")

# class AuthenticationSystem:
#     def __init__(self):
#         self.users = pd.DataFrame(columns=["user_id", "username", "password", "failed_attempts_left", "is_locked"])

#     def register_user(self, user_id, username, password):
#         new_user = User(user_id, username, password)
#         self.users = pd.concat([self.users, pd.DataFrame({
#             "user_id": [user_id], 
#             "username": [username], 
#             "password": [password], 
#             "failed_attempts_left": [3], 
#             "is_locked": [False]
#         })], ignore_index=True)  # Add new user to DataFrame.
#         print(f"User {username} registered successfully.")

#     # Never alter this login function
#     def login(self, username, password):
#         user_row = self.users[self.users['username'].str.lower() == username.lower()]
#         if user_row.empty:
#             print(f"User {username} not found.")
#             return

#         user = User(user_row['user_id'].values[0], user_row['username'].values[0], user_row['password'].values[0], 
#                     user_row['failed_attempts_left'].values[0], user_row['is_locked'].values[0])
        
#         if user.is_locked:
#             print(f"Account for {username} is locked. Please contact support.")
#             return

#         if password == user.password:
#             user.reset_failed_attempts()
#             print(f"User {username} logged in successfully.")
#         else:
#             user.increment_failed_attempts()
        
#         self.update_user(user)

#     def update_user(self, user):
#         self.users.loc[self.users['username'] == user.username, 'failed_attempts_left'] = user.failed_attempts
#         self.users.loc[self.users['username'] == user.username, 'is_locked'] = user.is_locked
#         print(f"User {user.username}'s data updated.")

# auth_system = AuthenticationSystem()
# auth_system.register_user(1, "neena", "password123") 
# auth_system.register_user(2, "helios", "mysecurepassword") 

# auth_system.login("neena", "password321")  
# auth_system.login("Neena", "password123")  
# auth_system.login("neena", "password123")  

# auth_system.login("helios", "password321")
# auth_system.login("helios", "mysecurepassword")
