document
    .getElementById("fileUpload")
    .addEventListener("change", function (event) {
        document.getElementById("loader-container").style.display = "block";
        console.log(this);
        console.log(this.files);
        event.preventDefault(); // Prevent the default form submission

        var formData = new FormData();
        formData.append("file", this.files[0]); // Append the file to the form data
       
        fetch("http://127.0.0.1:5000/", {
            // this.action contains the form's action attribute (URL to which the form data will be sent)
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
                // Insert the server's response into a specific part of your page, or replace the current content
                document.documentElement.innerHTML = html;
            })
            .catch((error) => {
                console.error("Error:", error);
                // Handle the error
                // For example, you could alert the user or display the error in the page
                alert("Error uploading file.");
            });
    });

