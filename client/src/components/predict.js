import React, {useState} from 'react';
import axios from 'axios';
import './predict.css'

function Predict() {

    // State to store the input message and prediction result
    const [message, setMessage] = useState('');
    const [prediction, setPrediction] = useState('');

    // Fetch function to gather if an inputted message is spam or ham
    const handleSubmit = async () => {
        try {
            // Make a POST request to the FastAPI backend
            const response = await axios.post('http://127.0.0.1:8000/predict/', {text: message});
            // Update the prediction state with the result from the backend
            setPrediction(response.data.prediction);
        } catch (error) {
            // Display errors
            console.error('Error making request:', error);
        }
    };

    // Form
    return (
        <div className='predict'>
            <div className='enter-message'>
                <textarea
                    type="text"
                    placeholder='Type your message here'
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    className="input" // Apply styles
                />
                <button onClick={handleSubmit}>Predict</button>
            </div>
            {prediction && <p>The message is {prediction}</p>}
        </div>
    );
}

export default Predict;
