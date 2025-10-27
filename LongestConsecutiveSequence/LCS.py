class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        nums.sort()

        consecCount = 1
        largestCount = 1

        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i] + 1:
                consecCount = consecCount + 1

                if largestCount < consecCount:
                    largestCount = largestCount + 1

            else:
                consecCount = 1

        return largestCount
