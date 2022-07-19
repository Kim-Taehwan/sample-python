import logging
import string

# Solution 1
"""
    1. 문자열을 배열로 만든다.
    2. start_index 는 0 부터 시작한다. 
    3. 반복문을 실행하면서, 하나의 문자를 dict 에 key 값으로 저장하고, value: 0 으로 한다.
    4. 다른 문자가 나오면, dict 에 key 값으로 저장하고, length_cnt 를 1 씩 증가시킨다.
    5. 같은 문자가 나오면, 
        a. start_index = start_index + length_cnt 로 변경한다.
        b. max_cnt = max(length_cnt, max_cnt) 로 계산한다.
        c. start_index 부터 반복문을 실행하면서,  
"""

# Solution 2
"""
    1. 문자열을 배열로 만든다.
    2. start_index 는 0 부터 시작한다.
    3. 반복문을 실행하면서, 하나의 문자를 dict 에 key 값으로 저장하고, value: 0 으로 한다.
    4. 다른 문자가 나오면, dict 에 key 값으로 저장하고, length_cnt 를 1씩 증가시킨다.
    5. 같은 문자가 나모면,
        a. start_index = start_index + 1 로 변경한다.
        b. max_cnt = max (max_cnt, length_cnt) 로 계산한다.
        c. dict 를 초기화 한다.
    6. 다시 반복문을 실행하면서, 3, 4, 5 를 실행한다.
    7. 문자열의 끝에 도달하면, max_cnt 를 리턴한다.
"""


class Solution2:

    def length_of_longest_substring(self, s: str) -> int:
        start_index = 0
        length_cnt = 0
        max_cnt = 0
        to_array = list(s)

        for ch in s:
            char_dict = {}

            for c in to_array[start_index:]:
                value = char_dict.get(c)
                if value is None:
                    char_dict[c] = 1
                    length_cnt = length_cnt + 1
                else:
                    break

            max_cnt = max(max_cnt, length_cnt)
            start_index = start_index + 1
            length_cnt = 0

        return max_cnt


solution = Solution2()
# args = ["dvdf", "abcabcbb"]
args = ['abcabcbb', 'a cab2c#bb', 'b bbb', 'pwwkew', " ", "c", "au", "dvdf"]

for s in args:
    answer = solution.length_of_longest_substring(s)
    print(f'answer: {answer}')
