import unittest


from  lexer import LexicalAnalyzer
class MyTestCase(unittest.TestCase):
    def test_lexical(self):
        analyzer = LexicalAnalyzer()
        s = "(3 + 2 )  " \
            "*6- 5 "
        analyzer.run(s)

        print(analyzer.tokens)

        print(analyzer.peak().type)
if __name__ == '__main__':
    unittest.main()
