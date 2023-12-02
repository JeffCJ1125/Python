"""Numpy index and slice practice"""

import numpy as np


l1 = [[f"{row},{col}" for col in range(0, 4)] for row in range(0, 4)]
print(f"l1 {l1}")

npl1 = np.array(l1)

print(f"npl1 \n {npl1}")
# basic index
print(f"npl1[3][2] {npl1[3][2]}")
print(f"npl1[3,2] {npl1[3,2]}")

# array indexing
row_select_index = [1, 3]
col_select_index = [0, 2]
print(f"npl1 row_select_index \n {npl1[row_select_index]}")
print(f"npl1 col_select_index \n {npl1[:,col_select_index]}")
print(
    f"npl1[row_select_index,col_select_index]  \n {npl1[row_select_index,col_select_index]}"
)

npl2 = np.array([[row + col for col in range(0, 3)] for row in range(0, 3)])
print(f"npl2 \n {npl2}")


# boolean index
print(f"npl2 >= 3 \n {npl2 >= 3}")
print(f"npl2[npl2 >= 3] \n {npl2[npl2 >= 3]}")

# mask
mask = np.zeros(npl2.shape)
mask[npl2 >= 3] = 1
print(f"mask \n {mask}")
print(f"npl2 \n {mask * npl2}")

# slicing
print(f"npl1[:,:]\n {npl1[:,:]}")
print(f"npl1[2:,:3]\n {npl1[2:,:3]}")
print(f"npl1[0:2,1:4] \n {npl1[0:2,1:4]}")
