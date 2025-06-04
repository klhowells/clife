export const generateRandomLiveCells = (percentage: number): boolean[][] => {
    const gridSize = 100;
    const totalCells = gridSize * gridSize;
    const liveCellsCount = Math.floor((percentage / 100) * totalCells);
    const liveCells = Array.from({ length: totalCells }, () => false);

    let count = 0;
    while (count < liveCellsCount) {
        const randomIndex = Math.floor(Math.random() * totalCells);
        if (!liveCells[randomIndex]) {
            liveCells[randomIndex] = true;
            count++;
        }
    }

    return Array.from({ length: gridSize }, (_, rowIndex) =>
        liveCells.slice(rowIndex * gridSize, (rowIndex + 1) * gridSize)
    );
};

export const toggleCellState = (grid: boolean[][], row: number, col: number): boolean[][] => {
    const newGrid = grid.map(row => [...row]);
    newGrid[row][col] = !newGrid[row][col];
    return newGrid;
};

export const handleMouseDrag = (grid: boolean[][], startRow: number, startCol: number, endRow: number, endCol: number): boolean[][] => {
    const newGrid = grid.map(row => [...row]);
    for (let row = Math.min(startRow, endRow); row <= Math.max(startRow, endRow); row++) {
        for (let col = Math.min(startCol, endCol); col <= Math.max(startCol, endCol); col++) {
            newGrid[row][col] = true; // Set cells to "live"
        }
    }
    return newGrid;
};