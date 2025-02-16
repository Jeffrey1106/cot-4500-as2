import numpy as np 

# Problem 1: Neville's Method
def neville_method(x_vals, y_vals, x):
    n = len(x_vals)
    Q = np.zeros((n, n))
    Q[:, 0] = y_vals
    
    for j in range(1, n):
        for i in range(n - j):
            Q[i, j] = ((x - x_vals[i + j]) * Q[i, j - 1] - (x - x_vals[i]) * Q[i + 1, j - 1]) / (x_vals[i] - x_vals[i + j])

    return Q[0, n - 1]

# Problem 2 & 3: Newton's Divided Differences and Interpolation
def newton_forward_difference(x_vals, y_vals):
    n = len(x_vals)
    coef = np.zeros([n, n])
    coef[:, 0] = y_vals
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x_vals[i + j] - x_vals[i])

    return coef

def interpolate_newton(x_vals, coef, x):
    n = len(x_vals)
    result = coef[0, 0]
    product_term = 1.0

    for i in range(1, n):
        product_term *= (x - x_vals[i - 1])
        result += coef[0, i] * product_term

    return result

# Problem 4: Hermite Interpolation Matrix with Z-values in the first column
def hermite_interpolation(x, f, df):
    n = len(x)
    z = np.zeros(2 * n)
    Q = np.zeros((2 * n, 5))  # 5 columns including z-values
    
    for i in range(n):
        z[2 * i] = x[i]
        z[2 * i + 1] = x[i]
        Q[2 * i, 0] = x[i]  # Store z-values
        Q[2 * i + 1, 0] = x[i]
        Q[2 * i, 1] = f[i]  # Store function values
        Q[2 * i + 1, 1] = f[i]
        Q[2 * i + 1, 2] = df[i]  # Store derivative values
        if i != 0:
            Q[2 * i, 2] = (Q[2 * i, 1] - Q[2 * i - 1, 1]) / (z[2 * i] - z[2 * i - 1])
    
    for j in range(3, 5):  # Fill in remaining columns (2nd and 3rd divided differences)
        for i in range(3, 2 * n):
            Q[i, j] = (Q[i, j - 1] - Q[i - 1, j - 1]) / (z[i] - z[i - j + 1])

    return Q

# Problem 5 cubic spline interpolation
def cubic_spline_interpolation(x, y):
    n = len(x) - 1
    h = np.diff(x)

    # Step 1: Construct the matrix A
    A = np.zeros((n + 1, n + 1))
    A[0, 0] = 1  # Natural spline condition
    A[n, n] = 1  # Natural spline condition

    for i in range(1, n):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]

    # Step 2: Construct the vector b
    b = np.zeros(n + 1)
    for i in range(1, n):
        b[i] = 3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

    # Step 3: Solve for c
    c = np.linalg.solve(A, b)

    # Step 4: Solve for b and d
    b_coeffs = np.zeros(n)
    d_coeffs = np.zeros(n)
    for i in range(n):
        b_coeffs[i] = (y[i + 1] - y[i]) / h[i] - h[i] * (2 * c[i] + c[i + 1]) / 3
        d_coeffs[i] = (c[i + 1] - c[i]) / (3 * h[i])

    # Step 5: Output matrix A, vector b, and vector x (c values)
    print(A)
    print(b)
    print(c)
