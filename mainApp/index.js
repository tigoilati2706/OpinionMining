// SIDEBAR
const menuItems = document.querySelectorAll(".menu-item");

// MESSAGES
const messagesNotification = document.querySelector("#messages-notification");

// THEME
const theme = document.querySelector("#theme");
const themeModal = document.querySelector(".customize-theme");
const fontSizes = document.querySelectorAll(".choose-size span");
var root = document.querySelector(":root");
const colorPalette = document.querySelectorAll(".choose-color span");
const Bg1 = document.querySelector(".bg-1");
const Bg2 = document.querySelector(".bg-2");
const Bg3 = document.querySelector(".bg-3");

// ================ SIDEBAR ===============

// remove active class from all menu items
const changeActiveItem = () => {
  menuItems.forEach((item) => {
    item.classList.remove("active");
  });
};

menuItems.forEach((item) => {
  item.addEventListener("click", () => {
    changeActiveItem();
    item.classList.add("active");
    if (item.id != "notifications") {
      document.querySelector(".notifications-popup").style.display = "none";
    } else {
      document.querySelector(".notifications-popup").style.display = "block";
      document.querySelector(
        "#notifications .notification-count"
      ).style.display = "none";
    }
  });
});

// THEME/DISPLAY CUSTOMIZATION

// opens modal
const openThemeModal = () => {
  themeModal.style.display = "grid";
};

// closes modal
const closeThemeModal = (e) => {
  if (e.target.classList.contains("customize-theme")) {
    themeModal.style.display = "none";
  }
};

// close modal
themeModal.addEventListener("click", closeThemeModal);

theme.addEventListener("click", openThemeModal);

// ======================== FONTS =========================

// remove active class from spans or font size selectors
const removeSizeSelector = () => {
  fontSizes.forEach((size) => {
    size.classList.remove("active");
  });
};

fontSizes.forEach((size) => {
  size.addEventListener("click", () => {
    removeSizeSelector();
    let fontSize;
    size.classList.toggle("active");

    if (size.classList.contains("font-size-1")) {
      fontSize = "10px";
      root.style.setProperty("----sticky-top-left", "5.4rem");
      root.style.setProperty("----sticky-top-right", "5.4rem");
    } else if (size.classList.contains("font-size-2")) {
      fontSize = "13px";
      root.style.setProperty("----sticky-top-left", "5.4rem");
      root.style.setProperty("----sticky-top-right", "-7rem");
    } else if (size.classList.contains("font-size-3")) {
      fontSize = "16px";
      root.style.setProperty("----sticky-top-left", "-2rem");
      root.style.setProperty("----sticky-top-right", "-17rem");
    } else if (size.classList.contains("font-size-4")) {
      fontSize = "19px";
      root.style.setProperty("----sticky-top-left", "-5rem");
      root.style.setProperty("----sticky-top-right", "-25rem");
    } else if (size.classList.contains("font-size-5")) {
      fontSize = "22px";
      root.style.setProperty("----sticky-top-left", "-12rem");
      root.style.setProperty("----sticky-top-right", "-35rem");
    }

    // change font size of the root html element
    document.querySelector("html").style.fontSize = fontSize;
  });
});

// remove active class from colors
const changeActiveColorClass = () => {
  colorPalette.forEach((colorPicker) => {
    colorPicker.classList.remove("active");
  });
};

// change primary colors
colorPalette.forEach((color) => {
  color.addEventListener("click", () => {
    let primary;
    // remove active class from colors
    changeActiveColorClass();

    if (color.classList.contains("color-1")) {
      primaryHue = 252;
    } else if (color.classList.contains("color-2")) {
      primaryHue = 52;
    } else if (color.classList.contains("color-3")) {
      primaryHue = 352;
    } else if (color.classList.contains("color-4")) {
      primaryHue = 152;
    } else if (color.classList.contains("color-5")) {
      primaryHue = 202;
    }
    color.classList.add("active");

    root.style.setProperty("--primary-color-hue", primaryHue);
  });
});

// theme BACKGROUND values
let lightColorLightness;
let whiteColorLightness;
let darkColorLightness;

// changes background color
const changeBG = () => {
  root.style.setProperty("--light-color-lightness", lightColorLightness);
  root.style.setProperty("--white-color-lightness", whiteColorLightness);
  root.style.setProperty("--dark-color-lightness", darkColorLightness);
};

// change background colors
Bg1.addEventListener("click", () => {
  // add active class
  Bg1.classList.add("active");
  // remove active class from the others
  Bg2.classList.remove("active");
  Bg3.classList.remove("active");
  // remove customized changes from local storage
  window.location.reload();
});

Bg2.addEventListener("click", () => {
  darkColorLightness = "95%";
  whiteColorLightness = "20%";
  lightColorLightness = "15%";

  // add active class
  Bg2.classList.add("active");
  // remove active class from the others
  Bg1.classList.remove("active");
  Bg3.classList.remove("active");
  changeBG();
});

Bg3.addEventListener("click", () => {
  darkColorLightness = "95%";
  whiteColorLightness = "10%";
  lightColorLightness = "0%";

  // add active class
  Bg3.classList.add("active");
  // remove active class from others
  Bg1.classList.remove("active");
  Bg2.classList.remove("active");
  changeBG();
});

//GET DATE
function getDate() {
  var currentdate = new Date();
  var datetime =
    currentdate.getDate() +
    "/" +
    (currentdate.getMonth() + 1) +
    "/" +
    currentdate.getFullYear() +
    " - " +
    currentdate.getHours() +
    ":" +
    currentdate.getMinutes() +
    ":" +
    currentdate.getSeconds();
  return datetime;
}

