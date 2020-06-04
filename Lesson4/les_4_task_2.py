import cProfile
import timeit

def sieve(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2

            while j < n:
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i > 0]
    return result


def prime(n):
    lst = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


def main(n):
    num = n ** 2
    a = sieve(num)
    b = prime(num)
    return a, b

#cProfile.run('main(100)')

main(10)

#         1    0.716    0.716    0.717    0.717 les_4_task_2.py:19(prime) 100
#         1    0.000    0.000    0.723    0.723 les_4_task_2.py:30(main) 100
#         1    0.005    0.005    0.006    0.006 les_4_task_2.py:4(sieve) 100
#      1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects} 100




# "les_4_task_2.prime(10)"
# 1000 loops, best of 5: 6.24 usec per loop

# "les_4_task_2.sieve(10)"
# 1000 loops, best of 5: 5.58 usec per loop

# "les_4_task_2.prime(100)"
# 1000 loops, best of 5: 122 usec per loop

# "import les_4_task_2" "les_4_task_2.sieve(100)"
# 1000 loops, best of 5: 40.3 usec per loop

# Вывод решето Эратосфена быстре