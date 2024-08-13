# Task: Implement Gauss-Jordan elimination in Python to solve a system of linear equations.


# 1. Import the numpy library for matrix and vector operations.



# 2. Create a function divide_row that divides row i of matrix A by a divisor.
#    - Parameters:
#      - A: The matrix where the row will be divided.
#      - i: The index of the row to be divided.
#      - divisor: The value by which the row will be divided.
# Note: This function will not return anything, it should update A in-place.



# 3. Create a function subtract_rows that subtracts multiplier times row j from row i.
#    - Parameters:
#      - A: The matrix where the operation will occur.
#      - i: The index of the row to be modified.
#      - j: The index of the row to subtract.
#      - multiplier: The value to multiply row j by before subtracting it from row i.
# Note: This function will not return anything, it should update A in-place.



# 4. Create the main function gauss_jordan_elimination that uses the functions above to solve Ax = b.
#    - Parameters:
#      - A: The coefficient matrix of the system of equations.
#      - b: The constant vector.



    # 5. Initialize the variable Ab to be the augmented matrix of A with vector b.
    # Hint: Use the hstack method from numpy.



    # 6. Redefine Ab to have a float data type to avoid integer division.



    # 7. Iterate through each column of the matrix A.



        # 8. Use the appropriate row operation function from above to make this column's
        # corresponding diagonal entry 1.



        # 9. Iterate through each row of the column.



            # 10. Use the appropriate row operation to make the entry
            # in this row and column equal to 0 (skip the diagonal entry).



    # 11. Return the last column which is the solution vector.


