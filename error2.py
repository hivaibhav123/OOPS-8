def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
  
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#output
#File "<string>", line 12
    #© 2022 GitHub, Inc.
    #^
#SyntaxError: invalid character in identifier
#> 
