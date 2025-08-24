from collections import deque
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        length = len(board)
        board.reverse()
        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length

            if r % 2:
                c = length - 1 - c
            return [r,c]

        q = deque() 
        q.append([1,0])

        visited = set()

        while q:
            square, moves = q.popleft()
            for i in range(1,7):
                nextSquare = square + i 
                r,c = intToPos(nextSquare)

                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    q.append([nextSquare,moves+1])

        return -1
    

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]

sol = Solution()
print(sol.snakesAndLadders(board))


"""
Its a bfs and save in the queue square and moves, if it is visited, not visist again,
put visit of node as set
"""