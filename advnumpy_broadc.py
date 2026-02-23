# In which we Perform Arithmatic Operation on Dimension Array
#Arithmatic Opertion Like :
#   1.adding
#   2. Multiply
#   3.addition of Array

import numpy as np

class Broadcast :
     def __init__(self):
        self.array_1d = np.array([1,36,7])
        self.array_2d = np.array([[3,5,7],[4,6,8]])

     def operation (self, array):
        if self.opt == 1:
           val=int(input("Enter the val :"))

           print("After add :",array+val)   # direct add but array need to be np.array
        elif self.opt == 2:
           val=int(input("Enter the val :"))
           print("After Mul :",array*val)     # direct Mul but array need to be np.array
        elif self.opt == 3:
          
           print(" Which  to Be add 1d or 2d :")
           select_Arr= int(input("Enter opt :\n 1 For 1d ..\n 2 for 2d .."))
           if select_Arr == 1:
             col =array.shape[0]    #Show limit of val to enter of 1d array size(col)
             inp_arr = list(map(int,input(f"Enter the val but limit is {col} :").strip()))  # or use split()

#                  map() → Applies a function (like int) to every element in an iterable (like a list).
#                          -An iterable is any object that you can loop over one element at a time.
#                  split() → Breaks a string into a list using a separator (default is space).

#                 strip() → Removes extra spaces (or characters) from the beginning and end of a string.

#                list() → Converts an iterable (like map object) into a proper list.

#                  int (inside map) → Converts a string number (like "10") into an integer (10).


             print("Array after add : ", array+inp_arr)
           
           elif select_Arr ==2 :
              col =array.shape[1]  # count col 
              rows = int(input("Enter rows of new 2D array: "))
              cols = int(input("Enter columns of new 2D array: "))

              data = []
              for i in range(rows):
               row = list(map(int, input(f"Enter {cols} values for row {i+1}: ").split()))
               if len(row) != cols:
                  print("Column size mismatch!")
                  exit()
               data .append(row)

              new_2d = np.array(data)
           print("Addition of 2d matrix :",array+new_2d)

        else :
           print("Wrong indentation ...") 
   
     def Ask(self):
        print("\n Choise :")
        print("\n 1 for add ..")
        print("\n 2 for Mul..")
        print("\n 3 for add of 1d and 2d array ..")
        self.opt= int(input("\nEnter the choise :"))
        self.opt_2 =int(input("\n1D OR 2D respectively (1 or 2 ):"))
        
        if self.opt_2 == 1 :
          self.operation(self.array_1d)
        elif self.opt_2 ==2 :
          self.operation(self.array_2d)
        else :
           print("invalid opt")

c1 = Broadcast()
c1.Ask()
