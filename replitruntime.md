{% include navigation.html %}

<div class="row justify-content-center" style="margin: 2%;">
    <iframe height="1000px" width="700px" src="https://replit.com/@SDSC2004/Pranav-Data-Structures-Repository-Tri-2?lite=true#menu.py"></iframe>
</div>

## Code Snippets

Menu
```python
# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders

import Week0.pattern
import Week0.matrices
import Week0.swap
import Week1.list
import Week1.fibonacci
import Week2.factorial
import Week2.gcd
import Week2.palindrome


# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    ["Fun", Week0.pattern.starpattern],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu


maths_sub_menu = [
    ["Fibonacci", Week1.fibonacci.print_tester],
    ["Factorial", Week2.factorial.tester],
    ["GCD", Week2.gcd.tester2],
    ["Palindrome", Week2.palindrome.tester],
    ["Swap", Week0.swap.swap],
    ["Matrices", Week0.matrices.matrice],
]

loops_sub_menu = [
    ["All Loops", Week1.list.tester],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


      
# def maths_submenuc
# using maths_sub_menu list:
# maths_submenuc works similarly to menuc
def maths_submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, maths_sub_menu)
    m.menu()


def loops_submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, loops_sub_menu)
    m.menu()
  
# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    print(title)
    menu_list = main_menu.copy()
    menu_list.append(["Math", maths_submenu])
    menu_list.append(["Loops", loops_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def maths_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, maths_sub_menu)
def loops_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, loops_sub_menu)  

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again

      
if __name__ == "__main__":
    menu()


```

Swap
```python
def swap(): #taking input, calling actual swap2 function
    x = int(input('Input a number: '))
    y = int(input('Input a number: '))
    x,y = swap2(x, y)
    print(x,y)
  
def swap2(x,y):
    if (x > y or y < x):
        temp = x #using temp variable to store one x
        x = y #changing x to y
        y = temp #changing y to x
        return x,y #return
    else:
      return x,y #no need for swap function if x and y are equal
      
```

Matrices
```python
def matrice():
    matrix = [[
        input("input a number "),
        input("input a number "),
        input("input a number ")
    ],
              [
                  input("input a number "),
                  input("input a number "),
                  input("input a number ")
              ],
              [
                  input("input a number "),
                  input("input a number "),
                  input("input a number ")
              ]]
    newMatrix = []
    matrice2(matrix, newMatrix)
    matrice3(newMatrix)


def matrice2(matrix, newMatrix):
    for w in range(len(matrix)):
        for y in range(len(matrix[w])):
            newMatrix.append(matrix[w][y])
    return (newMatrix)


def matrice3(newMatrix):
    print(newMatrix[0], newMatrix[1], newMatrix[2])
    print(newMatrix[3], newMatrix[4], newMatrix[5])
    print(newMatrix[6], newMatrix[7], newMatrix[8])

    # terminal print commands
```

List
```python
# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Pranav",  
               "LastName": "Sarathy",  
               "DOB": "August 2",  
               "City": "Milwaukee",  
               "Phone": "8581234566",  
               "Sports":["Soccer","Basketball","Football","Tennis",]  
              })  

InfoDb.append({  
               "FirstName": "Mihir",  
               "LastName": "Sampath",  
               "DOB": "March 2",  
               "City": "Milwaukee",  
               "Phone": "8583526768",  
               "Sports":["Swimming","Basketball","Soccer","Baseball",]  
              })  
InfoDb.append({  
               "FirstName": "Aryan",  
               "LastName": "Shah",  
               "DOB": "May 10",  
               "City": "Cincinnati",  
               "Phone": "8589877655",  
               "Sports":["Baseball", "Golf", "Fencing" ,"Cheerleading"]  
              })  
InfoDb.append({  
               "FirstName": "Jay",  
               "LastName": "Manjrekar",  
               "DOB": "August 27",  
               "City": "Boston",  
               "Phone": "8581455677",  
               "Sports":["Soccer","Tennis", "BodyBuilding"]  
              })  
# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars
```

Loops
```python
def print_data(i):
  print(InfoDb[i]["FirstName"], InfoDb[i]["LastName"]) 
  print("\t", "Sports: ", end="")
  print(", ".join(InfoDb[i]["Sports"]))
  
# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)


## hack 2b: def while_loop(0)
# while loop contains an initial n and an index incrementing statement (n += 1)

def while_loopt():
  while_loop(0)

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    #for n in range(len(InfoDb)):
    #    print_data(n)
    #j = int(n)
    #print(j)

    #while j < len(InfoDb):
    #    print_data(j)
    #    j += 1
    #return


## hack 2c : def recursive_loop(0)
# recursion simulates loop incrementing on each call (n + 1) until exit condition is met

def recursive_loopt():
  recursive_loop(0)

def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return  # exit condition


# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n - 1)
```

Fibonacci
```python
def print_recurfibonacci(i):
  if i <= 2:
    return 1
  else: 
    return print_recurfibonacci(i-2) + print_recurfibonacci(i-1)
print_recurfibonacci(0)

def print_tester():
  try:
    
    num = int(input("Enter a number for fibonacci: "))
    # check if the number is negative
    if num < 0:
        print("Sorry, fibonacci does not exist for negative numbers")
    else:
        print("The fibonacci of", num, "is", print_recurfibonacci(num))
  except ValueError:
    print("Sorry, fibonacci doesn't accept this user input")

# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input
if __name__=="__main__":
      print_tester()
```

Factorial
```python

class Factorial:
  def __init__(self):
    self.factSeq = [1]
  def __call__(self, n):
    if n < len(self.factSeq):
           return self.factSeq[n]
    else:
          fact_number = n * self(n-1)
          self.factSeq.append(fact_number)
    return self.factSeq[n]
  
fact_of = Factorial() # object instantiation and run __init__ method
# fact_of.print_factSeq()
# print(fact_of(3))# object running __call__ method
# fact_of.print_factSeq()

def tester():
  n = int(input())    
  print(fact_of(n))
```

GCD
```python
def igcd(a, b):
    if a > b:
        s = b
    if b > a:
        s = a
    for i in range(1, s + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd



class Gcd:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        if self.a > self.b:
            s = self.b

        if self.b > self.a:
            s = self.a

        for i in range(1, s+1):
            if self.a % i == 0 and self.b % i == 0:
                gcd = i
        return gcd

def tester():      
  print("This is OOP Form")      
  f = Gcd(36,24)
  print("The gcd of 36 and 24 is : ",end="")
  print(f())
  
  g = Gcd(24,18)
  print("The gcd of 24 and 18 is : ",end="")
  print(g())
  print()
  print("This is Imperative Form")
  print(igcd(36,24))
  print(igcd(24,18))

def tester2():
  b = int(input())
  p = int(input())
  y = Gcd(b,p)
  print(y())
```

Palindrome
```python
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

# Value1 = Palindrome(true)
# Value2 = Palindrome(trueline)
# Value3 = Palindrome(false)
# Value4 = Palindrome(falseline)


# print(f"{true} is {Value1._is_a_palindrome}")
# print(f"{false} is {Value3._is_a_palindrome}")
# print(f"{trueline} is {Value2._is_a_palindrome}")
# print(f"{falseline} is {Value4._is_a_palindrome}")

def tester():
  n = input()
  y = Palindrome(n)
  print(f"{n} is {y._is_a_palindrome}")
```
