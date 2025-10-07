# ZTicTacToe

Tic Tac Toe is a famous game in which two players take turns placing
a mark on a 3x3 grid. The first player to get three in a row wins.

The module is a standalone implementation of the game TicTacToe
providing functionality to keep track of the game's state and to
make moves.

## Features

- Standalone implementation of the game Tic Tac Toe.
- Provides a way to customise **move triggers** and access state variables.
- Comes with an engine with near perfect moves.
- Written in Python from scratch and does not require any external libraries.
- Can be integrated into a larger project, with very little effort.
- Throws custom-built errors making it easy to debug and handle errors.

## Links

- [PyPI](https://pypi.python.org/pypi/zttt)
- [GitHub](https://github.com/Sigma1084/ZTicTacToe/tree/v1)
- [Documentation](https://ztictactoe.readthedocs.io/en/v1/)
- [Examples](https://github.com/Sigma1084/ZTicTacToe/tree/v1/examples)

## Installation

```bash
pip install zttt
```

## Quick Start

### Player vs Player

```python
from zttt import PvP

game = PvP()
game.play(0)  # Player 1 plays top-left
game.play(4)  # Player 2 plays center
print(game.board)
```

### Player vs Computer

```python
from zttt import PvC

game = PvC(engine_first=False)  # Player goes first
game.play(4)  # Player plays center
print(game.board)  # AI has already responded
```

## Development

### Setup

Install development dependencies:

```bash
pip install -e ".[dev]"
```

### Testing

Run tests:

```bash
pytest
```

### Linting

Check code quality:

```bash
ruff check .
```

Format code:

```bash
ruff format .
```

## License

MIT License - see LICENSE file for details.
