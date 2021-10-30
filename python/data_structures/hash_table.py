"""This module implements hash table with classes Node and HashTable"""


class HashTable:
    """The main class that implements hash table."""
    def __init__(self):
        self.capacity = 50
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        """The simple hash function"""
        hashsum = 0
        for indx, c in enumerate(key):
            hashsum += (indx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        """Method to insert new element to hash table"""
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def lookup(self, key):
        """The method to lookup the element of the hash function by key."""
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        return node.value

    def delete(self, key):
        """The method to delete node from hash table and all associations with it."""
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        self.size -= 1
        result = node.value
        if prev is None:
            node = None
        else:
            prev.next = prev.next.next
        return result


class Node:
    """The node class with key, value and next."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


if __name__ == "__main__":
    my_table = HashTable()
    my_table.insert("electronics", "midi")
    print(my_table.lookup("electronics"))
    my_table.insert("toys", "sloth")
    my_table.insert("study", "pen")
    my_table.insert("study", "books")
    print(my_table.lookup("study"))
    print(my_table.delete("electronics"))
