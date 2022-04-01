
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
  
def print_forloop():
    for i in range(len(InfoDb)):
        print_data(i)

      
# while loop contains an initial n and an index incrementing statement (n += 1)
def print_whileloop(i):
    while i < len(InfoDb):
        print_data(i)
        i += 1
    return

  
# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def print_recursiveloop(i):
    if i < len(InfoDb):
        print_data(i)
        print_recursiveloop(i + 1)
    return # exit condition


def tester():
  print_forloop(0)
  print_whileloop(0)
  print_recursiveloop(0)



