import numpy as np

class Split:
    def Data(self):
        self.array_1d = np.array([2,5,6])
        self.array_2d = np.array([[2,4,7],[23,5,2]])
        self.array_3d = np.array([[[2,4,5],[3,5,3]],[[3,5,6],[3,7,3]]])

    def option(self):
        print("1 for 1D\n2 for 2D\n3 for 3D")
        self.opt = int(input("Enter your choice: "))
        
        if self.opt == 1:
            self.for1d()
        elif self.opt == 2:
            self.for2d()
        elif self.opt == 3:
            self.for3d()
        else:
            print("Invalid choice")

    def for1d(self):
        print("Original 1D array:", self.array_1d)
        parts = np.array_split(self.array_1d, 3)  # safe split
        print("Split result:", parts)

    def for2d(self):
        print("Original 2D array:\n", self.array_2d)
        parts = np.array_split(self.array_2d, 2, axis=0)  # split along rows
        vs = np.array_split(self.array_2d, 2, axis=0)     # vertical split
        hs = np.array_split(self.array_2d, 2, axis=1)     # horizontal split
        print("Array split along rows:", parts)
        print("Vertical split:", vs)
        print("Horizontal split:", hs)

    def for3d(self):
        print("Original 3D array:\n", self.array_3d)
        axis = int(input("Split along axis 0, 1, or 2? Enter axis: "))
        parts = np.array_split(self.array_3d, 2, axis=axis)
        print("Split result:", parts)

# Usage
c1 = Split()
c1.Data()
c1.option()