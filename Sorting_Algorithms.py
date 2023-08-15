# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fmRv9dxhOGd2RQJoZT6S1LNNSEAlfeWL
"""

'''
Algorithm: Selection Sort
Time Complexity: O(n^2)
Space Complexity: O(1)
'''
def SelectionSort(arr):
  n = len(arr)
  for i in range(n):
    ind = i
    for j in range(i+1,n):
      if arr[j]<arr[ind]:
        ind = j
    arr[ind],arr[i] = arr[i],arr[ind]
  return arr
arr = [3,4,2,1,5]
print(SelectionSort(arr))

'''
Algorithm: Bubble Sort
Time Complexity: O(n^2)
Space Complexity: O(1)
'''
def BubbleSort(arr):
  n = len(arr)
  for i in range(n):

    for j in range(n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
  return arr
arr = [3,4,2,1,5]
print(BubbleSort(arr))

'''
Algorithm: Insertion Sort
Time Complexity: O(n^2)
Space Complexity: O(1)
'''
def InsertionSort(arr):
  n = len(arr)
  for i in range(1,n):
    key = arr[i]
    j = i-1
    while j>=0 and key<arr[j]:
      arr[j+1] = arr[j]
      j-=1
    arr[j+1] = key
  return arr
arr = [3,4,2,1,5]
print(InsertionSort(arr))

'''
Algorithm: Merge Sort
Time Complexity: O(nlogn)
Space Complexity: O(n)
'''
def merge(arr,low,mid,high):
  left = arr[low:mid]
  right = arr[mid:high]
  i = j = 0
  k = low
  while i<len(left) and j<len(right):
    if left[i]<right[j]:
      arr[k] = left[i]
      i+=1
    else:
      arr[k] = right[j]
      j+=1
    k+=1
  while i<len(left):
    arr[k] = left[i]
    i+=1
    k+=1
  while j<len(right):
    arr[k] = right[j]
    k+=1
    j+=1

def mergesort(arr,low,high):
  if low<high-1:
    mid = (low+high)//2
    mergesort(arr,low,mid)
    mergesort(arr,mid,high)
    merge(arr,low,mid,high)

arr = [3,4,2,1,5]
mergesort(arr,0,len(arr))
print(arr)

'''
Algorithm: Quick Sort
Time Complexity: Average: O(nlogn), Worst: O(n^2)
Space Complexity: O(n)
'''
def quicksort(arr):
  if len(arr)<=1:
    return arr
  return quicksort([i for i in arr if i<arr[0]])+[arr[0]]+([i for i in arr if i>arr[0]])

arr = [3,4,2,1,5]
print(quicksort(arr))