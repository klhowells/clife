# Grid Simulation Project

This project implements a grid simulation using React. The grid consists of 80x81 squares, each 10 pixels wide, allowing users to interact with the cells by toggling their state and controlling the simulation.

## Features

- **Interactive Grid**: Click on individual cells to toggle their state to "live" (light green). 
- **Multi-Cell Selection**: Click and drag to select multiple cells and toggle their states.
- **Random Mode**: Specify a percentage of cells to start as "live," randomly distributed across the grid.
- **Simulation Controls**: Start, stop, and reset the simulation using dedicated buttons.

## Project Structure

```
clife
├── grid-simulation
│   ├── src
│   │   ├── components
│   │   │   ├── Grid.tsx
│   │   │   ├── Controls.tsx
│   │   │   └── RandomMode.tsx
│   │   ├── styles
│   │   │   └── grid.css
│   │   ├── utils
│   │   │   └── helpers.ts
│   │   └── App.tsx
│   ├── public
│   │   └── index.html
│   ├── package.json
│   ├── tsconfig.json
│   └── README.md
└── .gitignore
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd clife/grid-simulation
   ```

3. Install the dependencies:
   ```
   npm install
   ```

4. Start the development server:
   ```
   npm start
   ```

5. Open your browser and go to `http://localhost:3000` to view the application.

## Usage

- Click on a cell to toggle its state.
- Click and drag to select multiple cells.
- Use the "Random Mode" to set a percentage of cells to start as "live."
- Control the simulation with the "Start," "Stop," and "Reset" buttons.

## License

This project is licensed under the MIT License.