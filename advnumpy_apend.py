# in this we add values in 2d array okkkkkkkkkkkk
# syntax for the command is 
# new_array = np.append(old_array,[val])     no need to mention axis 

# Main Error :  ValueError: all the input arrays must have same number of dimensions,
#              but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)

import numpy as np

def data():
    row = int(input("\nEnter the row of array : "))
    col = int(input("Enter the col of array : "))

    arr = np.zeros((row, col), int)

    for i in range(row):
        for j in range(col):
            val = int(input(f"Enter value for position [{i}][{j}] : "))
            arr[i][j] = val

    print("\nYour 2D Array is:")
    print(arr)

    return arr

def app(arr):
  #to append the val in last as per row
  print("\n To add as er Row select(1)")
  print("\n To add as er Col select(2)")
  opt=int(int(input("Enter 1 or 2 only")))
  if opt == 1:
      row_arr = np.append(arr,[45],axis =0)
      np_array3 = np.concatenate([arr,row_arr])
      print(np_array3)
      print(row_arr)
  elif opt == 1:
      col_arr = np.append(arr,[354],axis =1)
      print(col_arr)
  else :
      print("Wrong indentation.. ")


arr1=data()
app(arr1)