//RENDER USER INFO
const userLoginInfo = JSON.parse(localStorage.getItem("userLogin"));
const username = document.querySelector(".username");
const userIdProfileText = document.querySelector(".profile-text");
console.log(userLoginInfo);
username.innerText = userLoginInfo.userName;
userIdProfileText.innerText = `id: ${userLoginInfo.idUser}`;

//NEWFEEDS
import addFeed from "./feedHandler.js";
//ADD NEW POST
let createPostBtn = document.querySelector("#new-post");
let newPostContent = document.querySelector("#create-post");
let postContent = "";

newPostContent.oninput = (e) => {
  postContent = e.target.value;
};
async function createPost(content, user) {
  const newPost = {
    content: content.trim(),
    dateCreate: getDate(),
    idUser: user.idUser,
    idAdmin: "admin1",
  };
  if (content.trim() !== "") {
    try {
      // console.log(newPost);
      const res = await axios.post(
        "http://localhost:5000/api/create_post",
        newPost
      );
      location.reload();
    } catch (error) {
      console.error(error);
    }
  } else {
    alert("Please Fill In The Content Of The Post");
  }
}

createPostBtn.addEventListener("click", (e) => {
  createPost(postContent, userLoginInfo);
});

//RENDER POSTS

async function renderPosts() {
  const response = await axios.get("http://localhost:5000/api/get_post");
  const posts = JSON.parse(response.data);
  //  console.log(posts);

  for (let i = posts.length - 1; i >= 0; i--) {
    addFeed(posts[i]);
  }
}

renderPosts();

//ADD COMMENT
let newFeeds = document.querySelector(".feeds");

//TOGGLE COMMNET SECTION

var divArray = document.getElementsByClassName("feeds")[0];

var observer = new MutationObserver(function () {
  var commentSections = document.getElementsByClassName("view-commnents");
  for (
    let i = 0;
    i < document.getElementsByClassName("view-commnents").length;
    ++i
  ) {
    commentSections[i].onclick = (e) => {
      // e.target.classList.toggle("display-block");
      const parentNode = String(e.target.classList[0]);
      const parentNodeId = parentNode.split("-")[2];
      const childNode = document.getElementsByClassName(
        `comment-section-${parentNodeId}`
      )[0];
      childNode.classList.toggle("display-block");
      // console.log(childNode);
    };
  }
});

observer.observe(divArray, {
  attributes: false,
  childList: true,
  subtree: true,
});

// When you've got what you need, you should call this function to trigger a disconnect
function classesFound() {
  observer.disconnect();
}

//ADD COMMENT
var observer = new MutationObserver(function () {
  var commentInputSections = document.getElementsByClassName("comment-input");
  for (let i = 0; i < commentInputSections.length; ++i) {
    commentInputSections[i].onclick = (e) => {
      const commentInput = String(e.target.classList[0]);
      // const commentInputId = commentInput.charAt(commentInput.length - 1);
      const commentInputId = commentInput.split("-")[2];
      const createPostBtn = document.getElementsByClassName(
        `btn-create-comment-${commentInputId}`
      )[0];
      // console.log(createPostBtn);
      e.target.oninput = (e) => {
        postContent = e.target.value;
        // console.log(commentInputId, postContent);
      };
      createPostBtn.addEventListener("click", (e) => {
        e.preventDefault();
        createComment(postContent, Number(commentInputId), userLoginInfo);
      });
    };
  }
});

observer.observe(divArray, {
  attributes: false,
  childList: true,
  subtree: true,
});

async function createComment(content, idPost, user) {
  const newComment = {
    content: content.trim(),
    dateCreate: getDate(),
    idUser: user.idUser,
    idPost,
    ranked: "good",
  };
  if (content.trim() !== ''){
    try {
      // console.log(newComment);
      const res = await axios.post(
        "http://localhost:5000/api/user_create_cmt",
        newComment
      );
      location.reload();
    } catch (error) {
      console.error(error);
    }
  }else{
    alert("Please Fill In The Content Of The Comment");
  }
}

//DELETE POST
var observer = new MutationObserver(function () {
  var postSections = document.getElementsByClassName("delete-post");
  for (let i = 0; i < postSections.length; ++i) {
    postSections[i].onclick = (e) => {
      const post = String(
        document.getElementsByClassName("toggle-comments")[i].classList[0]
      );

      const user = String(
        document.getElementsByClassName("user")[i].classList[0]
      );

      const postId = post.split("-")[2];

      const userId = user.split("-")[1];

      // console.log(userId);

      if (Number(userId) === userLoginInfo.idUser) {
        deletePost(postId);
      } else {
        alert("You Are Not The Owner Of This Post");
      }
      // console.log("userId:" + userId);
    };
  }
});

observer.observe(divArray, {
  attributes: false,
  childList: true,
  subtree: true,
});

async function deletePost(postId) {
  try {
    await axios.delete(`http://localhost:5000/api/delete_post/${postId}`);
    location.reload();
  } catch (error) {
    console.log("error");
  }
}

//LOGOUT FEATURE

const logout = document.querySelector(".logout-item");
logout.addEventListener("click", () => {
  localStorage.removeItem("userLogin");
  location.replace("../LoginAndRegister/login.html");
});

//GO TO ADMIN DASHBOARD
const adminDashboard = document.querySelector(".analytics-item");
adminDashboard.addEventListener("click", () => {
  // localStorage.removeItem("userLogin");
  location.replace("../LoginAndRegister/loginAdmin.html");
});

// END
