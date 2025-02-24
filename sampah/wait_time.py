import random
import time
import itertools

def gaussian_wait_time():
    return max(1, random.gauss(5, 2))

def exponential_wait_time():
    return max(1, random.expovariate(1/5))

wait_time = itertools.cycle([1, 2, 3, 4, 5, 6])
def cycle_wait_time():
    hour = time.localtime().tm_hour
    if 8 <= hour <= 18:
        return random.uniform(2, 5)
    else:
        return random.uniform(5, 10)

def adaptive_wait_time(self):
    """Mengatur wait time berdasarkan rata-rata waktu respons API"""
    if self.environment:
        last_response_time = self.environment.stats.total.avg_response_time
        return max(1, last_response_time / 1000)
    return 5
