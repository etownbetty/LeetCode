#Given an array, rotate the array to the right by k steps, where k is non-negative.

class Solution:
	def rotate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype:  void Do not return anything, modify nums in-place instead.
		"""
		if k > 0:
			nums[:] = nums[k:]+nums[:k]

	def rotate_rec(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype:
		"""
		#rotate k times
		for i in range(k):
			self.rotate_rec(nums[:i+1], k-1)

	def rotate2(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype:
		"""
		#rotate k times
		for i in range(k):
			last = nums[0]
			nums[:] = nums[1:]
			nums.append(last)
