from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_map:
                return [num_map[comp], i]
            num_map[num] = i

        return []

if __name__ == '__main__':
    s = Solution()
    result = s.twoSum([2, 11, 15, 7], 9)
    print(result)