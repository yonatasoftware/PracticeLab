# hello.py

def greet(name,age):
    """Return a greeting for a given name."""
    return f"Hello, {name}! your age is {age}"

if __name__ == "__main__":
    user = input("Enter your name: ")
    age = input("Enter your age ")
    print(greet(user,age))
    print(age)
