## todo I just want to implement a parser from ground up
"""
classical BNF for expression
expr->product ((+ | -) product)*
product->value ((* | /) value)*
value->num | '('expr')'

expr->product + expr
"""


## constructing AST

from lexer import  LexicalAnalyzer
def op_executable():
    pass

def number_executable():
    pass

def rule():
        return Parser()

class OrParser():
    def __init__(self, *parsers):
        self.parsers = parsers


    def parse(self, lex):
        pass

class StarParser():
    def __init__(self):
        pass

    def parse(self, lex):
        pass

class NumParser():
    pass

class Parser():
    def __init__(self, parser):
       self.parser = []

    def ast(self, parser):
        self.parser.append(parser)
        return self

    def sep(self, c):
        self.parser.append(c)
        return self

    def OR(self,*parsers ):
        self.parser.append(OrParser(parsers))
        return self
    def STAR(self, parser):
        self.parser.append(StarParser(parser))

        return self

    def number(self):
        pass

    def parse(self, lex):
        lexer_analyzer = LexicalAnalyzer()
        lexer_analyzer.run(input)

        while lexer_analyzer.hasNext():
            ## todo what to do right now
            token = lexer_analyzer.peak()

"""
classical BNF for expression
expr->product ((+ | -) product)*
product->value ((* | /) value)*
value->num | '('expr')'
"""

expr = None
value =  rule().OR(rule().number(), rule().sep('(').ast(expr).sep(')'))

product = rule().ast(value).ast(rule().STAR(rule().OR("*", "/").ast(value)))
orPlusMinusProductStar = rule().STAR(rule().OR("+", "-").ast(product))

expr = rule().ast(product).ast(orPlusMinusProductStar)

def run(input):
    lexer_analyzer = LexicalAnalyzer()
    lexer_analyzer.run(input)

    while lexer_analyzer.hasNext():
        ## todo what to do right now
        tree = expr.parse(lexer_analyzer)

    tree.run()
