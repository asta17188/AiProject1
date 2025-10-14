from games import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""

    def __init__(self, board=[3,1]):
        moves = [(i, y)
         for i, count in enumerate(board)
         for y in range(1, count + 1)]
        self.initial = GameState(to_move='MAX', utility=0, board=board, moves=moves)


    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves

    def result(self, state, move):
        if self.terminal_test(state): # Test to see if we are at the end of the game
            return state
        #subtracts amount from row
        new_board = state.board
        new_board[move[0]] -= move[1]
        new_moves = [(i, y)
         for i, count in enumerate(state.board)
         for y in range(1, count + 1)]
        other_player = ""
        if other_player == 'MAX':
            other_player = 'MIN'
        else:
            other_player = 'MAX'
        return GameState(to_move=other_player, utility=state.utility, board=new_board, moves=new_moves)

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        if (self.terminal_test(state)):
            if player == 'MAX':
                return 1
            else:
                return -1
        else:
            return 0

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
            #if a number other than zero is encountered game is not over
        for x in state.board:
            if x != 0:
                return False
        #no non zeroes were found game is over
        return True

    def display(self, state):
        board = state.board
        print("board: ", board)


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    #print(nim.initial.board) # must be [0, 5, 3, 1]
    #print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1,3) ))
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")