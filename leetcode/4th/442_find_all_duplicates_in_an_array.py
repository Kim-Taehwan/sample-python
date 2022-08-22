from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        1. for 문을 돌면서, dict 에 넣는다.
        2. dict 에 value 를 넣으면서, key 값이 있으면 value + 1 을 한다.
        3. for 문 종료 후에 value 가 2인 값들을 뽑는다.
        """
        dict_no = {}
        for num in nums:
            if dict_no.get(num) is None:
                dict_no.update({num: 1})
            else:
                value = dict_no.get(num) + 1
                dict_no.update({num: value})

        result = [k for k, v in dict_no.items() if v == 2]
        print(result)
        result.sort()
        print(result)
        return result


solution = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
solution.findDuplicates(nums)
