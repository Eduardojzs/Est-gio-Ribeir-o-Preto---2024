def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def check_fibonacci(num, fib_sequence):
    if num in fib_sequence:
        return True
    else:
        return False

def main():
    num = int(input("Informe um número: "))
    sequence = fibonacci_sequence(num)
    print("Sequência de Fibonacci até {}: {}".format(num, sequence))
    
    if check_fibonacci(num, sequence):
        print("{} pertence à sequência de Fibonacci.".format(num))
    else:
        print("{} não pertence à sequência de Fibonacci.".format(num))

if __name__ == "__main__":
    main()