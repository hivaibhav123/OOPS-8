try:
    x = 5656265//0  
    print(x)
    
except ZeroDivisionError:
    print("Can't divide by zero")
  
finally:
    print("This is always executed")