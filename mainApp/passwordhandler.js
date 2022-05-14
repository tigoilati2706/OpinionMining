const password = document.querySelector(".password");
const passwordConfirm = document.querySelector(".password-confirm");
const oldPassword = document.querySelector(".old-password");
const userInfo = JSON.parse(localStorage.getItem("userLogin"));
const submitBtn = document.querySelector(".update-password-btn");
// console.log(userInfo);

function passwordConfirmationCheck(password, passwordConfirm) {
  if (password !== passwordConfirm) {
    return false;
  }
  return true;
}

async function updatePassword() {
  try {
    if (
      passwordConfirmationCheck(password.value, passwordConfirm.value) &&
      oldPassword.value === userInfo.password
    ) {
      const userProfile = {
        idUser: userInfo.idUser,
        userName: userInfo.userName,
        address: userInfo.address,
        email: userInfo.email,
        gender: userInfo.gender,
        dateOfBirth: userInfo.dateOfBirth,
        password: password.value,
      };

      const res = await axios.put(
        "http://localhost:5000/api/update_profile",
        userProfile
      );
      localStorage.setItem("userLogin", JSON.stringify(userProfile));
      alert("Successfully Changed Password");
    } else if (
      password.value.trim() === "" ||
      passwordConfirm.value.trim() === "" ||
      oldPassword.value.trim() === ""
    ) {
      alert("Please Fill Out All The Information!");
    } else if (oldPassword.value !== userInfo.password) {
      alert("Old password Is Not Correct!");
    } else if (passwordConfirmationCheck(password.value, passwordConfirm.value) == false) {
      alert("Password Does Not Match Password Confirm!")
    }else {
      alert('Something Went Wrong!')
    }
  } catch (error) {
    console.log(error);
  }
}

(async () => {
  submitBtn.addEventListener("click", () => {
    updatePassword();
  });
})();
