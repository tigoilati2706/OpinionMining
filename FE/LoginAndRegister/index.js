let emailDOM = document.querySelector("#email");
let passwordDOM = document.querySelector("#password");
const form = document.querySelector('form');
let email = '';
let password = '';

emailDOM.oninput = (e) => {
  email = e.target.value;
};

passwordDOM.oninput = (e) => {
  password = e.target.value;
};

form.addEventListener('submit', function(e){
    e.preventDefault();
    (async () => {
      const users = await getUsers();
      // console.log(users[0].email);
      // console.log(users[0].password);

      for(let i = 0; i < users.length; i++){
        if (users[i].email === email && users[i].password === password){
          localStorage.setItem("userLogin", JSON.stringify(users[i]));
          location.replace(
            "../mainApp/index.html"
          );
        }
      }
    })()
})

async function getUsers() {
  try {
    const response = await axios.get("http://localhost:5000/api/get_user");
    console.log(response.data);
    return JSON.parse(response.data);
  } catch (error) {
    console.log(error);
  }
} 