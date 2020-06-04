import cProfile

def prime(num):
    count = 1
    current_prime = 2

    while count < num:
        current_prime += 1
        for i in range(2, int(current_prime ** 0.5 + 1)):
            if current_prime % i == 0:
                break
        else:
            count += 1
    return current_prime

def test_prime(func):
    real_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

    for i,item in enumerate(real_prime, start=1):
        assert func(i) == item, f'Test {i} fail\t func({i}) =  {func(i)}'
        print(f'Test {i} OK')


test_prime(prime)