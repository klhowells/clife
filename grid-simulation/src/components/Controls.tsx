import React from 'react';

const Controls: React.FC<{ onStart: () => void; onStop: () => void; onReset: () => void; }> = ({ onStart, onStop, onReset }) => {
    return (
        <div className="controls">
            <button onClick={onStart}>Start</button>
            <button onClick={onStop}>Stop</button>
            <button onClick={onReset}>Reset</button>
        </div>
    );
};

export default Controls;