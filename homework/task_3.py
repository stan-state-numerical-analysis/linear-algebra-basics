# Task: Implement the LU Decomposition Method for Solving a System of Equations

# 1. Import the numpy library, which will be used for matrix operations.



# 2. Define a function lu_decomposition that returns two matrices L (lower triangular) and
# U (upper triangular) so that A = LU.
#    - Parameters:
#      - A: The square matrix whose LU decomposition is to be computed.



    # 3. Initialize a variable n to be the number of rows of A.



    # 4. Initialize the L and U matrices as all zeroes with the correct
    # dimensions and float data type.



    # 5. Iterate over each row of A.



        # 6. Iterate over each column in the row from the diagonal entry onwards.



            # 7. Assign the entry i, j of the upper triangular matrix U
            # with the corresponding value.



        # 8. Iterate over each column in the row from the diagonal entry onwards.



            # 9. Assign the entry i, j of the lower triangular matrix L
            # with the corresponding value.

            

    # 10. Return the matrices L and U.




# 11. Define a function forward_substitution that solves the system Ly = b for y using forward substitution.
#    - Parameters:
#      - L: The lower triangular matrix.
#      - b: The right-hand side vector of the equation Ly = b.



    # 12. Initialize the vector y as all zeroes with the correct length
    # and float data type.



    # 13. Iterate through each row of L.



        # 14. Update the entry of y using the forward substitution formula.



    # 15. Return the solution vector y.



# 16. Define a function backward_substitution that solves the system Ux = y for x using backward substitution.
#    - Parameters:
#      - U: The upper triangular matrix.
#      - y: The right-hand side vector of the equation Ux = y.



    # 17. Initialize the vector x as all zeroes with the correct length
    # and float data type.



    # 18. Iterate through each row of U.



        # 19. Update the entry of x using the backward substitution formula.
        # Be sure to start from the bottom up.



    # 20. Return the solution vector x.



# 21. Define a main function solve_lu that combines LU decomposition, forward substitution,
# and backward substitution to solve the system Ax = b.
#    - Parameters:
#      - A: The square matrix of coefficients of the equation Ax = b.
#      - b: The right-hand side vector of the equation Ax = b.



    # 22. Find the LU-decomposition of A.
    # Call the outputs L and U.



    # 23. Apply forward subsitution with the correct matrix and vector.
    # Call the output y.



    # 24. Apply backward substitution with the correct matrix and vector.
    # Call the output x.



    # 25. Return the solution vector x.

