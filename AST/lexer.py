import re

NUMBER = "NUMBER"
OP = "OP"
PARENTHESIS = "PARENTHESIS"

class Token():
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def value(self):
        return self.value
    def __repr__(self):
        return "type={0},value={1}".format(self.type, self.value)
    def __str__(self):
        return "type={0},value={1}".format(self.type, self.value)

class LexicalAnalyzer():
    def __init__(self):
        self.tokens = []
        self.reg = "([0-9]+|\+|\-|\*|/|\(|\)|\s)"
        self.pattern = re.compile(self.reg)
        self.op = set(['+', '-', '*', '/'])
        self.parenthesis = set(['(', ')'])

    def hasNext(self):
        return  len(self.tokens) > 0

    def nextToken(self):

        token = self.tokens[0]
        self.tokens.pop(0)

        return token

    def peak(self, index = 0):
        if index >= len(self.tokens):
            return None
        return  self.tokens[index]

    def add_token(self, s):
        if s.strip() == "":
            # just empty string do nothing
            return
        if s in self.op:
            self.tokens.append( Token(OP, s))
            return
        elif s in self.parenthesis:
            self.tokens.append(Token(PARENTHESIS, s))
            return
        else:
            # it has to be integer
            num = int(s)
            self.tokens.append(Token(NUMBER, num))
            return


    def run(self, input):
        begin = 0
        end = len(input)
        try:
            while begin < end:
                matched_obj = self.pattern.match(input, begin, end)
                matched_str = matched_obj.group(1)

                begin += len(matched_str)

                self.add_token(matched_str)
        except Exception as e:
            print(e)
            raise ValueError("invalid input={0}", input)
