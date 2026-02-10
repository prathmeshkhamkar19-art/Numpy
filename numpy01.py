import numpy as np   # import numpy package

class Numpy:

    def __init__(self):
        self.size = int(input("Enter the size of array: "))   #this is instance variable 

        print("\nChoose input type:")
        print("1. 1D Array")
        print("2. 2D Array")

        self.option = int(input("Enter your choice: ")) 

    def get_in_1D(self):                                  # function for get input from user for 1 d
        arr_1d = np.zeros(self.size, dtype=int)

        for i in range(self.size):                     #using normal loop 
            arr_1d[i] = int(input(f"Enter value at index {i}: "))

        return arr_1d            # return the array

    def get_in_2D(self):                                   # function for get input from user for 1 d
        print(f"Enter {self.size} rows (space separated values):")
        arr_2d = np.array([list(map(int, input().split())) for _ in range(self.size)])
        
        # New method for inpuut
       # np.array() - Converts Python list into NumPy array
       # input() - Takes one full line input
       # .split() - Splits input into separate value
       # map(int, ...) - Converts each value into integer
        #list(...) - Converts mapped values into list
       # list(map(...)) - Creates one complete row
       
        return arr_2d          

    def get_input(self):                            # function used for run condition only
        if self.option == 1:
            return self.get_in_1D(), None          #it is return the 1st func for 1d and another is none for print 
        elif self.option == 2:
            return None, self.get_in_2D()        #it return when get_input call then it store val in arr_1d = none and other
        else:
            print("Invalid choice!")
            return None, None

    def print_array(self, arr_1d, arr_2d):      
        if arr_1d is not None:            #with the help of is not "identify oper " print funnction used
            print("\n1D Array:")
            print(arr_1d)

        if arr_2d is not None:
            print("\n2D Array:")
            print(arr_2d)


# -------- MAIN PROGRAM --------

n1 = Numpy()
arr_1d, arr_2d = n1.get_input()
n1.print_array(arr_1d, arr_2d)
