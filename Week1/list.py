
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


# def print_data(n):
#     print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
#     print("\t", "Cars: ", end="")  # \t is a tab indent, end="" make sure no return occurs
#     print(", ".join(InfoDb[n]["Owns_Cars"]))  # join allows printing a string list with separator
#     print()
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


def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion


# for loop iterates on length of InfoDb



