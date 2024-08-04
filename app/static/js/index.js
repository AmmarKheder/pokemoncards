function get_card_details() {
    let file = document.getElementById("file");
    if (file.files && file.files.length > 0) {
        const selectedFile = file.files[0];
        let details = document.getElementById("details");
        let form = new FormData();
        form.append("file", selectedFile);
        fetch("/get_card_details", {
            method: "POST",
            body: form
        }).then(response => {
            return response.json().then(data => {
                if (response.status == 200) {
                    return data;
                } else {
                    alert(data.message);
                    details.innerHTML = "";
                }
            });
        })
        .then(data => {
            details.innerHTML = `<div class="grid_container">` +
                                `<label class="block">Card Name</label>&nbsp;&nbsp;` +
                                `<input class="box_style" readonly value='${data["Card Name"]}'>&nbsp;&nbsp;` +
                                `<label class="block">Card Number</label>&nbsp;&nbsp;` +
                                `<input class="box_style" readonly value='${data["Card Number"]}'>&nbsp;&nbsp;` +
                                `<label class="block">Set Name</label>&nbsp;&nbsp;` +
                                `<input class="box_style" readonly value='${data["Set Name"]}'>&nbsp;&nbsp;` +
                                `<label class="block">Year</label>&nbsp;&nbsp;` +
                                `<input class="box_style" readonly value='${data["Year"]}'>&nbsp;&nbsp;` +
                                `</div>` +
                                `<div class="image_container">` +
                                `<img class="image" src='${data["Image URL"]}' alt="Image de la carte">` +
                                `</div>`;
        });
    }
}
