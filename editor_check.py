numbers = [1, 2, 3]
print(numbers)


def greet(name: str) -> str:
    """Return a friendly greeting for the provided name."""
    return "Hello, " + name


print(greet("Alice"))
print(greet("Bob"))
print(greet("Charlie"))
