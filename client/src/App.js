import React from 'react';
import Predict from './components/predict';

function App() {
    return (
        <div className="App">
            <h1>SMS Detector</h1>
            <h3>Check if a text message is SPAM or HAM</h3>
            <Predict/>
        </div>
    );
}

export default App;