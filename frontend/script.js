
const myForm = document.getElementById("myForm");

myForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const request = new XMLHttpRequest();

    request.open("get", "heroku-code/backend/search_components/youtube.py");
    request.onload = function() {
        console.log(request.responseText);
    }
    request.send(new FormData(myForm));
})
