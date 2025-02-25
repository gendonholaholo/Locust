import random

class WaitTime:
    @staticmethod
    def gaussian_wait_time(self=None):
        """Distribusi normal dengan rata-rata 5 detik dan standar deviasi 2 detik"""
        return max(1, random.gauss(5, 2))

    @staticmethod
    def exponential_wait_time(self=None):
        """Distribusi eksponensial dengan rata-rata 5 detik"""
        return max(1, random.expovariate(1/5))
