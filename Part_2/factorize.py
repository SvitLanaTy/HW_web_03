from multiprocessing import cpu_count, Pool
from time import time


def factorize(*number):
    result = []
    for num in number:
        f = [i for i in range(1, num + 1) if num % i == 0]
        result.append(f)
    return result


if __name__ == '__main__':
    start_time = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    stop_time = time()   
    print(f'Sinchro-time ==> {stop_time - start_time}')    
    print(f"Count CPU: {cpu_count()}")
    start_time = time()
    with Pool(cpu_count()) as p:
        p.map(
            factorize,
            [128, 255, 99999, 10651060]
        )
        
    stop_time = time()
    print(f'Multiprocessing time ==> {stop_time - start_time}')


# a, b, c, d  = factorize(128, 255, 99999, 10651060)

# assert a == [1, 2, 4, 8, 16, 32, 64, 128]
# assert b == [1, 3, 5, 15, 17, 51, 85, 255]
# assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
