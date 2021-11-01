#tests if 'testedNumber' is a prime number, returns a boolean
def isPrime(testedNumber):
    isTestedNumberPrime = False
    flag = False
    if testedNumber > 1:
        for den in range(2, testedNumber - 1):
            if (testedNumber % den) == 0:
                flag = True
                isTestedNumberPrime = False
    if flag == False:
        isTestedNumberPrime = True
    return(isTestedNumberPrime)

#runs 'isPrime()' function and adds to 'prime' array all prime numbers
def primeLoop(maxTestedNumber):
    primes = []
    for number in range(2, maxTestedNumber):
        if isPrime(number) == True:
            primes.append(number)
    return(primes)

#run primeLoop() to get all prime numbers from 2 to 'maxTestedNumber'