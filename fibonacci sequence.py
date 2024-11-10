#This program returns a sequence of fibonacci values.

def fibonacci(n=10):
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Real-time example
print("First 10 Fibonacci numbers:", fibonacci())


def fib(n=10):
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

#Output
print("The first 10 numbers in our fib sequence are:", fib())