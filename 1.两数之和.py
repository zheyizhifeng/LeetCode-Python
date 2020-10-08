#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in map:
                map[nums[i]] = i
            else:
                return [map[diff], i]
        return [-1, -1]
# @lc code=end
