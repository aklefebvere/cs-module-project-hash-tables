# resizing an array is linear
# pre-allocating is one option
my_arr = [None] * 100000000

# Pre-populate your cache
import math

def inverse_root(num):
   return 1 / math.sqrt(num)



cache = {}

def populate_cache():
    for i in range(1, 10000):
        cache[i] = inverse_root(i)






# hash table:
## hash function
## backed by an array
## Some way to handle collisions: Linked list (or use open addressing)
