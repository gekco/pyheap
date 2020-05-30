# Heapy - Heaps in python
Easy to use, customisable ordered heaps in python.

# Installation
```
pip install heapy
```
## OR....
Just copy heap.py to your file or directory


# Usage and Methods


# Creation
You can create a heap from an array of nodes. A node here can be anything from what you want it to be. An integer, string, custom class, dictionary node

## Empty heap
You can create an empty heap by
```
heap = Heap(). # Min Heap
heap = Heap(min_heap=False) # Max Heap
```

## From Array
You can create the heap from an array in the following way:
```
arr = [9,0,-1,2,3,21]
min_heap = Heap.from_array(arr)
max_heap = Heap.from_array(arr, min_heap=False)
```

##  Insertion in heap 
You can push elements into the heap in the following manner.
```
arr = [9,0,-1,2,3,21]
heap = Heap.from_array(arr, min_heap=True)
heap.insert(12)
heap.insert(120)
```

# Pop
You can pop from heap 
```
arr = [9,0,-1,2,3,21]
heap = Heap.from_array(arr, min_heap=True)
heap.insert(12)
heap.insert(120)
heap.pop().  # will print -1
```

# Custom Score Heap
You can give a function in key which gives the score for that node, for example if you want your node to be a pair of (<char>, <count>) 
```
counts = {'A':1, 'B' : 2, 'C':3}
heap = Heap.from_array(counts.items(), key= lambda y : y[1])
while heap.length:
  heap.pop()
```

# Custom Comparator Heap
Like the sort function you can give comparator for the heap 
```
    class CustomHeapNode:
        def __init__(self, score1, score2, label):
            self.s1 = score1
            self.s2 = score2
            self.label = label

        def __str__(self):
            return self.label + str(self.s1) + str(self.s2)

    def lte(A, B):
        if A.s1 == B.s1:
            if A.s2 < B.s2:
                return 1
            elif A.s2 == B.s2:
                return 0
            else:
                return -1
        elif A.s1 < B.s1:
            return 1
        else:
            return -1

    arr = [CustomHeapNode(5, 2, "A"), CustomHeapNode(6, 1, "B"),
           CustomHeapNode(3, 10, "C"), CustomHeapNode(21, 0, "D"),
           CustomHeapNode(-1, 22, "E")]
    heap = OrderedHeap.from_array(arr, comp_nodes=lte)
    sorted_arr = sorted(arr, key=lambda y: y.s2)
    sorted_arr = sorted(sorted_arr, key=lambda y: y.s1)

    heap_arr = []
    while heap.length:
        heap_arr.append(heap.pop())

    assert heap_arr == sorted_arr

```






