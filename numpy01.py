import numpy as np   #impot numpy packae imp
import asyncio 
class Numpy :
    

    def __init__(self):
        self.size= int(input("Enter the size of array :"))  # we make it instance variable in contructor that ask to size of array
        print("Enter the choise pf input :",end= " ")
        print("1. 1d .",end="  "".2d .",end=" ")
        self.option = int(input("Enter the choise :"))


def get_input (self):
 if self.option == 1 :

    def get_in_1D(self):
        
        arr_1d = np.zeros(self.size,dtype=int)     # Create array of 5 size with All 0 element initial

        for i in range (self.size):
            arr_1d[i] = int(input(f"Enter the val of index {i}:"))   # Get the val from user in array

        return arr_1d;
 
 elif self.option == 2: 

    def get_in_2D(self):
       
       arr_2d = np.array([list(map(int, input().split())) for _ in range(self.size)])

       return arr_2d  
    
 else :
    print("option is not valid . ")
    
    
def print_123_D(self , arr_1d, arr_2d):
    
    ot = int(input("Enter the dimension to print "))
    if ot==1:
     print("Array is :"+ arr_1d)
    elif ot ==2:
       print("Array is 2d :"+arr_2d)

     

