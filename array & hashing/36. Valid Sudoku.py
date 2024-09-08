#36 valid suduoku
#https://leetcode.com/problems/valid-sudoku/
# determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# A partially filled sudoku which is valid.


#Example 1:
#Input: board =     [["5","3",".",".","7",".",".",".","."], ["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."], ["8",".",".",".","6",".",".",".","3"], ["4",".",".","8",".","3",".",".","1"], ["7",".",".",".","2",".",".",".","6"], [".","6",".",".",".",".","2","8","."], [".",".",".","4","1","9",".",".","5"], [".",".",".",".","8",".",".","7","9"]]
#Output: true


# code:
from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) #deafault dict is used to store the numbers that have been seen in the columns and initialize them to an empty set 
        rows = defaultdict(set) # in regular dict, we would have to check if the key is in the dict before adding the value to the set but with defaultdict, we don't have to do that.
        sq = defaultdict(set)   #set is used to store the numbers that have been seen in the 3x3 sub-boxes and initialize them to an empty set

        for r in range(9):
            for c in range(9):
                cell = board[r][c]  #get the cell value and its position

                if cell == '.':
                    continue

                if cell in rows[r] or cell in cols[c] or cell in sq[(r // 3, c // 3)]:
                    return False    #check if the cell value is in the rows, columns, or 3x3 sub-boxes, if it is, return False  
                rows[r].add(cell)
                cols[c].add(cell)
                sq[(r // 3, c // 3)].add(cell)

        return True


# Solution:
# 1. Create a dictionary for rows, columns, and 3x3 sub-boxes to store the numbers that have been seen. and initialize them to an empty set
# 2. Iterate through the board using two nested loops for rows and columns respectively   and get the cell value and its position
# 3. Check if the cell value is a dot, if it is, continue to the next iteration of the loop 
# 4. Check if the cell value is in the rows, columns, or 3x3 sub-boxes, if it is, return False for rows rows[r] used to check if the cell value is in the row, cols[c] used to check if the cell value is in the column, and sq[(r // 3, c // 3)] used to check if the cell value is in the 3x3 sub-boxes
# 5. Add the cell value to the rows, columns, and 3x3 sub-boxes if it is not in them already and continue to the next iteration of the loop 
# 6. Return True if the board is valid
# 7. The time complexity of this solution is O(1) because the board is always a 9x9 board   and the space complexity is O(1) because the board is always a 9x9 board
# 8. The solution passes all the test cases in Leetcode
# 9. The solution is optimal as it uses a dictionary to store the numbers that have been seen in the rows, columns, and 3x3 sub-boxes