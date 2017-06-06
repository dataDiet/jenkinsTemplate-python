class Solution(object):
	def ArrayPairSum(self, nums):
		nums=sorted(nums)
		ls=[]
		while nums:
			ls.append(min(nums.pop(),nums.pop()))
        	# your solution here
		return(sum(ls))
s=Solution()
s.ArrayPairSum([1,4,3,2])
