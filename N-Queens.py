from typing import List
"""
Leetcode : 51
Problem Statement : https://leetcode.com/problems/n-queens/description/
"""

class Solution:
    # Initalize main function and call the helper function
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Initializing variables
        result = []
        board = [["." for _ in range(n)] for _ in range(n)]
        cols = set()
        diag1 = set()
        diag2 = set()

        # Backtrack function recursively places a queen on the board
        def backtrack(row):
            # Breaking condition if we reach the last row
            if row == n:
                # A valid board configuration is found and added to result
                result.append(["".join(row) for row in board])
                return
            # Loop through the columns -> Trying to place a queen in each column of the current row
            for col in range(n):
                # Check Constraints -> Skip placing the queen in the colums or digonals already occupied
                # here (row - col) = bottom left diagonal and (row + col) = bottom right
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                # Place the queen on the board
                board[row][col] = "Q"
                # Mark the constraints
                cols.add(col)  # Same column constraint
                diag1.add(row - col)  # Bottom left diagonal
                diag2.add(row + col)  # Bottom right diagonal
                # Recursive call -> Move to the next row
                backtrack(row + 1)
                # Backtrack: remove the queen and free the columns and diagonals
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        # Start backtracking from the first row and place the queen
        backtrack(0)
        # Return all the found results
        return result