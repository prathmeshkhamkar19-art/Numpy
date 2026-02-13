# indexing - when we dill with for single element or row or column

#for 1 Dimension array - use [index]
#for 2 Dimension array  - use [row,column]

import numpy as np

class Index_sl:
   
 def index(self):
    self.in_arr = np.array([334,45,67,78,45,5,6,67])
    print("1 .find element of index")
    print("2.for print reve")
    print("3.find  subarray of given row and column")
    print("4.for Exit")
    self.inp= int(input("Enter the choise for opt -"))
    
    return self.in_arr, self.inp
  
 def sub(self,row1,col1,in_arr):
   arr = in_arr[row1:col1]

   return arr


 def condition(self,inp,in_arr):        #we pass the argument which same as return
   
   
    if inp == 1:
     index= int(input("Enter the index :"))
     print(f"Element of index {index} is :",in_arr[index])
     
    elif inp == 2:
     print("Reverse array is : ",in_arr[::-1])
    elif inp == 3:
       row = int((input("Enter the Row No.. ")))
       col = int(input("Enter the Column No.."))
       ans = self.sub(row1=row,col1=col,in_arr=in_arr)               #it is in freely in class so make it instance
                                                        #fun or class func means if we not call it through object
       print("Array is :",ans)
       

    elif inp == 4:
        print("Thank you ")
        2
    
    else :
        print("Wrong indentition ")

c1 = Index_sl()
new_arr,num = c1.index()     #if we return the 2 argument take in new var 
c1.condition(num,new_arr)   #pass the 


