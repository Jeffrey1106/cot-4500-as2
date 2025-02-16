import numpy as np
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))

# Import functions from assignment_2.py
from assignment_2 import (
    neville_method,
    newton_forward_difference,
    interpolate_newton,
    hermite_interpolation,
    cubic_spline_interpolation
)

# Problem 1 Execution
x_vals1 = [3.6, 3.8, 3.9]
y_vals1 = [1.675, 1.436, 1.318]
x_target = 3.7
print(neville_method(x_vals1, y_vals1, x_target))

# Problem 2 & 3 Execution
x_vals2 = [7.2, 7.4, 7.5, 7.6]
y_vals2 = [23.5492, 25.3913, 26.8224, 27.4589]
coef_matrix = newton_forward_difference(x_vals2, y_vals2)
print(f"\n{coef_matrix[0,1]}\n{coef_matrix[0,2]}\n{coef_matrix[0,3]}\n")

x_target2 = 7.3
print(f"{interpolate_newton(x_vals2, coef_matrix, x_target2)}\n")

# Problem 4 Execution
x_h = np.array([3.6, 3.8, 3.9])
f_h = np.array([1.675, 1.436, 1.318])
df_h = np.array([-1.195, -1.188, -1.182])

hermite_table = hermite_interpolation(x_h, f_h, df_h)

# Printing the Hermite Matrix with z-values in the first column
print(f"{hermite_table}\n")

# Problem 5 Execution
x_vals = np.array([2, 5, 8, 10])
y_vals = np.array([3, 5, 7, 9])

cubic_spline_interpolation(x_vals, y_vals)