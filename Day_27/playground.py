def add(*args):
    return sum([arg for arg in args])


print(add(1, 2, 3, 4, 5, 6))


def calculate(n, **kwargs):
    if "multiply" in kwargs:
        n *= kwargs["multiply"]
    if "divide" in kwargs:
        n /= kwargs["divide"]
    if "add" in kwargs:
        n += kwargs["add"]
    if "subtract" in kwargs:
        n -= kwargs["subtract"]
    return n


print(calculate(5, multiply=2, add=6))
