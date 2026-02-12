from doctest import debug_script


def debug(function):
    def wrapper(*args, **kwargs):
        print(function.__name__)
        print(f"{args}, {kwargs}")
        x = function(*args, **kwargs)
        print(x)
        return x
    return wrapper

@debug
def add(a, b, scale=1):
    return (a + b) * scale

print(add(2, 3, scale=10))