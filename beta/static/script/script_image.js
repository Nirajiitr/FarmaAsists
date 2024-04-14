const fileInput = document.getElementById('file-input');
const imagePreview = document.getElementById('image-preview');
const responseContainer = document.getElementById('response');
const resultBox = document.getElementById('result-box');
fileInput.addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function() {
            const img = document.createElement('img');
            img.src = reader.result;
            imagePreview.innerHTML = '';
            imagePreview.appendChild(img);
        }
        reader.readAsDataURL(file);
    }
});

// Function to update response
function updateResponse(response) {
    function updateResult(result) {
        resultBox.textContent = "Predicted result: " + response;
    }
    responseContainer.textContent = response;
    
    
}

// Function to handle form submission
document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(this);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json(); // Parse JSON response
    
    })
    .then(data => {
        
        updateResponse(data.result); // Update response
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
