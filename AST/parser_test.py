import unittest

from parser_expr import  ParserEngine
class MyTestCase(unittest.TestCase):
    def test_parser_without_parenthesis(self):
        engine = ParserEngine()
        s= "2"
        correct_ans =2
        ans = engine.run(s)
        self.assertEqual(correct_ans == ans, True)


        s= "2 + 10"
        correct_ans =2 + 10
        ans = engine.run(s)
        self.assertEqual(correct_ans == ans, True)

        s= "2 * 10"
        correct_ans =2 * 10
        ans = engine.run(s)
        self.assertEqual(correct_ans == ans, True)

        s= "2 + 10 * 5"
        correct_ans =2 + 10 * 5
        ans = engine.run(s)
        self.assertEqual(correct_ans == ans, True)

        s= "2*10 + 5"
        correct_ans =2*10 + 5
        ans = engine.run(s)
        self.assertEqual(correct_ans == ans, True)

        s = "2*10 + 5 + 3 + 12 + 231*12*31"
        correct_ans = 2*10 + 5 + 3 + 12 + 231*12*31
        ans = engine.run(s)
        self.assertEqual(correct_ans == ans, True)

    def test_with_parenthesis(self):
        engine = ParserEngine()

        s = "(3 + 5)"
        correct_ans = (3 + 5)
        ans = engine.run(s)
        print(ans)
        self.assertEqual(correct_ans == ans, True)

        s = "(3 * 5)"
        correct_ans = (3 * 5)
        ans = engine.run(s)
        print(ans)
        self.assertEqual(correct_ans == ans, True)

        s= "  ((3 * 5) + 2) * 10 + 2 + 100*(10*(10+31) + 10)"
        correct_ans =   ((3 * 5) + 2) * 10 + 2 + 100*(10*(10+31) + 10)
        ans = engine.run(s)
        print( ans )
        self.assertEqual(correct_ans == ans, True)



if __name__ == '__main__':
    unittest.main()
