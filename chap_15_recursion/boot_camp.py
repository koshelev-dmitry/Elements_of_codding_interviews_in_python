'''
Pizdoliz

Shifted Array Search
A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset 
and you don’t have a pre-shifted copy of it. 
For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.

Given shiftArr and an integer num, implement a function shiftedArrSearch that finds 
and returns the index of num in shiftArr. If num isn’t in shiftArr, return -1. 
Assume that the offset doesn’t equal to 0 (i.e. assume the array is shifted at least once) 
or to arr.length - 1 (i.e. assume the shifted array isn’t fully reversed).

Explain your solution and analyze its time and space complexities.


Example:

input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
                                                 # outcome of shifting
                                                 # [2, 4, 5, 9, 12, 17]
                                                 # three times to the left
len(shiftArr)<2^31-1
shiftArr are integeres
num is integer 

# 1:
brute force comparison of each element of arr with num
time: O(n)
space: O(1)

# 2
If it sorted => bin search O(log n)

[9, 12, 17, 2, 4, 5]

num = 12
1) middle index = 3 (6//2) we have two parts: we compare the left with middle and middle with the right
2) 
O(log n) to find the start_index




output: 3 # since it’s the index of 2 in arr

'''
def bin_search(arr, target):
  l = 0
  r = len(arr)-1
  while l<=r:
    m = (l+r)//2
    if arr[m] == target:
      return m
    elif arr[m] > target:
      r = m - 1
    else:
      l = m + 1
  return -1 

# [17, 2]

def shifted_arr_search(shiftArr, num):
  # find the start_index
  l = 0
  r = len(shiftArr) - 1 # 5
  
  # [9, 12, 17, 2, 4, 5]
  #  l      m         r
  #         l   m     r
  #         l   r     

  while l != r-1:
    m = (r + l) // 2 
    if shiftArr[l] < shiftArr[m]: 
      l = m
    else:
      r = m
  
  rottated_index = r # 1
  
  if num >= shiftArr[0]:
    return bin_search(shiftArr[:rottated_index], num)
  else:
    return rottated_index + bin_search(shiftArr[rottated_index:], num)

shiftArr = [9, 12, 17, 2, 4, 5, 6, 7, 8]
for num in shiftArr:
    print(shifted_arr_search(shiftArr, num))
















