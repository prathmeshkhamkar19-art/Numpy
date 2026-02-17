# in this with help of Reshaping func   ( reshap(0,0))  we channge the dimension of Array/ Vector
import numpy as np

class Res_Ma:

    def __init__(self):  #Constructor after creating object in run and initialize variable First
        arr_1 = np.array([1,2,3,4,5,6])  #convert list into array
        reshaped_arr = arr_1.reshape(2,3)
        print(reshaped_arr)
    
#  ✔ Total elements must remain same
# ✔ rows × columns = total elements
# ✔ Can use -1 for automatic calculation
# ✔ Only structure changes, data remains same


      # Toc convert the multi dimension array in 1d 

    def _con_1d (self):
        self.arr_2d = np.array([[112,4,6], [4,7,4]])  #Combination of 1d array

        self.arr_3d = np.array([ [[1,2,3], [4,5,6]], [[7,8,9],[10,11,12]]  #Combination of 2d array
])
        print("Select the option for convert 2d or 3rd ...")
        print("1 for 2d Conversion..")
        print("2. for 3d Conversion..")
        print("3 for exit..")
        self.opt = int(input("Enter  :"))
        

        if self.opt == 1 :
        
         print("2D Array : ",self.arr_2d)
         print("\nAfter 1D (*Return Copy Form **):")
         print(self.arr_2d.flatten())
         print("\nAfter 1D (*Return View Form **):")
         print(self.arr_2d.ravel())
         
        elif self.opt == 2:
         print("2D Array : ",self.arr_3d)
         print("\nAfter 1D (*Return Copy Form **):")
         print(self.arr_3d.flatten())
         print("\nAfter 1D (*Return View Form **):")
         print(self.arr_3d.ravel())

        elif self.opt == 3 :
           print("Thank you ...")

        else : 
           print("Invlid validation...")

c1 = Res_Ma()
c1._con_1d()
