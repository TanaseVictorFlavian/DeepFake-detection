document
    .getElementById("fileUpload")
    .addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission

        const formData = new FormData(this); // 'this' refers to the form element

        fetch(this.action, {
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
