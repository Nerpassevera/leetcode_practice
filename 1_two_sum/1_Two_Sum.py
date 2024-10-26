# Time complexity O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = dict()

        for i in range(len(nums)):
            item = nums[i]
            second_addend = target - item

            if num_dict.get(second_addend) is not None:
                return [num_dict[second_addend], i]

            num_dict[item] = i



# Assertion to test the method
assert Solution().twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1], "1st Wrong!"
assert Solution().twoSum(nums=[3, 2, 4], target=6) == [1, 2], "2nd Wrong!"
assert Solution().twoSum(nums=[3, 3], target=6) == [0, 1], "3rd Wrong!"
