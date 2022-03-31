# Extra Credit Hack 4 Palindrome

import re


class Palindrome:
    
    def __init__(self, candidate):
        
        self._candidate = candidate  
        self._length = len(candidate)  
        
        self._is_a_palindrome = False  
        self._az09 = re.sub(r'[^a-zA-Z0-9]', '', self._candidate) 
        self._analysis = []  
        self._tests = 0  
       
        self.is_palindrome()

    
    def is_palindrome(self):
        z = self._az09
        
        tests = int(len(z) / 2)
        for i in range(0, tests):
            front = z[i];
            back = z[len(z) - i - 1]
            if front.lower() == back.lower():
                self.logger(front, back, True)
                self._tests += 1
            else:
                self.logger(front, back, False)
                return
        self._is_a_palindrome = True
        return

  
    def logger(self, front, back, result):
        self._analysis.append({"test": self._tests, "front": front, "back": back, "result": result})

    @property
    def candidate(self):
        return self._candidate

    @property
    def tests(self):
        return self._tests

    @property
    def isPalindrome(self):
        return self._is_a_palindrome

    @property
    def analysis(self):
        return self._analysis
true = "racecar"
trueline = "A man, a plan, a canal -- Panama!"
false = "Monster"
falseline = "The Dog is a Cat"

Value1 = Palindrome(true)
Value2 = Palindrome(trueline)
Value3 = Palindrome(false)
Value4 = Palindrome(falseline)


print(f"{true} is {Value1._is_a_palindrome}")
print(f"{false} is {Value3._is_a_palindrome}")
print(f"{trueline} is {Value2._is_a_palindrome}")
print(f"{falseline} is {Value4._is_a_palindrome}")

      