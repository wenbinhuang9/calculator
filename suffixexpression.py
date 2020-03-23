
import re
class SuffixExpression:
    def __init__(self):
        self.precedence = {
            "(":10,
            "*":9,
            "/":9,
            "+":8,
            "-":8,
            ")":7
        }

    def __check_valid(self):
        pass

    def __cmp_precedence(self, op1, op2):
        return self.precedence[op1] - self.precedence[op2]

    def __put_to_operator(self, suffix, operators, operator):
        if operator == "(":
            operators.append(operator)
        elif operator == ")":
            op_in_stack = operators.pop()
            while len(operators) > 0 and op_in_stack != "(":
                suffix.append(op_in_stack)
                op_in_stack = operators.pop()
        else:
            if len(operators) > 0 and operators[-1] == "(":
                operators.append(operator)
                return

            while len(operators) > 0 and self.__cmp_precedence(operator,operators[-1]) <= 0:
                op_in_top = operators.pop()
                suffix.append(op_in_top)

            operators.append(operator)


    def parse(self, expr):
        # (3+5)*6 - (2 + 3)
        reg = "([0-9]+|\+|\-|\*|/|\(|\)|\s)"
        pattern = re.compile(reg)
        begin, end = 0, len(expr)
        suffix = []
        operators = []
        try:
            while begin < end:
                match_ans = pattern.match(expr, begin, end)
                match_str = match_ans.group(1)

                begin += len(match_str)
                if match_str.strip() == "":
                    continue

                if match_str in self.precedence:
                    self.__put_to_operator(suffix, operators, match_str)
                else:
                    # it should be an integer here
                    number = int(match_str)
                    suffix.append(number)


            while len(operators) > 0:
                suffix.append(operators.pop())
            return suffix
        except Exception as e:
            print (e)
            raise ValueError("invalid expression {0}".format(expr))

    def __simulate(self, operand1, operand2, op):
        if op not in self.precedence:
            raise ValueError("invalid operator={0}", op)

        if op == "+":
            return  operand1  + operand2
        elif op == "-":
            return  operand1 - operand2
        elif op == "*":
            return  operand1 * operand2
        elif op == "/":
            return operand1/operand2

        else:
            raise ValueError("invalude operator={0}", op)



    def calculate(self, expr):
        suffix = self.parse(expr)

        stack = []
        ans = None
        try:
            for i in suffix:
                if i in self.precedence:
                    operand2 = stack.pop()
                    operand1 = stack.pop()

                    ans = self.__simulate(operand1, operand2, i)
                    stack.append(ans)
                else:
                    stack.append(i)

            return ans
        except Exception as e:
             print("invalid suffix {0}", suffix)
             raise e

