from typing import List


class Solution:
    def count_bits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            result.append(bin(i).count('1'))

        return result


num_list = [2, 5]
solution = Solution()

for _n in num_list:
    print(f'num: {_n}')
    print(solution.count_bits(_n))


