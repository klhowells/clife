# Conway's Game of Life - PyQt5 Implementation

This project is a PyQt5-based implementation of Conway's Game of Life, a cellular automaton devised by mathematician John Conway. The program simulates the evolution of cells on a grid based on simple rules, creating complex and fascinating patterns. Created with (by) CoPilot AI.

## Features

- **Grid Setup**: An 80x80 grid of squares (toroidal), each 10 pixels wide.
- **Cell States**: "Live" cells are displayed in light green, and "dead" cells are white.
- **Interactive Controls**:
  - Click on individual cells to toggle their state.
  - Click and drag to toggle multiple cells.
- **Random Mode**: Populate the grid with a random percentage of live cells, specified by the user.
- **Control Buttons**:
  - **Start**: Begin the simulation.
  - **Stop**: Pause the simulation.
  - **Reset**: Clear the grid.

## Requirements

- Python 3.7+
- PyQt5

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/clife.git
   cd clife
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Use the GUI to interact with the grid:
   - Click or drag to toggle cells.
   - Use the "Random" button to populate the grid with a random percentage of live cells.
   - Start, stop, or reset the simulation using the respective buttons.

## Rules of the Game

1. Any live cell with fewer than two live neighbors dies (underpopulation).
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies (overpopulation).
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

## Project Structure

```
clife/
├── main.py          # Entry point for the application
├── grid.py          # Logic for the grid and cell states
├── gui.py           # GUI implementation using PyQt5
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- John Conway for inventing the Game of Life.
- The PyQt5 library for making GUI development in Python straightforward.
