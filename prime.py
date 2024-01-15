import timeit


def disasterCode():
    unique_primes = []
    for i in range (2,2500):
        curr = i
        if is_prime(curr, unique_primes):
            unique_primes.append(curr)
        else:
            for j in unique_primes:
                if curr % j == 0:
                    unique_primes.append(j)
                    while curr % j == 0:
                        curr /= j
                if curr == 1:
                    break


def is_prime(num, primes):
    for i in primes:
        if num % i == 0:
            return False
    return True

# Benchmark the code


if __name__ == "__main__":
    benchmark_code = "disasterCode()"
    setup_code = "from __main__ import disasterCode"

    # Measure the execution time of disasterCode function
    times = []
    for i in range(0,5):
        times.append(timeit.timeit(benchmark_code, setup=setup_code, number=1))

    res = sum(times)/5

    print(f"Average execution time after 5 runs: {res:.6f} seconds")
