document
    .getElementById("fileUpload")
    .addEventListener("change", function (event) {
        console.log("File selected.");
        var formData = new FormData();

        formData.append("file", this.files[0]);

        fetch("http://127.0.0.1:5000/upload_image", {
            method: "POST",
            body: formData,
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.text(); // Assuming the server responds with text/html
            })
            .then((html) => {
                document.documentElement.innerHTML = html;
            })
            .catch((error) => {
                console.error("Error:", error);

                alert("Error uploading file.");
            });
    });

function runButtonHandler() {
    var checkbox = document.getElementById("toggle");
    if (checkbox && checkbox.checked) {
        console.log("Checkbox is checked.");
        console.log("The value of the checkbox is: " + checkbox.value);
    } else {
        console.log("Checkbox is not checked.");
    }

    document.getElementById("loader-container").style.display = "block";
    var formData = new FormData();
    formData.append("aug", checkbox ? checkbox.checked : false);
    

    let uploadedFile = document.getElementById("uploadedImage");
    
    if (!uploadedFile) uploadedFile = document.getElementById("uploadedVideo");

    formData.append("file_path", uploadedFile.src);
    fetch("http://127.0.0.1:5000/", {
        method: "POST",
        body: formData,

    })
        .then((response) => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.text(); // Assuming the server responds with text/html
        })
        .then((html) => {
            document.documentElement.innerHTML = html;
        })
        .catch((error) => {
            console.error("Error:", error);
        });
}

function refreshPageHard() {
    location.reload(true);
}