from typing import List


class Solution:
    def count_bits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            bin_count = self.calulate_bin_count(i)
            result.append(bin_count)

        return result

    def calulate_bin_count(self, num: int) -> int:
        if num == 0:
            return 0

        cnt = 0

        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                cnt = cnt + 1
                num = num // 2

        return cnt


num_list = [2, 5]
solution = Solution()

for _n in num_list:
    print(f'num: {_n}')
    print(solution.count_bits(_n))


