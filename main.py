# main.py

def greet_user(name):
    """
    Function to greet a user by name.
    """
    if not isinstance(name, str):
        raise ValueError("Name must be a string")
    if not name.strip():
        raise ValueError("Name cannot be empty")
    print(f"Hello, {name}!")


if __name__ == "__main__":
    try:
        user_name = input("Enter your name: ")
        greet_user(user_name)
    except ValueError as e:
        print(e)
