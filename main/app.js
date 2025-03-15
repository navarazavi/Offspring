document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('submitBtn').addEventListener('click', function() {
        var userInput = document.getElementById('userInput').value;

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
            document.getElementById('stuResponse').innerText = data.response;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('stuResponse').innerText = "Oops! Something went wrong. Try again.";
        });
    });
});
