

# Converts number into hash code
def hash_(num):
    hash_value = ((num ** 2) + 10) ** 2
    return int(hash_value)

hashmap = [[ ] for i in range(10)]


def store_hashmap(value, key):
    index = hash_(key) % 10
    hashmap[index].append(value)

store_hashmap("hello", 10)
store_hashmap("hi", 10)
print(hashmap)