const username = document.querySelector(".username");
const address = document.querySelector(".address");
const email = document.querySelector(".email");
const dayOfBirth = document.querySelector(".day-of-birth");
const gender = document.getElementsByName("gender");
const goBackBtn = document.querySelector('.go-back-btn');
const updateBtn = document.querySelector('.update-btn');
const userInfo = JSON.parse(localStorage.getItem('userLogin'));

// console.log(userInfo);

username.value = userInfo.userName;
dayOfBirth.value = userInfo.dateOfBirth;
address.value = userInfo.address;
email.value = userInfo.email;
// console.log(gender)

goBackBtn.addEventListener("click",()=>{
    location.replace('./index.html')
});

function getInput(oldInput, newInput) {
  let result = null;
  if (oldInput === newInput){
    result = oldInput;
  } else {
    result = newInput;
  }
  return result;
};

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

(() => {
    if (userInfo.gender === "male") {
      gender[0].checked = "checked";
    } else if (userInfo.gender === "female") {
      gender[1].checked = "checked";
    } else {
      gender[2].checked = "checked";
    }
})();

async function updateProfile(){
  const userProfile ={
    idUser : userInfo.idUser,
    userName: username.value,
    address: address.value,
    email: email.value,
    gender:getGender(),
    dateOfBirth:dayOfBirth.value,
    password:userInfo.password
  }

  // console.log(JSON.stringify(userProfile));

  try {
    const res = await axios.put(
      "http://localhost:5000/api/update_profile",
      userProfile
    );
    localStorage.setItem("userLogin", JSON.stringify(userProfile));
    alert("Successfully Changed Information");
  } catch (error) {
    console.error(error);
  }
};

(async()=> {
  updateBtn.addEventListener("click",()=>{
    updateProfile();
  })
})();