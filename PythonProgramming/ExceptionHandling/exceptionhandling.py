try:
    
    myvalue = int( input("enter the number of n"))
    result = 10/ myvalue
except ZeroDivisionError:
    print ("Not possibel to divide the number")
except Exception as e:
    print("Excpetion occured" +e)
  