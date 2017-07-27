from bitarray import bitarray
import mmh3


class BloomFilter:
    def __init__(self, size, hash_funcs_count):
        self.m = size
        self.k = hash_funcs_count
        self.store = bitarray(size)
        self.store.setall(0)

    def insert(self, text):
        for seed in range(self.k):
            result = mmh3.hash(text, seed) % self.m
            self.store[result] = 1

    def query(self, text):
        for seed in range(self.k):
            result = mmh3.hash(text, seed) % self.m
            if self.store[result] == 0:
                return "Definitely Not!"
        return "Maybe!"

"""
    Suppose we are going to store n=100000 elements in BloomFilter
    Hoping False Positive Probability be p<10^-5
    Then $m=-\\frac{n \\ln p}{(\\ln 2)^2}= -2.0814 n \\ln p = 2875560 bits = 351 KB$
    function number $k = -1.4427 \\ln p = 20 $
"""

bf = BloomFilter(2876000, 20)
bf.insert("test")
bf.insert("insert")
bf.insert("is")
bf.insert("there")
bf.insert("any")
bf.insert("false")
bf.insert("positive")
bf.insert("in")
bf.insert("this")
bf.insert("Bloom")
bf.insert("filter")
bf.insert("Notes")

print("bloom: " + bf.query("bloom"))
print("Filter: " + bf.query("Filter"))
print("Mutu: " + bf.query("Mutu"))
print("X: " + bf.query("X"))
print("1: " + bf.query("1"))
print("Bloom: " + bf.query("Bloom"))
print("filter: " + bf.query("filter"))
print("Notes: " + bf.query("Notes"))
