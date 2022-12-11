class Node:
    def __init__(self, value,
                 prev_pointer=None, next_pointer=None):
        self.set_value(value)
        self.set_prev(prev_pointer)
        self.set_next(next_pointer)

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next_pointer

    def get_prev(self):
        return self._prev_pointer

    def set_value(self, value):
        self._value = value

    def set_prev(self, prev_pointer):
        self._prev_pointer = prev_pointer

    def set_next(self, next_pointer):
        self._next_pointer = next_pointer

    def __str__(self):
        return str(self.get_value())

class ListIterator:
    def __init__(self, list):
        self._cur = list._get_pointer(0)

    def __next__(self):
        el = self._cur
        if self._cur is None:
            raise StopIteration
        self._cur = self._cur.get_next()
        return el.get_value()


class List:
    def __init__(self, collection=None):
        self._start_pointer = None
        self._finish_pointer = None
        self._length = 0

        # If passed collection, add elements of collection to list
        if collection is not None:
            for i in collection:
                self.append(i)

    def __len__(self):
        return self._length

    def append(self, value):
        if self._length == 0:
            self._start_pointer = Node(value)
            self._finish_pointer = self._start_pointer
            self._length = 1
        else:
            self._finish_pointer.set_next(Node(value,
                                               self._finish_pointer))
            self._finish_pointer = self._finish_pointer.get_next()
            self._length += 1

    def __getitem__(self, i):
        curr_pointer = self._get_pointer(i)

        return curr_pointer.get_value()

    def __str__(self):
        arr = []
        for i in range(self._length):
            arr.append(str(self[i]))
        return "[" + ", ".join(arr) + "]"

    def pop(self, i):
        cur = self._get_pointer(i)

        if cur is None:
            return None

        prev = cur.get_prev()
        next = cur.get_next()

        if i in range(1, len(self) - 2):
            prev.set_next(next)
            next.set_prev(prev)
        else:
            if i == 0:
                self._start_pointer = next
                if next is not None:
                    next.set_prev(None)
            if i == len(self) - 1:
                self._finish_pointer = prev
                if prev is not None:
                    prev.set_next(None)

        self._length -= 1

        return cur.get_value()  # Return value of i-th element

    def _get_pointer(self, i):
        if i < 0 or i >= self._length:
            return None

        if i <= self._length / 2:
            curr_pointer = self._start_pointer
            for j in range(i):
                curr_pointer = curr_pointer.get_next()
        else:
            curr_pointer = self._finish_pointer
            for j in range(self._length - i - 1):
                curr_pointer = curr_pointer.get_prev()

        return curr_pointer

    def __add__(self, other):
        lst = List()

        cur = self._start_pointer

        while cur is not None:
            lst.append(cur)
            cur = cur.get_next()

        cur = other._start_pointer

        while cur is not None:
            lst.append(cur)
            cur = cur.get_next()

        return lst

    def __iter__(self):
        return ListIterator(self)
