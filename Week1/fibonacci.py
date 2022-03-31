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