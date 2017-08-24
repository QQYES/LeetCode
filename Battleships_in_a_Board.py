class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        if board is None:
            return 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i != 0:
                    if j != 0:
                        if board[i][j] == '+':
                            if board[i - 1][j] == '.' and board[i][j] == '.':
                                count += 1
                    else:
                        if board[i][j] == '+':
                            if board[i - 1][j] == '.':
                                count += 1
                else:
                    if j != 0:
                        if board[i][j] == '+':
                            if board[i][j - 1] == '.':
                                count += 1
                    else:
                        if board[i][j] == '+':
                            count += 1
        return count
