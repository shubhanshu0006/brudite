#https://leetcode.com/problems/single-number-ii/description/
class Solution(object):
    def singleNumber(self, nums):
       unique_set = set(nums)
       summ = sum(unique_set)*3 - sum(nums)
       ns = summ//2
       return ns
