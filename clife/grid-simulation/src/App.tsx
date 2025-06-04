import React, { useState } from 'react';
import Grid from './components/Grid';
import Controls from './components/Controls';
import RandomMode from './components/RandomMode';
import './styles/grid.css';

const App = () => {
    const [isRunning, setIsRunning] = useState(false);
    const [gridState, setGridState] = useState(Array(100).fill(Array(100).fill(false)));

    const startSimulation = () => {
        setIsRunning(true);
    };

    const stopSimulation = () => {
        setIsRunning(false);
    };

    const resetGrid = () => {
        setGridState(Array(100).fill(Array(100).fill(false)));
    };

    return (
        <div className="app">
            <h1>Grid Simulation</h1>
            <Controls 
                startSimulation={startSimulation} 
                stopSimulation={stopSimulation} 
                resetGrid={resetGrid} 
                isRunning={isRunning} 
            />
            <RandomMode setGridState={setGridState} />
            <Grid gridState={gridState} setGridState={setGridState} isRunning={isRunning} />
        </div>
    );
};

export default App;