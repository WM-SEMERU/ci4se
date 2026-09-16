def get_nth_prime_bruteforce(n, start_guess=2, start_num_primes=0):
    guess = start_guess
    num_primes_found = start_num_primes
    while True:
        if is_prime(guess):
            num_primes_found += 1
        if num_primes_found == n:
            nth_prime = guess
            break
        guess += 1
    return nth_prime