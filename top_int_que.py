class Solution:
    def reverseString_344_1(self, s):
        """
        T: O(n); S: O(n)
        """
        res = ''
        for i in range(len(s) - 1, -1, -1):
            res += s[i]
        return res

    def reverseString_344_2(self, s):
        """
        be careful that string is immutable
        T: O(n); S: O(n)
        """
        s = list(s)
        n = len(s)
        for i in range((n - 1)//2+1):
            s[i], s[n-i-1] = s[n-i-1], s[i]
        return ''.join(s)

    def reverseString_344_3(self, s):
        """
        be careful that string is immutable
        T: O(n * log(n)); S: O(log(n))
        """
        n = len(s)
        if n < 2:
            return s
        lstr = s[0:n//2]
        rstr = s[n//2:]
        return self.reverseString_344_3(rstr) + self.reverseString_344_3(lstr)

    def reverseString_344_4(self, s):
        """
        be careful that string is immutable
        T: O(n * log(n)); S: O(log(n))
        """
        return s[::-1]

    def fizzBuzz_412_1(self, n):
        """
        directly process every elements
        """
        res = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res

    def fizzBuzz_412_2(self, n):
        """
        process the idx first
        """

        no5 = {i for i in range(0, n+1, 5)} - {0}
        no3 = {i for i in range(0, n+1, 3)} - {0}

        FB = no3 & no5
        F = no3 - FB
        B = no5 - FB

        res = [str(i) for i in range(1, n+1)]

        for i in FB:
            res[i-1] = 'FizzBuzz'

        for i in F:
            res[i-1] = 'Fizz'

        for i in B:
            res[i-1] = 'Buzz'

        return res

    def fizzBuzz_412_3(self, n):
        """
        trick
        """
        res =['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n + 1)]
        return res

    def fizzBuzz_412_4(self, n):
        """
        ternary
        """
        return [str(i) if i % 3 != 0 and i % 5 != 0 else 'Fizz' * (not i % 3) + 'Buzz' * (not i % 5) for i in range(1, n+1)]





solver = Solution()
s1 = "A man, a plan, a canal: Panama"
s2 = "hello"

# print('reverseString_344_1: ', solver.reverseString_344_1(s1))
# print('reverseString_344_2: ', solver.reverseString_344_2(s1))
# print('reverseString_344_3: ', solver.reverseString_344_3(s1))
# print('reverseString_344_4: ', solver.reverseString_344_4(s1))

print('fizzBuzz_412_1: ', solver.fizzBuzz_412_1(15))
print('fizzBuzz_412_2: ', solver.fizzBuzz_412_2(15))
print('fizzBuzz_412_3: ', solver.fizzBuzz_412_3(15))
print('fizzBuzz_412_4: ', solver.fizzBuzz_412_4(15))
