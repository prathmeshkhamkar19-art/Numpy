# in this we add values in 2d array okkkkkkkkkkkk
# syntax for the command is 
# For adding value in 2d Avoid Append 
# for industry practice use alternative :
#     1.Concatinate - Join a sequence of arrays along an existing axis. combining multiple arrays
#     2.vstack -
#     3.hstack - 

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

    return arr  # this pass 2d matrix

def app(arr):
  
  print("\n To add as Row using vstack select(1)")
  print("\n To add as  Col using hstack select(2)")
  print("\n To add Normaly my geting input from user select (3).")
  opt=int(int(input("Enter 1 or 2 or 3 :")))
  if opt == 1:
     # row_arr = np.append(arr,[45,0],axis =0)                 #Error due to given is 2d matrix and we insert the 1d matrix
    #   np_array3 = np.concatenate([arr,row_arr],axis=0)
      
      #Solution  - 

        new_row = [45] * arr.shape[1]      # it get number of col in  arr and make in 1d(row wise LIST) using arr.shape*[1] and mul by val 45 make [45,45,45]
        result = np.vstack((arr, new_row))   #it create new array by adjusting new arr - new_row with arr using np.vstak
        print("\nAfter Adding Row:")
        print(result)
  
  elif opt == 2:
     new_col = [354]*arr.shape[0]   #it get number of col in  arr and make in 1d(col wise LIST) using arr.shape*[0] and mul by val 354 make [354 , 354]
     new_arr =np.hstack((arr,new_col))
     print("New array Colm wise :")
     print(new_arr)
  
  elif opt==3:
      print("Add Row ...click(1)")
      print("Add Col ...click (2)") 
      opt_2 = int(input("Enter the option :"))
     
      if opt_2 ==1:
          if opt_2 == 1:
           new_sim_row = list(map(int, input("Enter row values: ").split()))

          if len(new_sim_row) != arr.shape[1]:
           print("Error: Column count must match")
          else:
           simp_arr = np.vstack((arr, new_sim_row))
          print("New array after row wise simple array:")
          print(simp_arr)
      elif opt_2 == 2 :
         
        new_sim_col = list(map(int, input("Enter column values: ").split()))

        if len(new_sim_col) != arr.shape[0]:
           print("Error: Row count must match")
        else:
         new_sim_col = np.array(new_sim_col).reshape(-1,1)
         simp_arr = np.hstack((arr, new_sim_col))
         print("New array after column wise simple array:")
         print(simp_arr)
 
  else :print("Wrong indentation.. ")
      
arr1=data()
app(arr1)


# ✔ Avoid append() for 2D
# ✔ Use vstack() for row
# ✔ Use hstack() for column
# ✔ Use np.full() when filling with same value
# ✔ Always check arr.shape