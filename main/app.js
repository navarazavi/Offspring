document.addEventListener('DOMContentLoaded', function() {
    // Add event listener to the button or form submit for sending the request
    document.getElementById('submitBtn').addEventListener('click', function() {
        // Get user input
        var userInput = document.getElementById('userInput').value;

        // Make the POST request to the Flask API
        fetch('https://offspring-backend.onrender.com/ask_stu', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                question: userInput
            })
        })
        .then(response => response.json())
        .then(data => {
            // Display Stu's response
            document.getElementById('stuResponse').innerText = data.response;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('stuResponse').innerText = "Oops! Something went wrong. Try again.";
        });
    });
});
