'''Given a Binary Heap of size n in an array arr[]. Write a program to calculate the height of the Heap.'''
import math

class Solution:
    def heapHeight(self, arr, n):
        if n == 0:
            return -1
        return math.floor(math.log2(n))
