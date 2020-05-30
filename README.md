# Heapy - Better Heaps in python
Custom heap Implementation in python. Easy to implement Heaps in python with custom keys and comparator.

In order to use it 

# Min Heap
By default the heap is treated as min heap.

```
from heap import Heap

my_min_heap = Heap()
my_min_heap.insert(20)
my_min_heap.insert(1)
my_min_heap.insert(9)

my_min_heap.pop()
```

# Max Heap
```
from heap import Heap

my_min_heap = Heap(min_heap=False)
my_min_heap.insert(20)
my_min_heap.insert(1)
my_min_heap.insert(9)

my_min_heap.pop()
```

# Custom Key Heap
This is when the heap element is not a primitive type for example a heap of pairs ['<character>', 'count'] heapified using the character count.
  
```
counts = {'A':1, 'B' : 2, 'C':3}
heap = Heap.from_array(counts)
while heap.length:
  heap.pop()
```

# Custom Comparator Heap
You can override the comp_val function like following to manage your custom comparator

```
class MyHeap(Heap):
    def comp_val(right, left):
        """
        Your changes goes here
        """

```






