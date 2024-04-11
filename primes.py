prime_numbers = [num for num in range (2, 1001) if all(num % i for i in range(2, num))]
print(prime_numbers)