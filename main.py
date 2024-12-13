# main.py

def greet_user(name):
    """
    Function to greet a user by name.
    """
    if not isinstance(name, str):
        raise ValueError("Name must be a string")
    print(f"Hello, {name}!")

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greet_user(user_name)
