let emailDOM = document.querySelector("#email");
let passwordDOM = document.querySelector("#password");
const form = document.querySelector("form");
let email = "";
let password = "";

emailDOM.oninput = (e) => {
  email = e.target.value;
};

passwordDOM.oninput = (e) => {
  password = e.target.value;
};

form.addEventListener("submit", function (e) {
  e.preventDefault();
  if ("admin@gmail.com" === email && "1234" === password) {
    location.replace("../mainApp/adminDashboard.html");
  }
});
