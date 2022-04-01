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
      