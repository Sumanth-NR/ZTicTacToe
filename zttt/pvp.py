from ._zt_core import ZTBaseBoard


class PvP(ZTBaseBoard):
    """Player vs Player Tic Tac Toe game
    
    This class provides a simple interface for a two-player Tic Tac Toe game.
    Players alternate turns, with Player 1 (X) going first.
    
    Example:
        >>> game = PvP()
        >>> game.play(0)  # Player 1 plays top-left
        >>> game.play(4)  # Player 2 plays center
        >>> print(game.board)
    """

    def __init__(self) -> None:
        """Initialize a new Player vs Player game"""
        super().__init__()

    def play(self, pos: int) -> None:
        """Plays the current player's move at the position specified

        :param pos: The position to play (0-8, row-major order from top-left)
        :type pos: int
        :return: None
        :raise: ZTGameException if the game is not in progress
        :raise: ZTInvalidInput if the move is invalid
        """
        if self.turn == 1:
            super()._play_player_one_move(pos)
        else:
            super()._play_player_two_move(pos)
