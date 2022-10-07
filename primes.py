"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def is_a_Prime(num):
    if (num==0) or (num==1):
        return False

    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

def primes(number_of_primes):
    if(number_of_primes <= 0):
        raise ValueError("The number of primes muss be bigger then 0")
        return

    list = []
    count = 0

    while(len(list) < number_of_primes):
        if is_a_Prime(count):
            list.append(count)

        count += 1
    return list
