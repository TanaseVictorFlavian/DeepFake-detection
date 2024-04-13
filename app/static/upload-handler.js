document
    .getElementById("fileUpload")
    .addEventListener("change", function (event) {
        document.getElementById("loader-container").style.display = "block";
        console.log(this);
        console.log(this.files);
        event.preventDefault(); 
        var formData = new FormData();
        formData.append("file", this.files[0]); 
       
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
                t
                document.documentElement.innerHTML = html;
            })
            .catch((error) => {
                console.error("Error:", error);

                alert("Error uploading file.");
            });
    });

