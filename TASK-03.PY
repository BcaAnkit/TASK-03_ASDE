def compute_value(n):
    if n < 10:
        return n ** 2
    elif n >= 10 and n <= 20:
        fact = 1
        for i in range(n - 10, 0, -1):
            fact *= i
        return fact
    else:
        return sum(range(1, n - 20 + 1))

# Testing the script
print(compute_value(4))   # Output: 16
print(compute_value(15))  # Output: 120
print(compute_value(25))  # Output: 15
