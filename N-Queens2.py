"""
Leetcode : 52
Problem Statement : https://leetcode.com/problems/n-queens-ii/description/
"""

class Solution:
    # Initalize main function and call the helper function
    def totalNQueens(self, n: int) -> int:
        # Initializing variables
        count = 0
        cols = set()
        diag1 = set()
        diag2 = set()

        # Backtrack function recursively places a queen on the board
        def backtrack(row):
            # Declare count as a nonlocal variable to keep track of the number of valid solutions.
            nonlocal count
            # When all rows are filled, increment the solution count.
            if row == n:
                # A valid board configuration is found and added to result
                count += 1
                return
            # Loop through the columns -> Trying to place a queen in each column of the current row
            for col in range(n):
                # Check Constraints -> Skip placing the queen in the colums or digonals already occupied
                # here (row - col) = bottom left diagonal and (row + col) = bottom right
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                # Place the queen on the board and Mark the constraints
                cols.add(col)  # Same column constraint
                diag1.add(row - col)  # Bottom left diagonal
                diag2.add(row + col)  # Bottom right diagonal
                # Recursive call -> Move to the next row
                backtrack(row + 1)
                # Backtrack: Unmark the columns and diagonals
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        # Start backtracking from the first row and place the queen
        backtrack(0)
        # Return all the found results
        return count