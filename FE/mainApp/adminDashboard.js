const comments = document.querySelector(".comments-number");
const posts = document.querySelector(".posts-number");
const goodComments = document.querySelector(".good-comments-number");
const badComments = document.querySelector(".bad-comments-number");

async function getKeyword() {
  try {
    const response = await axios.get(
      "http://localhost:5000/api/ad_get_keyword_20"
    );
    return JSON.parse(response.data);
  } catch (error) {
    console.error(error);
  }
}
async function getComment() {
  try {
    const response = await axios.get("http://localhost:5000/api/get_comment");
    return JSON.parse(response.data);
  } catch (error) {
    console.error(error);
  }
}

async function getPost() {
  try {
    const response = await axios.get("http://localhost:5000/api/get_post");
    return JSON.parse(response.data);
  } catch (error) {
    console.error(error);
  }
}

function renderRecentKeyword(keyword) {
  (async () => {
    const table = document.querySelector("table");
    //   console.log(keyword);
    if (table) {
      let trows = document.createElement("tbody");

      trows.innerHTML += `
        <tr>
            <td>${keyword.category}</td>
            <td>${keyword.content}</td>
            <td>${keyword.score}</td>
        </tr>
    `;
      table.appendChild(trows);
    }
  })();
}

(async () => {
  const myChart = document.querySelector("#myChart").getContext("2d");
  console.log(myChart);

  const commentsNumber = await getComment();
  comments.innerHTML = commentsNumber.length;

  const postsNumber = await getPost();
  console.log(postsNumber);
  posts.innerHTML = postsNumber.length;

  let goodcommetsCounter = 0;
  let badCommentsCounter = 0;
  for (let i = 0; i < commentsNumber.length; i++) {
    if (commentsNumber[i].ranked.toUpperCase() === "GOOD") {
      goodcommetsCounter += 1;
    } else {
      badCommentsCounter += 1;
    }
  }

  goodComments.innerHTML = goodcommetsCounter;
  badComments.innerHTML = badCommentsCounter;

  let pieChart = new Chart(myChart, {
    type: "pie",
    data: {
      labels: ["Good", "Bad"],
      datasets: [
        {
          label: "bad comments vs good comments",
          data: [goodcommetsCounter, badCommentsCounter],
          backgroundColor: ["#60d6c5", "#ff6183"],
        },
      ],
    },
    options: {},
  });


  const recentKeywords = await getKeyword();
  for (let i = recentKeywords.length; i > recentKeywords.length - 10; i--) {
    renderRecentKeyword(recentKeywords[i]);
  }
})();

