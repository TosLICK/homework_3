from time import time
from multiprocessing import Pool, cpu_count


def factorize(*numbers):
    dividers_list = []
    for num in numbers:
        dividers = []
        for i in range(1, num + 1):
            if not num % i:
                dividers.append(i)
        dividers_list.append(dividers)
    return dividers_list


def processing_factorize(n: int) -> list:
    dividers = []
    for i in range(1, n + 1):
        if not n % i:
            dividers.append(i)
    return dividers


def callback(result):
    print(f"Result in callback: {result}")


if __name__ == "__main__":
    start_time = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print(f"Sync execution time is {time() - start_time}")

    with Pool(cpu_count()) as p:
        numbers = 128, 255, 99999, 10651060
        start_time = time()
        p.map_async(processing_factorize, numbers, callback=callback)
        p.close()
        p.join()
        print(f"Execution time in processing is {time() - start_time}")




# assert a == [1, 2, 4, 8, 16, 32, 64, 128]
# assert b == [1, 3, 5, 15, 17, 51, 85, 255]
# assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
#              380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
