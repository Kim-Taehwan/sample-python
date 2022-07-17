import logging
import string


def reset_alphabets(s):
    # key-value 쌍 만들기
    alphabets = {}
    for c in s:
        alphabets[c] = 0

    return alphabets


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        alphabets = reset_alphabets(s)
        max_cnt = 0
        tmp = 0

        if len(s) == 0:
            return 0

        if len(s.strip()) == 0 or len(s) == 1:
            return 1

        for i in s:
            value = alphabets.get(i)
            if value == 0:
                alphabets[i] = 1
                tmp = tmp + 1
            else:
                max_cnt = max(tmp, max_cnt)
                tmp = 0
                alphabets = reset_alphabets(s)

                alphabets[i] = 1
                tmp = tmp + 1
                max_cnt = max_cnt - 1

        return max(tmp, max_cnt)


sol = Solution()
_s = ['abcabcbb', 'a cab2c#bb', 'b bbb', 'pwwkew', " ", "c", "au", "dvdf"]
for ss in _s:
    answer = sol.length_of_longest_substring(ss)
    print(f'test:{answer}')
