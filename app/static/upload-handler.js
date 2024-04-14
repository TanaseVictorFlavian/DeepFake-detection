document
    .getElementById("fileUpload")
    .addEventListener("change", function (event) {
        var checkbox = document.getElementById("toggle");
        if (checkbox.checked) {
            console.log("Checkbox is checked.");
            console.log("The value of the checkbox is: " + checkbox.value);
        } else {
            console.log("Checkbox is not checked.");
        }

        document.getElementById("loader-container").style.display = "block";
        console.log(this);
        console.log(this.files);
        event.preventDefault();
        var formData = new FormData();
        formData.append("file", this.files[0]);
        formData.append("aug", checkbox.checked);

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

                alert("Error uploading file.");
            });
    });
