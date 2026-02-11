# # checking the nnumpy propertie
import numpy as np

# class Pro:
#     def __init__(self):     #Constuctor
#      self.arr_1d =np.array([1,2,33,77])      # 1 Dimension array 
#      self.arr_2d =np.array([[1,3,5],[34,5,6]])  # 2 Dimension array of 2(row) * 3(col)

#      print("Select choise to print Prop of Array:\n")
#      print("1.for 1 D. ")
#      print("2.for 2D. ")
#      print("3.for 3D.")
#      self.arr_op = int(input("Enter :"))

     
#      print("1.Check Shape")
#      print("1.Check size")
#      print("1.Check ndim")
#      print("1.Check dtype")
#      self. opt =int(input("Enter the Choise to Check prop :\n"))
     
     
     
#      def aray_s(self):
#        if self.arr_op == 1 :
#           return self.chk_1d(),None
#        elif self.arr_op == 2 :
#           return None,self.chk_2d()
#        else:
#           return self.chk_1d(),self.chk_2d()
          
#     def chk_1d(self):
#        if self.opt == 1:
#           print("Shape of 1d - ",self.arr_1d.shape)
#        elif self.opt == 2:
#           print("size of 1d - ",self.arr_1d.size)
#        elif self.opt == 3:
#           print("Dimension of 1d - ",self.arr_1d.ndim)
#        elif self.opt == 4:
#           print("Datatype of 1 d array is : ",self.arr_1d.dtype)
          
#     def chk_2d(self):
#         if self.opt == 1:
#           print("Shape of 2d - ",self.arr_2d.shape)
#         elif self.opt == 2:
#            print("size of 2d - ",self.arr_2d.size)
#         elif self.opt == 3:
#           print("Dimension of 2d - ",self.arr_2d.ndim)
#         elif self.opt == 4:
#           print("Datatype of 2d array is : ",self.arr_2d.dtype)

# p1 = Pro()
# p1.aray_s()
          
          
    




# using chatgpt for repeated ask 

# checking the numpy properties
#import numpy as np

class Pro:
    def __init__(self):
        # Arrays
        self.arr_1d = np.array([1, 2, 33, 77])
        self.arr_2d = np.array([[1, 3, 5], [34, 5, 6]])

    def menu_array(self):
        """ Loop for selecting array type """
        while True:
            print("\nSelect choice to print properties of Array:")
            print("1. 1D Array")
            print("2. 2D Array")
            print("e. Exit")

            self.arr_op = input("Enter: ").lower()

            if self.arr_op == 'e':
                print("Exiting Array Menu...")
                break

            elif self.arr_op in ('1', '2'):
                self.menu_property()

            else:
                print("❌ Invalid choice! Try again.")

    def menu_property(self):
        """ Loop for selecting property """
        while True:
            print("\nSelect property to check:")
            print("1. Shape")
            print("2. Size")
            print("3. ndim")
            print("4. dtype")
            print("e. Exit")

            opt = input("Enter choice: ").lower()

            if opt == 'e':
                print("Back to Array Menu...")
                break

            elif opt in ('1', '2', '3', '4'):
                self.opt = int(opt)
                self.aray_s()

            else:
                print("❌ Invalid choice! Try again.")

    def aray_s(self):
        if self.arr_op == '1':
            self.chk_1d()
        elif self.arr_op == '2':
            self.chk_2d()

    def chk_1d(self):
        if self.opt == 1:
            print("Shape of 1D:", self.arr_1d.shape)
        elif self.opt == 2:
            print("Size of 1D:", self.arr_1d.size)
        elif self.opt == 3:
            print("Dimensions of 1D:", self.arr_1d.ndim)
        elif self.opt == 4:
            print("Datatype of 1D:", self.arr_1d.dtype)

    def chk_2d(self):
        if self.opt == 1:
            print("Shape of 2D:", self.arr_2d.shape)
        elif self.opt == 2:
            print("Size of 2D:", self.arr_2d.size)
        elif self.opt == 3:
            print("Dimensions of 2D:", self.arr_2d.ndim)
        elif self.opt == 4:
            print("Datatype of 2D:", self.arr_2d.dtype)


# Run
p1 = Pro()
p1.menu_array()
