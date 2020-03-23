"""
classical BNF for expression
expr->product ((+ ) expr)
product->value ((* ) product)
value->num | '('expr')'

"""
# todo how to achieve minus left associativity ???
from lexer import NUMBER, PARENTHESIS, LexicalAnalyzer

class NumAST():
    def __init__(self, token):
        self.token = token

    def run(self):
        return self.token

class ExprAST():
    def __init__(self, operand1, op, operand2):
        self.operand1 = operand1
        self.op = op
        self.operand2 = operand2

    def run(self):
        if self.op == None:
            if self.operand1 == None:
                raise ValueError("operand1 is None")
            return self.operand1
        else:
            num1 = self.operand1.run()
            num2 = self.operand2.run()

            return simulate(num1, num2, self.op)

class ExprParser():
    def __init__(self, product):
        self.product = product

    def parse(self,lex):
        operand1 = self.product.parse(lex)
        token = lex.peak()

        if token == None or token.value == ")":
            return operand1

        op = lex.nextToken().value
        assert  op == "+"
        operand2 = self.parse(lex)
        return ExprAST(operand1, op, operand2)

class ProductParser():
    def __init__(self, value):
        self.value = value

    def parse(self, lex):
        operand1 = self.value.parse(lex)

        token = lex.peak()

        if token == None or token.value != "*":
           return operand1

        op = lex.nextToken().value
        assert op == "*"
        operand2 = self.parse(lex)
        return ExprAST(operand1, op, operand2)


class ValueParser():
    def __init__(self, expr):
        self.expr_parser =  expr

    def parse(self, lex):
        token = lex.peak()
        if token.type == NUMBER:
            token = lex.nextToken()
            print(token)
            return NumAST(token.value)

        elif token.type == PARENTHESIS:
            left = lex.nextToken()
            assert left.value == "("
            tree = self.expr_parser.parse(lex)
            right = lex.nextToken()
            assert right.value == ")"
            return tree

        else:
            raise ValueError("invalid input")


def simulate( operand1, operand2, op):

    if op == "+":
        return operand1 + operand2
    elif op == "-":
        return operand1 - operand2
    elif op == "*":
        return operand1 * operand2
    elif op == "/":
        return operand1 / operand2

    else:
        raise ValueError("invalude operator={0}", op)

class ParserEngine():
    def __init__(self):
        pass

    def run(self, input):
        lexx = LexicalAnalyzer()
        lexx.run(input)
        expr = None
        value = ValueParser(expr)
        product = ProductParser(value)
        expr = ExprParser(product)
        value.expr_parser = expr
        tree = expr.parse(lexx)

        ans = tree.run()

        return ans

