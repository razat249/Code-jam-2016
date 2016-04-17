import random

def str_generator(size, chars='01'):
    return '1' + ''.join(random.choice(chars) for _ in range(size -2)) + '1'

import math

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

# print list(divisorGenerator(111))[1]

import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return (False, 0)
    return (all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2)), 0)

def allUnique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)

def main():
    T = raw_input()
    input = raw_input()
    input = input.split()
    arr = [2,3,4,5,6,7,8,9,10]
    divisor_arr = []
    result_arr = []
    print 'Case #1: '
    while(True):
        string = str_generator(int(input[0]))
        flag = 1
        
        # for i in arr:
        #     num_arr.append(int(string,i))
        for i in arr:
            if is_prime(int(string,i))[0]:
                flag = 0
                break

        if flag:
            temp = []
            for i in arr:
                temp.append(list(divisorGenerator(int(string,i)))[1])
            print string + ' ' + ' '.join([str(x) for x in temp])

        if flag:
            result_arr.append(string)
        if len(result_arr) == int(input[1]) and allUnique(result_arr):
            return result_arr



print main()
