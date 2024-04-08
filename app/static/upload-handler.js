document.getElementById('fileUpload').addEventListener('change', function(event) {
    if (event.target.files && event.target.files[0]) {
        const formData = new FormData();
        formData.append('fileUpload', event.target.files[0]);

        document.querySelector('.loader-container').style.display = 'grid';

        fetch('/index', { 
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('prediction').textContent = data.prediction;
            document.getElementById('confidenceValue').textContent = `${data.confidence}%`;
        })
        .catch(error => console.error('Error:', error));
    }
});