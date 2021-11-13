"""In this method classes for Linked List, Queue and Stack are implemented.
There are also supportive classes Node, Stripped Linked List, DoubleLinkedListForStack.
Node is a class that implements nodes of all the other classes.
StrippedLinkedList is a Linked List without some methods
that doesn't go to Queue.
Queue, Linked List and DoubleLinkedListForStack are inherited from it.
DoubleLinkedListForStack is a class that implements doubly linked list with just some
methods that are necessary for implementing Stack. """

class StrippedLinkedList:
    """This class implements core of linked list and is used to build other classes.
    it has __init__(), __repr__(), __iter__() and append() methods"""
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def append(self, node):
        """Method that appends node to the end of the linked object.
        return is used just as a breaking point here for a case when list is empty
        in other cases it goes through all of the nodes first and then links the passes node to
        the previous last one"""
        if self.head is None:
            self.head = node
            return
        last_node = None
        for current_node in self:
            last_node = current_node
        last_node.next = node


class LinkedList(StrippedLinkedList):
    """Implements fully functioning Linked List
    Methods: -inherited from StrippedLinkedList: __init__(), append(), __repr__(), __iter__()
             -it's own methods: prepend(), insert(), delete(), lookup()"""
    def prepend(self, node):
        """Links the passed node at the beginning of the linked list, makes this node a new head."""
        node.next = self.head
        self.head = node

    def insert(self, index, new_node):
        """Inserts the node at the specified index by going through all the linked nodes
        before it and moving them to the right.
        Raises an exception is the list is empty and if the node with passed index is not found."""
        if self.head is None:
            raise Exception("List is empty")
        prev_node = self.head
        i = 0
        for node in self:
            if i == index:
                prev_node.next = new_node
                new_node.next = node
                return
            i += 1
            prev_node = node
        raise Exception(f"Node with index {index} not found")

    def delete(self, index):
        """Deletes (unlinks) the node from the list.
        Raises an exception if list is empty and if the node with passed index is not found.
        Goes through all the nodes to the indexed one and links the previous and next nodes."""
        if self.head is None:
            raise Exception("List is empty")
        if index == 0:
            self.head = self.head.next
            return
        previous_node = self.head
        i = 0
        for node in self:
            if i == index:
                previous_node.next = node.next
                return
            i += 1
            previous_node = node
        raise Exception(f"Node with index {index} not found")

    def lookup(self, target_node_data):
        """Looks up the node by the passed data, returns the index of the target node.
        Raises an exception if list is empty and if the node with passed index is not found.
        """
        if self.head is None:
            raise Exception("List is empty")
        if self.head.data == target_node_data:
            return 0
        i = 0
        for node in self:
            if node.data == target_node_data:
                return i
            i += 1
        raise Exception(f"Node with data {target_node_data} not found")


class Node:
    """Class that implements a node which can be linked to next and previous nodes.
    Takes data of the node."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return self.data


class Queue(StrippedLinkedList):
    """Inherited from StrippedLinkedList implements queue with one-way linked list.
    Methods: -inherited from StrippedLinkedList: __init__(), append(), __repr__(), __iter__()
             -it's own methods: enqueue(), dequeue(), peek()"""

    def enqueue(self, node):
        """Puts the node as the last one to the queue"""
        super().append(node)

    def dequeue(self):
        """Takes the head node and returns it, removing it from the queue.
        Making the next node a new head.
        Raises an exception if queue is empty"""
        if self.head is None:
            raise Exception("Queue is empty")
        self.head = self.head.next
        previous_node = self.head
        self.head = self.head.next
        return previous_node

    def peek(self):
        """Returns the data of the head node"""
        return self.head.data


class DoubleLinkedListForStack(StrippedLinkedList):
    """The supportive class to implement Stack, is inherited from StrippedLinkedList.
  Methods: -inherited from StrippedLinkedList: __init__() partially, __iter__()
           -it's own methods: append(), __repr__()"""
    def __init__(self, nodes=None):
        super().__init__()
        self.tail = None
        if nodes is not None:
            node_tail = Node(data=nodes.pop)
            self.tail = node_tail
            for elem in reversed(nodes):
                node_tail.previous = Node(data=elem)
                node_tail = node_tail.previous

    def append(self, node):
        """Appends a node to the end, makes it a new tail
        and links it to the previous node both ways."""
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        node.previous = self.tail
        self.tail = node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " <=> ".join(nodes)


class Stack(DoubleLinkedListForStack):
    """Stack class inherited from DoubleLinkedListForStack.
     It's own methods: push(), pop(), peek()"""
    def __init__(self):
        super().__init__()

    def push(self, node):
        """Appends node to the end of stack."""
        super().append(node)

    def pop(self):
        """Removes from stack and returns the last element from stack.
        Raises an exception is Stack is empty."""
        if self.head is None:
            raise Exception("Stack is empty")
        last_node = self.tail
        self.tail = self.tail.previous
        return last_node

    def peek(self):
        """Returns the data of last node from stack"""
        return self.tail.data
