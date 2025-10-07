# Contributing to ZTicTacToe

Thank you for your interest in contributing to ZTicTacToe!

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/Sumanth-NR/ZTicTacToe.git
cd ZTicTacToe
```

2. Install development dependencies:
```bash
pip install pytest flake8 mypy
```

## Code Quality Standards

This project follows Python best practices and maintains high code quality standards:

### Linting
We use `flake8` for code linting:
```bash
flake8 zttt/
```

### Type Checking
We use `mypy` for static type checking:
```bash
mypy zttt/
```

### Testing
All changes must pass existing tests:
```bash
pytest tests/
```

## Code Style Guidelines

- Follow PEP 8 style guide
- Use type hints for all function signatures
- Maximum line length: 120 characters
- Use meaningful variable and function names
- Add docstrings for all public classes and methods
- Use enum types for constants where appropriate

## Making Changes

1. Create a new branch for your feature/fix
2. Make your changes
3. Add tests for new functionality
4. Run linting and tests
5. Commit with clear, descriptive messages
6. Submit a pull request

## Architecture

The codebase is organized as follows:

- `zttt/_zt_core/`: Core game logic
  - `zt_base_board.py`: Base board class with game state management
  - `zt_base_engine.py`: Base engine class for AI logic
  - `zt_engine_first.py`: AI implementation for when engine goes first
  - `zt_player_first.py`: AI implementation for when player goes first
- `zttt/pvp.py`: Player vs Player game mode
- `zttt/pvc.py`: Player vs Computer game mode
- `zttt/zt_errors.py`: Custom exception classes

## Key Design Patterns

- **Composition over Inheritance**: PvC uses composition to delegate to appropriate engine
- **Enums for Type Safety**: CellValue and Player enums provide type-safe constants
- **Event Callbacks**: on_move and on_finish callbacks for custom game event handling
- **Property Decorators**: Clean API with read-only properties for game state

## Questions?

Feel free to open an issue for any questions or concerns!
