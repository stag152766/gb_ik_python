import cProfile
import math


# pi_f = x / math.log(x)

def prime(num):
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 4,
               9592: 10 ** 5
               }

    for key in pi_func.keys():
        if num <= key:
            size = pi_func[key]
            break
    else:
        raise Exception('Слишком большой аргумент')

    array = [i for i in range(size)]
    array[1] = 0
    for m in range(2, size):
        if m != 0:
            j = m ** 2
            while j < size:
                array[j] = 0
                j += m
    res = [i for i in array if i != 0]
    return res[num - 1]


def test_prime(func):
    real_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

    for i, item in enumerate(real_prime, start=1):
        assert func(i) == item, f'Test {i} fail\t func({i}) =  {func(i)}'
        print(f'Test {i} OK')


test_prime(prime)
