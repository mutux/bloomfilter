# Bloomfilter algorithm implemented in Python

String algorithm for fun! Detailed information can be found on my blogger [MuTuX](http://www.mutux.com/2017/04/string-algorithm-bloom-filter.html "mutux's blog on text mining").

It also analyzed the configuration of parameters to guarantee a small enough false positive probability.

## Examples

```
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

```

## Finally
Have fun!
