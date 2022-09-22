# Составить список простых множителей натурального числа N
n = int(input('Введите натуральное число N: '))

primes : list = []


while n != 1:
    if n % 2 == 0:
        primes.append(2)
        n //= 2
        pass
    added_prime = bool(0)
    for x in range(3,n + 1,2):
        if n % x == 0:
            primes.append(x)
            n //= x
            added_prime = bool(1)
            break
    if added_prime == 0:
        primes.append(n)
        n //= n

print(f'Простые множители числа: {primes}')