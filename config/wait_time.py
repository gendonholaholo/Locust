import random
import time
import itertools

def gaussian_wait_time():
    """Distribusi normal dengan rata-rata 5 detik dan standar deviasi 2 detik"""
    return max(1, random.gauss(5, 2))

def exponential_wait_time(self=None):
    """Distribusi eksponensial dengan rata-rata 5 detik"""
    return max(1, random.expovariate(1/5))

cycle_times = itertools.cycle([1, 2, 3, 4, 5, 6])
def cycle_wait_time(self=None):
    """Pola wait time berdasarkan siklus tetap"""
    return next(cycle_times)
