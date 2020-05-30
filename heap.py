class Heap:

    def __init__(self, min_heap, key=None):
        self.heap_arr = []
        self.min = min_heap
        self.length = 0
        self.index_map = {}
        if key:
            self.get_value_impl = key

    def get_value_impl(self, val):
        return val

    def get_value(self, i):
        if i < 0 or i >= len(self.heap_arr):
            return self.get_end_val()
        if self.heap_arr[i] == self.get_end_val():
            return self.heap_arr[i]
        return self.get_value_impl(self.heap_arr[i])

    def comp(self, par, child):
        par_val = self.get_value(par)
        child_val = self.get_value(child)
        return self.comp_val(par_val, child_val)

    def swap(self, a, b):
        temp = self.heap_arr[a]
        self.heap_arr[a] = self.heap_arr[b]
        self.heap_arr[b] = temp

    @staticmethod
    def from_array(arr, min_heap,key=None):
        heap = Heap(min_heap,key)
        heap.min = min_heap
        for i in arr:
            heap.insert(i)
        return heap

    def insert(self, a):
        self.heap_arr.append(a)
        self.length += 1
        self.heapify_up(len(self.heap_arr) - 1)

    def heapify_up(self, node):
        if node <= 0:
            return
        if not self.comp((node - 1) // 2, node):
            self.swap((node - 1) // 2, node)
            self.heapify_up((node - 1) // 2)

    def get_end_val(self):
        if self.min:
            return float("infinity")
        return -float("infinity")

    def comp_val(self, right, left):
        if self.min:
            return right <= left
        else:
            return right >= left

    def heapify_down(self, node):
        if node > len(self.heap_arr) - 1:
            return
        self.heap_arr[node] = self.get_end_val()
        left = 2 * node + 1
        right = 2 * node + 2

        if self.comp(right, left):
            if right >= 0 and right < len(self.heap_arr):
                self.heap_arr[node] = self.heap_arr[right]
                self.heapify_down(right)
        else:
            if left >= 0 and left < len(self.heap_arr):
                self.heap_arr[node] = self.heap_arr[left]
                self.heapify_down(left)

    def pop(self):
        self.length -= 1
        temp = self.heap_arr[0]
        self.heapify_down(0)
        return temp

    def top(self):
        return self.heap_arr[0]


heap = Heap(min_heap=False, key=lambda y: y[1])
k = 0
for i in [1, 2, 1991, 12, 212, 121, 121, 212, 9]:
    k += 1
    heap.insert([i, k])

while heap.length:
    print(heap.pop())
