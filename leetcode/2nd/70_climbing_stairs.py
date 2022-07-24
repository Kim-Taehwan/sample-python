class Solution:
    tmp_list = [0 for i in range(46)]

    def climb_stairs(self, n: int) -> int:
        if n == 0:
            return 1

        if n == 1:
            return 1

        sol = Solution()
        if sol.tmp_list[n] != 0:
            return sol.tmp_list[n]

        sol.tmp_list[n] = sol.climb_stairs(n - 1) + sol.climb_stairs(n - 2)
        return sol.tmp_list[n]


n_list = [2, 3, 4, 5, 38]
solution = Solution()

for _n in n_list:
    print(f'num: {solution.climb_stairs(_n)}')