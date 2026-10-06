import time

def sum_of_n(n):
    total_sum = 0
    while n > 0:
        total_sum = total_sum + n
        n = n - 1
    return total_sum

dataset = []

for repetition in range(1, 11):
    timestamp_01 = time.time()
    n = repetition * 100
    result = sum_of_n(n)
    timestamp_02 = time.time()
    elapsed_time = round((timestamp_02 - timestamp_01) * 1e6, 2)
    dataset.append((n, elapsed_time, result))

for tup in dataset:
    print(tup)
