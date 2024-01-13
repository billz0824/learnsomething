import timeit

def disasterCode():
    uniquePrimes = []
    for i in range (2,2500):
        num = len(uniquePrimes)
        for j in uniquePrimes:
            if i % j != 0:
                num -= 1
        if num == 0:
            uniquePrimes.append(i)

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
