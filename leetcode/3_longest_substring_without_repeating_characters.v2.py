import logging
import string


class Solution:
    def reset_alphabets(self, _str):
        # key-value 쌍 만들기
        alphabets = {}
        for c in _str:
            alphabets[c] = 0

        return alphabets

    def length_of_longest_substring(self, s: str) -> int:
        sol = Solution()
        char_dict = {}

        max_no = 0
        tmp = 0

        for c in s:
            value = char_dict.get(c)
            print(f'c: {c}, value: {value}')

            if value is None:
                char_dict[c] = 1
                tmp = tmp + 1
            else:
                print(f'tmp: {tmp}')
                print(f'max_no: {max_no}')
                max_no = max(tmp, max_no)
                char_dict = {}
                break

        print(f'max_no: {max_no}')
        print(char_dict)
        return 0


solution = Solution()
args = ["dvdf"]
# args = ['abcabcbb', 'a cab2c#bb', 'b bbb', 'pwwkew', " ", "c", "au", "dvdf"]

for s in args:
    answer = solution.length_of_longest_substring(s)
    print(f'answer: {answer}')