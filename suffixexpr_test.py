import unittest
import re
from suffixexpression import SuffixExpression
class MyTestCase(unittest.TestCase):
    def test_suffix_expr(self):
        s ="1213+5)*6-(2 + 3)"

        reg = "^([\)|[0-9]+|\+|\-|\*|/|\(|\)])"
        pattern = re.compile(reg)
        g = pattern.match(s)

        print(g.group(1))

        self.assertEqual(g.group((1)) == "1213", True)

        s = ")"
        pattern = re.compile(reg)
        g = pattern.match(s)
        print(g.group(1))

    def test_parse(self):
        s ="(1213+5)*6-(2 + 3)"
        suffixcal = SuffixExpression()
        correc_ans = [1213, 5, '+', 6, '*', 2, 3, '+', '-']

        self.assertEqual(all([suffixcal[i] == correc_ans[i]  for i in range(len(correc_ans))]), True)


    def test_calculate(self):
        s = "(1213+5)*6-(2 + 3)"
        ans =(1213+5)*6-(2 + 3)
        suffixcal = SuffixExpression()

        self.assertEqual(ans == suffixcal.calculate(s) , True)

        s = "1- 3-10-3 +2"
        ans = 1 - 3 - 10 - 3 + 2

        self.assertEqual(ans == suffixcal.calculate(s), True)

        s = "4/ 1 * 2"
        ans = 4/1*2
        self.assertEqual(ans == suffixcal.calculate(s), True)

        s = "4/(1*2)"
        ans = 4 / (1 * 2)
        self.assertEqual(ans == suffixcal.calculate(s), True)

        s= "1 - 2 - 3 - 10 - 100"
        ans =1 - 2 - 3 - 10 - 100
        self.assertEqual(ans == suffixcal.calculate(s), True)
if __name__ == '__main__':
    unittest.main()
