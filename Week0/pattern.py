def starpattern():
  num_rows = int(input("Enter the number of rows"));
  for i in range(0, num_rows):
    for j in range(0, num_rows-i-1):
      print(end=" ")
    for j in  range(0, i+1):
        print("*", end=" ")
        print()

def pypart(n):
  k = 2*n - 2
  for i in range(0,n):
    for j in range(0,k):
      print(end="")
      k = k-2
      for j in range(0, i+1):
        print("*", end="")
      print("/r")


def contalpha(n):
  number = 65
  for i in range(0,n):
    for j in range(0,i+1):
      char = chr(number)
      print(char, end="")
      number = number + 1
    print("/r")

def tester():
  starpattern(5)

# main_menu = [
#   ["fancy staircase", "fancy.py"],
#   ["upside down staircase", "reversestaircase.py"],
# ]

# sub_menu = [
#   ["starpattern", "starpattern.py"],
# ]

# border = "=" * 25
# banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu():
#   title = "Pranav's Menu Python Challenge" + banner
#   menu_list = main_menu.copy()
#   main_list.append(["starpattern", submenu])

#   buildMenu(title, menu_list)
# def submenu():
#   title = "Pranav's Submenu Python Challenge" + banner
#   buildMenu(title, sub_menu)

# def buildMenu(banner, options):
#   print(banner)
#   prompts = {0: ["Exit", None]}
#   for op in options:
#     index = len(prompts)
#     prompts[index] = op
#   for key, value in prompts.items():PendingDeprecationWarningprint(key, '->', value[0])
#   choice = input("Type Your Choice> ")
# try: 
#   choice = int(choice)
#   if choice ==0:
#     return
#   try:
#     action = prompts.get(choice)[1]
#     action()
#   except TypeError:
#     try: 
#       exec(open(action).read())
#     except FileNotFoundError:
#       print(f"Not a number: {choice}")
#     except UnboundLocalError:
#       print(f"Invalid choice: {choice}")
#     buildMenu(banner,options)
  

