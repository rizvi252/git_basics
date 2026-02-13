# Simple calculator
# Simple calculator

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


if __name__ == "__main__":
    sum_result = add(2, 3)
    product_result = multiply(2, 3)

    print(f"2 + 3 = {sum_result}")
    print(f"2 * 3 = {product_result}")