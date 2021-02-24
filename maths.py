output = []
for i in range(0, 500):
    if i % 3 == 0 and i % 2 == 0:
        primes = []
        for num in range(4, i + 1):
            if num > 1:
                for j in range(2, num):
                    if (num % j) == 0:
                        break
                else:
                    primes.append(num)
        for k in primes:
            if i % k == 0:
                break
            else:
                output.append(i)
                break

#print(output)


def prime_checker(inputt):
    for i in range(2,inputt):
        if inputt % i == 0:
            return False
        elif i >= (inputt/2):
            return True

"""""
def recursion(n):
    i = n/2
    if i == 1:
        return True
    elif n %
"""""


def lastlist(x):
    if len(x) > 1:
        print("help")
        lastlist(x[1:None])
    else:
        print("fuck", x)
        return x


print(lastlist([1,2,3]))
#print(prime_checker(4))

d

