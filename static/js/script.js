document.getElementById("uploadbtn").addEventListener("click", function () {
    let fileinp = document.getElementById("fileup");

    if (fileinp.files.length === 0) {
        alert("Please select an image first.");
        return;
    }

    let formdata = new FormData();
    formdata.append("file", fileinp.files[0]);

    fetch("/upload", {
        method: "POST",
        body: formdata
    })
    .then(response => response.json())  
    .then(data => {
        if (data.error) {
            document.getElementById("result").textContent = "Error: " + data.error;
        } else {
            document.getElementById("result").textContent = "Prediction: " + data.result;
            document.getElementById("uploadedimg").src = data.image_url;
            document.getElementById("uploadedimg").style.display = "block";
        }
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").textContent = "An error occurred.";
    });
});
