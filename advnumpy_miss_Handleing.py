#in which we use 3 function 
# 1. np.isnan -- detect missing value from array
#                 return only boolean var (True or False)
# 2. np.nan_to_num()  - it Replace the missing or nan into int value
# 3. np.isinf()  - it detect the value thst go infinite
import numpy as np


# Create array with normal, NaN and infinite values
arr = np.array([10, 20, np.nan, 40, np.inf, -np.inf, 60])

print("Original Array:")
print(arr)

# 1️⃣ Detect NaN values
print("\nUsing np.isnan():")
print(np.isnan(arr))

# 2️⃣ Detect Infinite values
print("\nUsing np.isinf():")
print(np.isinf(arr))

# 3️⃣ Replace NaN and Infinite values
clean_arr = np.nan_to_num(arr, nan=0, posinf=999, neginf=-999)

print("\nAfter using np.nan_to_num():")
print(clean_arr)