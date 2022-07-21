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
    6. 다시 반복문을 실행하면서, 3, 4, 5 를 실행한다.
    7. 문자열의 끝에 도달하면, max_cnt 를 리턴한다.
"""

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
        char_list = list(s)
        print(f'char_list: {char_list}')
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