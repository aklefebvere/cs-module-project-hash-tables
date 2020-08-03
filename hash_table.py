# Build a data structure that will let us search for info really fast
## Given a list of a trillion elements, find a stirng O(1)
## Hack: turn a string into an index
## That way, we can jump there immediately

# we are building a dictionary {}, from scratch

## to Turn a string into an index, we built a hash function
### The hash function takes a string, turns it into a number, scrambles the number,
### and gives it back to us

## we Make sure the number we get back works with out list --> index
## Use our new index!

# Example
# Let's use key-value pair: "hello", "hello world"
## step 1: hash "hello"
## step 2: make hash work with list - aka turn into index
## step 3: put value at that index!

# Let's look it up!
## Step 1: hash "hello"
## step 2: make result work with list - turn into index
## step 3: go look at that index


my_list = ["hi", "how", "are", "you", "hello", "world"]

# time complexity of search?
# O(n)
#Why?
# Worst case scenerio is we would have to check every element
# my_list.contains() --> for loop (same thing)

# What if we had a function to tell us the index of "hello" in O(1)

# def my_func(string_to_search_for):
#     return index_of_string

# my_index = my_func("hello") # 4
# my_list[my_index] # return "hello"

# hashing function, hashes and returns a hash
## Deterministic

# Most take a string
# return an integer
# operate on the bytes of the string
# byte is basically an integer 0-255


def my_hash(s):
    string_bytes = s.encode()
    total = 0
    for b in string_bytes:
        total += b

    return total


print(my_hash("hello"))
print(my_hash("world"))

# what would happen if we got back the same number (index!) for different words?
## collision

# How to use the number we return (the "Hash") to get an index a list?
new_list = [None] * 8

hello_hash = my_hash("hello")

hello_index = hello_hash % len(new_list)

new_list[hello_index] = "hello world"

print(new_list[hello_index])

# put "howdy world" in at index "world"
## step 1: put "world" through our hashing function
## step 2: modulo that result with the length of our list
## step 3: use that modulo - index - with our list



hashed_world = my_hash("world")

world_index = hashed_world % len(new_list)

new_list[world_index] = "howdy world"

print(new_list)

# Search for "hello world" or #howdy world, given "world" or "hello"
## step 1: get the hash
## step 2: take the hash modulo length of our array
## step 3: use that index to access the value stored there
hashed_string = my_hash("hello")

our_index = hashed_string % len(new_list)

print(new_list[our_index])
