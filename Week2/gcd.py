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