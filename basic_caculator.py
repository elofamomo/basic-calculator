class Solution:
    def do_operation(self, first, second, operator) -> int:
        if operator == '+':
            return first + second
        elif operator == '-':
            return first - second
        elif operator == '*':
            return first * second
        elif operator == '/':
            return int(first / second)
        elif operator == '^':
            return first ** second

    def get_precedence(self, operator):
        if operator == '^':
            return 3
        elif operator == '*' or operator == '/':
            return 2
        elif operator == '+' or operator == '-':
            return 1
        return 0

    def calculate(self, s: str) -> int:
        elements = []
        operators = []
        curr = 0
        while curr < len(s):
            if s[curr] == ' ':  # blank
                curr += 1
                continue
            elif s[curr].isdigit():
                element = 0
                # find the current element since digits can be consecutive
                while curr < len(s) and s[curr].isdigit():
                    element = element * 10 + int(s[curr])
                    curr += 1
                elements.append(element)
                curr -= 1
            elif s[curr] == '(':
                operators.append(s[curr])
            elif s[curr] == ')':
                while len(operators) != 0 and operators[-1] != '(':
                    second = elements.pop()
                    first = elements.pop()
                    operator = operators.pop()
                    elements.append(self.do_operation(first, second, operator))
                operators.pop()
            else:  # operator
                while len(operators) != 0 and self.get_precedence(operators[-1]) >= self.get_precedence(s[curr]):
                    second = elements.pop()
                    first = elements.pop()
                    operator = operators.pop()
                    elements.append(self.do_operation(first, second, operator))
                operators.append(s[curr])
            curr += 1
            # now the entire will all at the lowest precedence
        while len(operators) > 0:
            second = elements.pop()
            first = elements.pop()
            operator = operators.pop()
            elements.append(self.do_operation(first, second, operator))
        return elements[-1]


if __name__ == '__main__':
    solution = Solution()
    # print(solution.calculate("(0-3)/4"))
    print(int(-3 / 4))