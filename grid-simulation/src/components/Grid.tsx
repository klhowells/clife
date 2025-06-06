import React, { useState, useEffect, useRef } from 'react';
import './grid.css';

const Grid = () => {
    const [grid, setGrid] = useState(Array(100).fill(null).map(() => Array(100).fill(false)));
    const [isDragging, setIsDragging] = useState(false);
    const [isRandomMode, setIsRandomMode] = useState(false);
    const gridRef = useRef<HTMLDivElement>(null);

    const toggleCell = (row: number, col: number) => {
        const newGrid = grid.map((r) => [...r]);
        newGrid[row][col] = !newGrid[row][col];
        setGrid(newGrid);
    };

    const handleMouseDown = (row: number, col: number) => {
        setIsDragging(true);
        toggleCell(row, col);
    };

    const handleMouseEnter = (row: number, col: number) => {
        if (isDragging) {
            toggleCell(row, col);
        }
    };

    const handleMouseUp = () => {
        setIsDragging(false);
    };

    const generateRandomCells = (percentage: number) => {
        const newGrid = Array(100).fill(null).map(() => Array(100).fill(false));
        const totalCells = 10000; // 100x100 grid
        const liveCellsCount = Math.floor((percentage / 100) * totalCells);

        let count = 0;
        while (count < liveCellsCount) {
            const row = Math.floor(Math.random() * 100);
            const col = Math.floor(Math.random() * 100);
            if (!newGrid[row][col]) {
                newGrid[row][col] = true;
                count++;
            }
        }
        setGrid(newGrid);
    };

    useEffect(() => {
        if (isRandomMode) {
            generateRandomCells(30); // Default to 30% live cells
        }
    }, [isRandomMode]);

    return (
        <div
            className="grid"
            ref={gridRef}
            onMouseUp={handleMouseUp}
            onMouseLeave={handleMouseUp}
        >
            {grid.map((row, rowIndex) => (
                <div key={rowIndex} className="row">
                    {row.map((cell, colIndex) => (
                        <div
                            key={colIndex}
                            className={`cell ${cell ? 'live' : ''}`}
                            onMouseDown={() => handleMouseDown(rowIndex, colIndex)}
                            onMouseEnter={() => handleMouseEnter(rowIndex, colIndex)}
                        />
                    ))}
                </div>
            ))}
        </div>
    );
};

export default Grid;