const username = document.querySelector(".username");
const password = document.querySelector(".password");
const passwordConfirm = document.querySelector(".password-confirm");
const dayOfBirth = document.querySelector(".day-of-birth");
const address = document.querySelector(".address");
const email = document.querySelector(".email");
const gender = document.getElementsByName("gender");
const submitBtn = document.querySelector('input[type="submit"]');
const registerBtn = document.querySelector(".register-btn");

// console.log(gender[1].value)
function getGender() {
  for (var i = 0, length = gender.length; i < length; i++) {
    if (gender[i].checked) {
      // alert(i);
      return gender[i].value;
    } else {
      // alert("Please select")
      return "other";
    }
  }
}

function passwordConfirmationCheck(password, passwordConfirm) {
  if (password !== passwordConfirm) {
    return false;
  }
  return true;
}

async function userRegistration() {
  const userInfo = {
    userName: username.value,
    password: password.value,
    address: address.value,
    email: email.value,
    gender: getGender(),
    dateOfBirth: dayOfBirth.value,
  };

  if (passwordConfirmationCheck(userInfo.password, passwordConfirm.value)) {
    try {
      // alert(getGender())
      const users = await getUsers();
      const emailExisted = users.map((user) => user.email);
      if (emailCheck(email.value, emailExisted)) {
        const res = await axios.post(
          "http://localhost:5000/api/register",
          userInfo
        );
        alert("Register Successs");
        // const res = await axios.post("http://localhost:3000/Users", userInfo);
        // alert(res.data);
      } else {
        alert("Email Already Exists!");
      }
    } catch (error) {
      console.log(error);
    }
  } else {
    alert("Password Comfirm Does Not Match Password!");
  }
}

registerBtn.addEventListener("click", () => {
  if (
    username.value !== "" &&
    password.value !== "" &&
    email.value !== "" &&
    getGender() !== ""
  ) {
    userRegistration();
  } else {
    alert("Please Fill Out All The Information!");
  }
});

const login = document.querySelector(".login");
login.addEventListener("click", () => {
  location.replace("../LoginAndRegister/login.html");
});

function emailCheck(email, emailExisted) {
  for (let i = 0; i < emailExisted.length; i++) {
    if (email === emailExisted[i]) {
      return false;
    }
  }
  return true;
}

async function getUsers() {
  try {
    const response = await axios.get("http://localhost:5000/api/get_user");
    // console.log(typeof response.data)
    return JSON.parse(response.data);
  } catch (error) {
    console.log(error);
  }
}
