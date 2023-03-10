# -*- coding: utf-8 -*-
"""subarray_maxproduct.ipynb


Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
"""

# brute force
def maxProduct(nums):
  result=nums[0]
  for i in range(len(nums)):
    product=1
    for j in range(len(nums)):
      product=nums[j]*product
      result=max(result, product)
  return result

nums=[-2,3,-4]

# kadens

def maxProduct(self, nums: List[int]) -> int:
  max_pro=nums[0]
  min_pro=nums[0]
  result=max_pro
  for i in range(1,len(nums)):
    curr=nums[i]
    temp_max=max(curr,curr*max_pro,curr*min_pro)
    min_pro= min(curr,curr*max_pro,curr*min_pro)
    max_pro=temp_max
    result=max(max_pro,result)
  result

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pro=nums[0]
        min_pro=nums[0]
        result=max_pro
        for i in range(1,len(nums)):
            curr=nums[i]
            temp_max=max(curr,curr*max_pro,curr*min_pro)
            min_pro= min(curr,curr*max_pro,curr*min_pro)
            max_pro=temp_max
            result=max(max_pro,result)
        return result
