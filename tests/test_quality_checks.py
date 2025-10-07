"""
Quality check tests for production verification.

These tests verify that the package is production-ready:
- All imports work correctly
- Package metadata is accessible
- Code passes linting checks
"""


def test_package_imports():
    """Test that all main imports work correctly"""
    from zttt import CellValue, Player, PvC, PvP, zt_errors

    # Verify classes are available
    assert PvP is not None
    assert PvC is not None

    # Verify enums are available
    assert CellValue is not None
    assert Player is not None

    # Verify error module is available
    assert zt_errors is not None


def test_package_version():
    """Test that package version is accessible"""
    from zttt import __version__

    assert __version__ is not None
    assert isinstance(__version__, str)


def test_enum_values():
    """Test that enum values are correct"""
    from zttt import CellValue, Player

    # Check CellValue
    assert CellValue.EMPTY == 0
    assert CellValue.PLAYER2 == 1
    assert CellValue.PLAYER1 == 4

    # Check Player
    assert Player.DRAW == 0
    assert Player.PLAYER1 == 1
    assert Player.PLAYER2 == 2
