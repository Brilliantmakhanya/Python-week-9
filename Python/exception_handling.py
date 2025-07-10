'''
try:
    print(x)
    
except NameError:
    print("variable x is not defined")
    
except:
    print("An exception occurred")
    

except:
    print("Something went wrong")


finally:
    print("The 'try except'is finished")
'''

#lesson2
try:
    print(x)
    
except NameError:
    print("variable x is not defined")

else:
    print("Everything went wrong")


x = -1
if x < 0:
    raise Exception("Sorry no number below zero")
