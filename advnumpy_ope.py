#In which we perform operation on array from getting user
#operation like  - insert , Append , Merge , Delete

# Note *  for insertion use same array in insert function and new array name also 
#           No need to call repeatdly function ... 
import numpy as np

class Opt:

    def __init__(self):
        self.size = int(input("Enter the size of array: "))
        self.arr = np.zeros(self.size, int)


        for i in range(self.size):                                          #Using loop insert Function
            val = int(input(f"Enter the val of index {i}: "))
            self.arr[i] = val     # Do not use append Function 
        print("\nAray after after add value using loop ")
        print("Final Array:", self.arr)
    
    def insert (self):
            

     while True :  
        self.opt = int(input("ENTER 1 TO REPEAT OR 2 TO EXIT : "))
        if self.opt == 1 :
        # insert valuse using insert function of numpy
           value=  int(input("Enter the val :"))
           ind = int(input("Enter the index where to add val :  "))
    
           self.arr =  np.insert(self.arr,ind,value)     #it copy all data from arr
                    
                                                        #after inserting value in array arr it make new array of sme name then call new arr
                                                        #dont use new array becuse it call repeat the old array and value only update one time in old array
        elif self.opt == 2 :
         break 
        
        else :
           print("Wrong Indentation .. ")
     print("\nArray after apply inser fuction ....")
     print("Final Array:", self.arr)
c1 = Opt()
c1.insert()
