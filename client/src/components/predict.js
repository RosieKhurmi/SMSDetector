import React, {useState} from 'react';
import axios from 'axios';

function FetchData() {

    const [message, setMessage] = useState('');
    const [prediction, setPrediction] = useState('');

    const handleSubmit = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:8000/predict/', {text: message});
            setPrediction(response.data.prediction);
        } catch (error) {
            console.error('Error making request:', error);
        }
    };

    return (
        <div>
            <h3>Enter your message below to determine whether it is spam or ham</h3>
            <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
            />
            <button onClick={handleSubmit}>Submit</button>
            <p>Prediction: {prediction}</p>
        </div>
    );
}

export default FetchData;
