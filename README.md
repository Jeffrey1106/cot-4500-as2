# Programming Assignment 2

## 📖 Description
This assignment focuses on numerical interpolation methods covered in Chapter 3, including:
- **Neville's Method**
- **Newton's Divided Difference Interpolation**
- **Hermite Interpolation**
- **Cubic Spline Interpolation**

These methods help approximate function values at given points using different polynomial techniques.

## 📌 Project Structure
```
PA2/
├── src/
│   ├── main/
│   │   ├── __init__.py
│   │   └── assignment_2.py
│   └── test/
│       ├── __init__.py
│       └── test_assignment_2.py
├── requirements.txt
└── README.md
```

## 🚀 Compilation & Execution Instructions
1. **Install Dependencies (if needed)**:
   - Ensure you have Python installed (`>=3.7`).
   - Install required libraries using:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the Test Cases**:
   - To verify outputs using `test_assignment_2.py`, run:
     ```bash
     python src/test/test_assignment_2.py
     ```

## 📌 Problem Breakdown
### ✅ **Problem 1: Neville’s Method**
- Implements **Neville’s iterative interpolation algorithm**.
- Computes the interpolated value at `x = 3.7` using the given dataset.

### ✅ **Problem 2 & 3: Newton's Divided Difference Method**
- Constructs **Newton’s divided difference table** for polynomial interpolation.
- Computes coefficients for degrees **1, 2, and 3**.
- Approximates `f(7.3)` using Newton's interpolating polynomial.

### ✅ **Problem 4: Hermite Polynomial Interpolation**
- Uses the **divided difference method** to construct the **Hermite interpolation table**.
- Incorporates both function values and derivatives to refine the polynomial.
- Outputs the structured Hermite **approximation matrix**.

### ✅ **Problem 5: Cubic Spline Interpolation**
- Constructs the **natural cubic spline** for the given dataset.
- Solves the tridiagonal system for spline coefficients.
- Outputs **Matrix A, Vector b, and Vector x** representing the system.

## 📜 Expected Output
The program prints the required results for each problem, including:
- Interpolated values for Neville's and Newton’s methods.
- Divided difference and Hermite interpolation tables.
- Cubic spline system matrices.

## 📌 Author
Jeffrey Chang 
Course: COT-4500 - Numerical Calculus  
Assignment: Programming Assignment 2

