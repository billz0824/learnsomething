#include <iostream>
#include <vector>

bool is_prime(int num, const std::vector<int>& primes) {
    for (int index = 0; index < primes.size(); ++index) {
        int i = primes[index];
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

void notDisasterCode() {
    std::vector<int> unique_primes;

    for (int i = 2; i < 2500; ++i) {
        int curr = i;
        if (is_prime(curr, unique_primes)) {
            unique_primes.push_back(curr);
        } else {
            for (int index = 0; index < unique_primes.size(); ++index) {
                int j = unique_primes[index];
                if (curr % j == 0) {
                    unique_primes.push_back(j);
                    while (curr % j == 0) {
                        curr /= j;
                    }
                }
                if (curr == 1) {
                    break;
                }
            }
        }
    }
}

int main() {
    double time = 0;
    for (int i = 0; i < 5; ++i) {
        auto start = std::chrono::high_resolution_clock::now();
        notDisasterCode();
        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> duration = end - start;
        time += std::chrono::duration<double>(duration).count();
    }
    time = time / 5;
    std::cout << "Average execution time after 5 runs: " << time << " seconds" << std::endl;

    return 0;
}
