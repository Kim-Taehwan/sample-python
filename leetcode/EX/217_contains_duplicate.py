from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}

        for num in nums:
            if num_dict.get(num) is None:
                num_dict[num] = 1
            else:
                return True

        return False


solution = Solution()
num_list = [1, 2, 3, 1]
solution.containsDuplicate(num_list)
