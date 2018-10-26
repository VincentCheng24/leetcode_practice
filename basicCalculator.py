import sys


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        exp = []
        isnum = False

        # split the numbers and operators and add them into a list with original order
        for i in range(len(s)):
            if s[i].isdigit():
                if not isnum:
                    isnum = True
                    pos = i
            else:
                if isnum:
                    exp.append(s[pos:i])
                    isnum = False
                if s[i] != ' ':
                    exp.append(s[i])

        if isnum:
            exp.append(s[pos:])

        exp = exp[:-1]  # remove '\n'

        def calc_rec(l, r):
            jump = 0

            # calculate - / +
            for i in range(r, l-1, -1):
                if exp[i] == ')':
                    jump += 1
                elif exp[i] == '(':
                    jump -= 1
                elif jump == 0 and exp[i] == '-':
                    return calc_rec(l, i-1) - calc_rec(i+1, r)
                elif jump == 0 and exp[i] == '+':
                    return calc_rec(l, i-1) + calc_rec(i+1, r)

            # calculate // / *
            for j in range(r, l-1, -1):
                if exp[j] == ')':
                    jump += 1
                elif exp[j] == '(':
                    jump -= 1
                elif jump == 0 and exp[j] == '/':
                    return calc_rec(l, j-1) // calc_rec(j+1, r)
                elif jump == 0 and exp[j] == '*':
                    return calc_rec(l, j-1) * calc_rec(j+1, r)

            if exp[l] == '(' and exp[r] == ')':
                return calc_rec(l+1, r-1)
            else:
                return int(''.join(exp[l:r+1]))

        return calc_rec(0, len(exp)-1)


if __name__ == '__main__':
    while True:
        input_str = sys.stdin.readline()
        if len(input_str) == 0:
            break
        solver = Solution()
        out = solver.calculate(input_str)
        sys.stdout.write(str(out))
        print()
