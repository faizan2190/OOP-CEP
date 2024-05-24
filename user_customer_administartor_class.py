import os
class User:

    def __init__(self, name, phone_no, email, username, password):
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.username = username
        self.password = password

    def save_to_file(self, folder_path):
        user_data = f"Name: {self.name}\nPhone Numer: {self.phone_no}\nEmail: {self.email}\nUsername: {self.username}\nPassword: {self.password}"

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        filename = os.path.join(folder_path, f"{self.username}.txt")

        with open(filename, "w") as file:
            file.write(user_data)

        print("Customer data have been successfully saved \U0001F600")

class Administrator(User):
    def __init__(self, name, phone_no, email, username, password):
        super().__init__(name, phone_no, email, username, password)

    def view_users(self):
        print("\nUsers:")
        for user in self.users:
            print(f"Username: {user.username}")

    def delete_user(self):
        print("\nDeleting User...")
        username = input("Enter username of user to delete: ")
        for user in self.users:
            if user.username == username:
                self.users.remove(user)
                print("User deleted successfully.")

    def search_user(self):
        print("\nSearching for User...")
        partial_name = input("Enter the partial name of the user to search: ").lower()
        found = False
        for user in self.users:
            if partial_name in user.name.lower():
                print(f"User found - Username: {user.username}, Name: {user.name}, Email: {user.email}")
                found = True
        if not found:
            print("No users found with the provided partial name.")

class Customer(User):
    def __init__(self, name, phone_no, email, username, password):
        super().__init__(name, phone_no, email, username, password)

    
