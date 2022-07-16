import logging


class Solution:

    def is_valid(self, s: str) -> bool:
        stack = []
        push_char_list = ['(', '{', '[']
        print('start')

        if len(s) == 0:
            return False

        for i in s:
            if i in push_char_list:
                stack.append(i)
                print(f'push: {stack}')
            else:
                if len(stack) == 0:
                    return False

                pop_char = stack.pop()
                if pop_char == '(' and i == ')':
                    continue
                if pop_char == '{' and i == '}':
                    continue
                if pop_char == '[' and i == ']':
                    continue
                return False
                print(f'pop: {pop_char}')

        if len(stack) == 0:
            return True
        else:
            return False


_s = "()("
sol = Solution()
is_answer = sol.is_valid(_s)
print(f'is_answer: {is_answer}')

