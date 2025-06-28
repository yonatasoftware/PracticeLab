# hello.py

def greet(name):
    """Return a greeting for a given name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    user = input("Enter your name: ")
    age = input("Enter your age ")
    print(greet(user))
    print(age)
