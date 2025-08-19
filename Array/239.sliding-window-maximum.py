class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_li = []
        max_li.append(max(nums[0:k]))

        for i in range(1,len(nums)-k+1,1):
            arr = nums[i:i+k]
            max_li.append(max(arr))
            """
            if nums[i] > max_li[-1]:
                max_li.append(nums[i])
            else:
                max_li.append(max_li[-1])
        """
        return max_li
    

sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
nums = [1,-1]
k = 1
print(sol.maxSlidingWindow(nums,k))   