class MinHeap:
    def __init__(self):
        self.heap = [None]
        self.size = 0

    def __str__(self):
        if self.size == 0:
            return 'Empty Heap'
        string = ''
        for item in self.heap[1:]:
            string += (str(item) + ', ')
        return string

    def isempty(self):
        return self.size == 0

    def insert(self, item):
        self.size += 1
        self.heap.append(item)
        self.swim(self.size)

    def swim(self, k):
        while k > 1 and self.heap[k // 2] > self.heap[k]:
            self.swap(k // 2, k)
            k = k // 2

    def sink(self, k):
        while 2*k <= self.size:
            largest = k
            l = 2 * k
            r = 2 * k + 1
            if l <= self.size and self.heap[l] < self.heap[k]:
                largest = l
            if r <= self.size and self.heap[r] < self.heap[largest]:
                largest = r
            if largest == k:
                break
            self.swap(largest, k)
            k = largest

    def del_min(self):
        if self.size == 0:
            raise IndexError('Empty heap')
        min_val = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return min_val

    def swap(self, x, y):
        temp = self.heap[x]
        self.heap[x] = self.heap[y]
        self.heap[y] = temp


