
const myForm = document.getElementById("myForm");

myForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const request = new XMLHttpRequest();

    const url = 'https://musiquity.herokuapp.com/search/?q='

    let query_text = myForm.nodeValue

    request.open("get", url + query_text);
    request.onload = function() {
        console.log(request.responseText);
    }
    request.send(new FormData(myForm));
})
