import dlt
from dlt.sources.helpers import requests

def main():
    print("Hello World");

def square_root_generator(limit):
    n = 1
    while n <= limit:
        print(n)
        yield n ** 0.5
        n += 1

# Example usage:


if __name__ == "__main__":
    limit = 13
    generator = square_root_generator(limit)

    res = 0
    for sqrt_value in generator:
        print(sqrt_value)
        # res = res + sqrt_value

    # print (res);
