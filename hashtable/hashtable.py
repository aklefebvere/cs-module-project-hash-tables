class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, key):
        current = self.head

        # search for the key that was passed into the method
        while current is not None:
            if current.key == key:
                return current

            current = current.next

        # if the search found nothing, return current which at this
        # point will always be None
        return current

    def insert_tail(self, key, value):
        # if there is no head...
        if self.head == None:
            # create a new node
            new_node = HashTableEntry(key, value)
            # make the new node the head
            self.head = new_node
        # if the head exists...
        else:
            # search for the node that matches the key
            # that was passed in
            node = self.search(key)
            
            # if it found a match
            if node is not None:
                # replace the value of that node with the new value
                node.value = value
            # if the key does not exist in the linked list...
            else:
                # create a new node
                new_node = HashTableEntry(key, value)
                # set a current variable to iterate
                current = self.head
                # itereate through current to find the tail
                while current.next is not None:
                    current = current.next
                # set the tails next node 
                current.next = new_node


    def delete(self, key):
        # set the current to iterate
        current = self.head
        # if the next value after current is None,
        # then that means the only node is the head.
        # remove the head
        if current.next is None:
            self.head = None
        # if the current key is the key passed in,
        # set the new head as the current's next node
        elif current.key == key:
            self.head = current.next
        # if there is a next node and the key does not
        # match the head...
        else:
            # iterate through the linked list
            while current.next is not None:
                # if the next node's key is the passed in key
                if current.next.key == key:
                    # set the current next node to None
                    current.next = None
                # if the current next's key is not the key we are looking for,
                # keep iterating
                else:
                    current = current.next

    def size(self):
        current = self.head
        size = 0
        if current.next is None:
            return 1
        else:
            while current is not None:
                size += 1
                current = current.next

            return size

    


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        total_elements = 0
        for i in self.table:
            if i is None:
                pass
            else:
                total_elements += i.size()

        return total_elements / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        string_bytes = key.encode()
        hash = 5381
        for i in string_bytes:
            hash = ((hash * 33) ^ i) % 0x100000000

        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # get the hash index
        hash_index = self.hash_index(key)

        # if the hash index is None...
        if self.table[hash_index] is None:
            # create a linkedlist object
            self.table[hash_index] = LinkedList()
            # insert the node to the tail of the linked list
            # since it won't find a head, it will set this
            # as the head
            self.table[hash_index].insert_tail(key, value)
        # if a linked list already exists
        else:
            # add a node to the tail
            self.table[hash_index].insert_tail(key, value)

        load_factor = self.get_load_factor()

        if load_factor >= 0.7:
            self.resize(self.get_num_slots() * 2)

        elif load_factor <= 0.2:
            new_capacity = self.get_num_slots() // 2
            if new_capacity < 8:
                new_capacity = 8
            self.resize(new_capacity)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # get the hash index
        hash_index = self.hash_index(key)
        
        # if there is no linked list at the index
        if self.table[hash_index] == None:
            # return
            return print("The key had no value")
        # if there is a linked list at the index...
        else:
            # delete the node
            self.table[hash_index].delete(key)

            # if the head was deleted...
            if self.table[hash_index].head is None:
                # a linked list is not needed, set the index to None
                self.table[hash_index] = None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # get the hash index
        hash_index = self.hash_index(key)
        # if there is no linked list at a the index...
        if self.table[hash_index] is None:
            # return None
            return None

        # if there is a linked list at the index,
        # search for the key at that linked list
        node = self.table[hash_index].search(key)

        # if it found a match...
        if node is not None:
            # return the value
            return node.value

        # if it didn't find a match
        else:
            # return None since search() returns None if nothing is found
            return node


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        new_array = [None] * new_capacity

        self.capacity = new_capacity

        for i in self.table:
            if i is None:
                pass
            else:
                hash_index = self.hash_index(i.head.key)
                new_array[hash_index] = i

        self.table = new_array



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
