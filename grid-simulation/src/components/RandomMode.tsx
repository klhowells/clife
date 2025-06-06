import React, { useState } from 'react';

const RandomMode = ({ setLiveCells }) => {
    const [percentage, setPercentage] = useState(0);

    const handleRandomize = () => {
        const totalCells = 10000; // 100x100 grid
        const liveCellsCount = Math.floor((percentage / 100) * totalCells);
        const newLiveCells = new Set();

        while (newLiveCells.size < liveCellsCount) {
            const randomIndex = Math.floor(Math.random() * totalCells);
            newLiveCells.add(randomIndex);
        }

        setLiveCells(newLiveCells);
    };

    return (
        <div>
            <input
                type="number"
                value={percentage}
                onChange={(e) => setPercentage(e.target.value)}
                min="0"
                max="100"
                placeholder="Percentage of live cells"
            />
            <button onClick={handleRandomize}>Randomize</button>
        </div>
    );
};

export default RandomMode;