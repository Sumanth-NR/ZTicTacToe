from typing import Any

from ._zt_core import ZTEngineFirst, ZTPlayerFirst


class PvC:
    """Player vs Computer Tic Tac Toe game

    This class provides an interface for playing against an AI opponent.
    The AI uses a near-perfect strategy to play the game.

    Example:
        >>> game = PvC(engine_first=False)  # Player goes first
        >>> game.play(4)  # Player plays center
        >>> print(game.board)  # AI has already responded
    """

    def __init__(self, _engine_first: bool = True) -> None:
        """Initialize a new Player vs Computer game

        :param _engine_first: If True, the AI plays first; if False, the player plays first
        :type _engine_first: bool
        :return: None
        """
        self._engine: ZTEngineFirst | ZTPlayerFirst
        if _engine_first:
            self._engine = ZTEngineFirst()
        else:
            self._engine = ZTPlayerFirst()

    def play(self, pos: int) -> None:
        """Plays the player's move and triggers the AI's response

        :param pos: The position to play (0-8, row-major order from top-left)
        :type pos: int
        :return: None
        :raise: ZTGameException if the game is not in progress
        :raise: ZTInvalidInput if the move is invalid
        """
        self._engine.play(pos)

    def __getattr__(self, name: str) -> Any:
        """Delegate all other attribute access to the underlying engine

        :param name: The attribute name to access
        :type name: str
        :return: The attribute value from the underlying engine
        :rtype: Any
        """
        return getattr(self._engine, name)
