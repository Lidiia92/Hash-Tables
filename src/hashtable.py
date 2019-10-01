# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]

        if node is None:
            self.storage[index] = LinkedPair(key, value)
            return
        else: 
            pointer = node
            item_to_add = LinkedPair(key, value)

            #Finding the end of the list
            while pointer.next is not None:
                pointer = pointer.next

            pointer.next = item_to_add


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        pointer_to_be_deleted = None
        pointer_1 = None 
        pointer_2 = None

        # Case 1: Node is None
        if node is None:
            return "Was not found"

        # Case 2: Node has 1 item with matching key
        elif node.key == key and node.next == None:
            node.key = None

        # Case 3: Node has more than 1 item and matching key
        # is located at first item

        elif node.key == key:
            pointer_to_be_deleted = node
            node = node.next
            self.storage.remove(pointer_to_be_deleted)

        # Case 4: Node has more than 1 item and matching value is
        # is not a first item

        else:
            pointer_1 = node.next
            pointer_2 = node

            while pointer_1 != None and pointer_1.key != key:
                pointer_2 = pointer_1
                pointer_1 = pointer_1.next
            
            if pointer_1 in None:
                return 'Match not found'
            else:
                pointer_to_be_deleted = pointer_1
                pointer_1 = pointer_1.next
                pointer_2.next = pointer_1
                self.storage.remove(pointer_to_be_deleted)




    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        pointer = self.storage[index]
        found_match = False
        searched_value = None

        # Searching over the bucket for the value of the key
        # that we passed

        while pointer is not None:
            if pointer.key == key:
                found_match = True
                searched_value = pointer.value
            pointer = pointer.next

        if(found_match == True):
            return searched_value
        else:
            return None



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2

        new_storage = [None] * self.capacity

        for item in self.storage:
            if item is not None:
                new_index = self._hash_mod(item.key)
                new_storage[new_index] = item
        
        self.storage = new_storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
