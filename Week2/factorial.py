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