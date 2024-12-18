
const sendDataToBackend = async (data) => {
    try {
        const response = await fetch('http://127.0.0.1:4887/socialmedia_backend/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            const result = await response.json();
            console.log('Response from backend:', result);
        } else {
            console.error('Failed to send data:', response.status, response.statusText);
        }
    } catch (error) {
        console.error('Error:', error);
    }
};

export const sendData = (data) => sendDataToBackend(data);
export const empty = (a,b) => a+b;

module.export = { sendData, empty };