#In this we get input from usser and make arr and then perform operation
import numpy as np
class Operation :

    def Data(self):
        
     self.size = int(input("Enter the size of array :"))
     

     arr = np.zeros(self.size,dtype=int)
     for i in range(self.size):
        arr[i]= int(input(f"Enter val for element {i} :"))
    
     return arr
    
    def Math(self,arr):
       
     while True:
       print("1.min")
       print("2.max")
       print("3.std")
       print("4.var")
       print("5.exit")
       
       self.opt= int(input("Enter your Choise :"))
       if self.opt == 1:
         print("Minimum is :",np.min(arr))
       elif self.opt == 2:
         print("Maximum is :",np.max(arr))
       elif self.opt == 3:
         print("std is :",np.std(arr))
       elif self.opt == 4:
         print("Var is :",np.var(arr))
       elif self.opt == 5:
         print("thank you")
         break
       else:
         print("Enter wrong Indementation...")
        
c1= Operation()
arr=c1.Data()
c1.Math(arr)