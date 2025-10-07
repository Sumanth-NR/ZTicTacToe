"""
Production quality tests for ZTicTacToe backend.

These tests verify production-ready behavior including:
- Error handling
- Type safety
- Edge cases
- API consistency
"""


def test_invalid_position_error():
    """Test that invalid positions raise appropriate errors"""
    from zttt import PvP
    from zttt.zt_errors import ZTInvalidInput

    game = PvP()

    # Test out of bounds
    try:
        game.play(-1)
        raise AssertionError("Should have raised ZTInvalidInput")
    except ZTInvalidInput as e:
        assert "Position must be between 0 and 8" in str(e)

    try:
        game.play(9)
        raise AssertionError("Should have raised ZTInvalidInput")
    except ZTInvalidInput as e:
        assert "Position must be between 0 and 8" in str(e)


def test_position_already_taken_error():
    """Test that playing on occupied position raises error"""
    from zttt import PvP
    from zttt.zt_errors import ZTInvalidInput

    game = PvP()
    game.play(0)

    try:
        game.play(0)
        raise AssertionError("Should have raised ZTInvalidInput")
    except ZTInvalidInput as e:
        assert "not available" in str(e).lower() or "already taken" in str(e).lower()


def test_game_over_error():
    """Test that moves after game over raise error"""
    from zttt import PvP
    from zttt.zt_errors import ZTGameException

    game = PvP()
    # Player 1 wins
    game.play(0)
    game.play(1)
    game.play(3)
    game.play(2)
    game.play(6)

    assert game.status is False
    assert game.winner == 1

    try:
        game.play(4)
        raise AssertionError("Should have raised ZTGameException")
    except ZTGameException as e:
        assert "not in progress" in str(e).lower()


def test_enums_exported():
    """Test that enums are properly exported"""
    from zttt import CellValue, Player

    assert hasattr(CellValue, "EMPTY")
    assert hasattr(CellValue, "PLAYER1")
    assert hasattr(CellValue, "PLAYER2")

    assert hasattr(Player, "DRAW")
    assert hasattr(Player, "PLAYER1")
    assert hasattr(Player, "PLAYER2")


def test_pvc_delegation():
    """Test that PvC properly delegates to engine"""
    from zttt import PvC

    game = PvC(False)
    assert hasattr(game, "board_list")
    assert hasattr(game, "status")
    assert hasattr(game, "turn")
    assert hasattr(game, "winner")
    assert hasattr(game, "history")
    assert hasattr(game, "empty_positions")


def test_immutable_board_list():
    """Test that board_list returns a copy"""
    from zttt import PvP

    game = PvP()
    board1 = game.board_list
    board1[0] = 999

    board2 = game.board_list
    assert board2[0] == 0, "Board list should be immutable"


def test_immutable_history():
    """Test that history returns a copy"""
    from zttt import PvP

    game = PvP()
    game.play(0)

    history1 = game.history
    history1.append(999)

    history2 = game.history
    assert 999 not in history2, "History should be immutable"


def test_empty_positions_updated():
    """Test that empty_positions is properly updated"""
    from zttt import PvP

    game = PvP()
    assert len(game.empty_positions) == 9
    assert 0 in game.empty_positions

    game.play(0)
    assert len(game.empty_positions) == 8
    assert 0 not in game.empty_positions


def test_turn_alternates():
    """Test that turns alternate between players"""
    from zttt import PvP

    game = PvP()
    assert game.turn == 1

    game.play(0)
    assert game.turn == 2

    game.play(1)
    assert game.turn == 1


def test_winner_values():
    """Test winner values for different outcomes"""
    from zttt import PvP

    # Player 1 wins
    game1 = PvP()
    game1.play(0)
    game1.play(1)
    game1.play(3)
    game1.play(2)
    game1.play(6)
    assert game1.winner == 1

    # Draw
    game2 = PvP()
    game2.play(1)
    game2.play(2)
    game2.play(3)
    game2.play(4)
    game2.play(5)
    game2.play(0)
    game2.play(6)
    game2.play(7)
    game2.play(8)
    assert game2.winner == 0

    # Game in progress
    game3 = PvP()
    assert game3.winner is None


def test_highlighted_positions():
    """Test that winning positions are highlighted"""
    from zttt import PvP

    game = PvP()
    game.play(0)
    game.play(1)
    game.play(3)
    game.play(2)
    game.play(6)

    highlighted = game.highlighted
    assert len(highlighted) > 0
    assert 0 in highlighted
    assert 3 in highlighted
    assert 6 in highlighted


def test_board_string_format():
    """Test that board string is properly formatted"""
    from zttt import PvP

    game = PvP()
    board = game.board
    assert isinstance(board, str)
    assert "X" not in board  # Empty board
    assert "O" not in board

    game.play(0)
    board = game.board
    assert "X" in board


def test_on_move_callback():
    """Test on_move callback is called correctly"""
    from zttt import PvP

    moves = []

    def track_moves(player, pos):
        moves.append((player, pos))

    game = PvP()
    game.on_move = track_moves

    game.play(0)
    game.play(1)

    assert len(moves) == 2
    assert moves[0] == (1, 0)
    assert moves[1] == (2, 1)


def test_on_finish_callback():
    """Test on_finish callback is called correctly"""
    from zttt import PvP

    winners = []

    def track_winner(winner):
        winners.append(winner)

    game = PvP()
    game.on_finish = track_winner

    game.play(0)
    game.play(1)
    game.play(3)
    game.play(2)
    game.play(6)

    assert len(winners) == 1
    assert winners[0] == 1
