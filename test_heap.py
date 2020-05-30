from random import randint

from heap import Heap, OrderedHeap


def check_heap(arr, heap, reverse=False, key=None):
    if key is None:
        def fun(a): return a

        key = fun
    sorted_arr = []
    assert len(arr) == heap.length
    while heap.length:
        sorted_arr.append(heap.pop())
    sort_arr_expect = sorted(arr, reverse=reverse, key=key)
    assert sort_arr_expect == sorted_arr


def test_min_heap():
    arr = [randint(-100, 100) for i in range(3, -1, -1)]
    heap = Heap.from_array(arr)
    check_heap(arr, heap)


def test_max_heap():
    arr = [randint(-100, 100) for i in range(3, -1, -1)]
    heap = Heap.from_array(arr, min_heap=False)
    check_heap(arr, heap, True)


def test_score():
    count = {'A': 2, 'D': 6, 'C': 6, 'B': 6}
    min_heap = OrderedHeap.from_array(count.items(), key=lambda y: y[1])
    max_heap = OrderedHeap.from_array(count.items(), min_heap=False,
                                      key=lambda y: y[1])
    check_heap(count.items(), min_heap, reverse=False, key=lambda y: y[1])
    check_heap(count.items(), max_heap, reverse=True, key=lambda y: y[1])


def test_order():
    arr = "aaabbbcccdddd"
    count = {}
    for i in arr:
        if i not in count:
            count[i] = 0
        count[i] += 1
    min_heap = OrderedHeap.from_array(count.items(), key=lambda y: y[1])
    max_heap = OrderedHeap.from_array(count.items(), min_heap=False,
                                      key=lambda y: y[1])
    check_heap(count.items(), min_heap, reverse=False, key=lambda y: y[1])
    check_heap(count.items(), max_heap, reverse=True, key=lambda y: y[1])


def test_dynamic_heap():
    input = [["PUSH", 1], ["PUSH", 2], ["PUSH", 3], ["POP"], ["POP"],
             ["PUSH", 4], ["PUSH", 7], ["POP"], ["PUSH", -1],
             ["POP"]]
    heap = Heap()
    ans = []
    expected = [1, 2, 3, -1]
    for i in input:
        if i[0] == "PUSH":
            heap.insert(i[1])
        else:
            ans.append(heap.pop())

    assert expected == ans

    heap = Heap(min_heap=False)
    ans = []
    expected = [3, 2, 7, 4]
    for i in input:
        if i[0] == "PUSH":
            heap.insert(i[1])
        else:
            ans.append(heap.pop())
    assert expected == ans


def test_comparator():
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

    for i in range(len(heap_arr)):
        print(str(heap_arr[i]), str(sorted_arr[i]))

    assert heap_arr == sorted_arr
