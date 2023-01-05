class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                val=board[i][j]
                if val!=".":
                    for k in range(9):
                        if j!=k and val==board[i][k]:
                            return False
                    for k in range(9):
                        if i!=k and val==board[k][j]:
                            return False
                    for k in range(3):
                        for l in range(3):
                            if 3*(i//3)+k !=i and 3*(j//3)+l!=j and val==board[3*(i//3)+k][3*(j//3)+l]:
                                return False
                                
        return True