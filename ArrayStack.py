import numpy as np
from Interfaces import Stack


class ArrayStack(Stack):
    """
        ArrayStack: Implements the Stack interface based on arrays.
        All the @abstractemthods should be implemented.
        An instance of ArrayStack has access to all the methods in ArrayStack and
        all the methods of the base class (Stack). When executing a method, it executes
        the method of ArrayStack, if it does not exists, it executes the method in the
        Base class (Stack).
        For exmaple,
        s = ArrayStack()
        print(s)
        print(len(s))
    """

    def __init__(self):
        self.n = 0
        self.a = np.zeros(1, dtype=object)  # this is numpy array

    def resize(self):
        """
        helper method; creates a new array that maintains the
        array size invariant and copies the old values making sure to keep LIFO order.
        """
        if self.n == len(self.a):
            new_length = max(2 * len(self.a), 1)
            new_a = np.zeros(new_length, dtype=object)

            for i in range(self.n):
                new_a[i] = self.a[i]

            self.a = new_a

        elif self.n <= len(self.a) // 3 and len(self.a) > 1:
            new_length = len(self.a) // 2
            new_a = np.zeros(new_length, dtype=object)

            for i in range(self.n):
                new_a[i] = self.a[i]

            self.a = new_a



    def get(self, i: int) -> object:
        """
        gets the element at index i of the LIFO stack
        :param i: int type; the index of the element to
        :return:
        """
        if i < 0 or i >= self.n:
            raise IndexError('out of bounds')
        return self.a[i]



    def set(self, i: int, x: object) -> object:
        """
        sets the value of index i to value x
        :param i: int type; the integer index that is non-negative but less than the number of elements
        :param x: object type; the new value to be placed at index i
        :return: object type; the old value that was replaced from index i
        """
        if i < 0 or i >= self.n:
            raise IndexError()
        y = self.a[i]
        self.a[i] = x
        return y



    def add(self, i: int, x: object):
        """
        inserts element x at index i by shifting all elements at indices j > i
        one position to the right
        :param i: int type; the integer index where the element will be inserted
        :param x: object type; the element to be inserted
        :raise IndexError: raises IndexError if i is negative or greater than or
        equal to the number of existing elements
        """
        if i < 0 or i > self.n:
            raise IndexError()
        if self.n == len(self.a):
            self.resize()
        for j in range(self.n, i, -1):
            self.a[j] = self.a[j - 1]

        self.a[i] = x
        self.n += 1






    def remove(self, i: int) -> object:
        """
        removes the element at index i by shift all elements at indices j > i
        one position to the left
        :param i: int type; the integer index of the element to be removed
        :raise IndexError: raises IndexError if i is negative or greater than or
        equal to the number of existing elements
        """
        if i < 0 or i >= self.n:
            raise IndexError()

        x = self.a[i]

        for j in range(i, self.n - 1):
            self.a[j] = self.a[j + 1]

        self.a[self.n - 1] = None

        self.n -= 1

        if self.n <= len(self.a) // 3 and len(self.a) > 1:
            self.resize()

        return x



    def push(self, x: object):
        """
        adds a given element to the stack in LIFO order
        :param x: object; the element to be added
        :return: None
        """
        self.add(self.n, x)

    def pop(self) -> object:
        """
        removes the head of the LIFO stack
        :return: object; the element at the head of the stack
        """
        if self.n == 0:
            raise IndexError("pop from empty stack")
        x = self.remove(self.n - 1)  # Remove the top element
        self.a[self.n] = None  # Explicitly set the last index to None after popping
        return x

    def size(self):
        """
            size: Returns the size of the stack
            Return: an integer greater or equal to zero representing the number
                    of elements in the stack
        """
        return self.n

    def __contains__(self, item):
        """
        returns True if the given item is stored in the stack; False otherwise
        allows for usage of 'in' operator with ArrayStack objects.
        :return: boolean
        """
        return item in self.a

    def __str__(self) -> str:
        """
        returns the content of the string using print(s)
        where s is an instance of the ArrayStack
        :return: str type; the content of the stack
        """
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        """
        makes this ArrayQueue an iterable object
        """
        self.iterator = 0
        return self

    def __next__(self):
        """
        returns the next item in the sequence when iterating over the
        ArrayStack
        """
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return x
