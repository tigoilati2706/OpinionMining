const category = document.querySelector(".category-input");
const content = document.querySelector(".content-input");
const score = document.querySelector(".score-input");
const addKeywordBtn = document.querySelector(".add-keyword-btn");
const myChart = document.querySelector("#myChart2").getContext("2d");

async function getKeyword() {
  try {
    const response = await axios.get(
      "http://localhost:5000/api/ad_get_keyword"
    );
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

async function createKeyword(category, content, score) {
  if (category !=='' && content !== '' && score !=='') {
    try {
      const newKeyword = {
        category: category,
        content: content,
        score: score
      };
      await axios.post(
        "http://localhost:5000/api/ad_create_keyword",
        newKeyword
      );
      location.reload();
    } catch (error) {
      console.log(error);
      alert("Cannot Add Keyword!");
    }
  }else{
    alert("Please Fill Out All the Informations");
  }
}

(async () => {
  addKeywordBtn.onclick = () => {
    createKeyword(
      category.value.trim().toLowerCase(),
      content.value.trim(),
      Number(score.value.trim())
    );
  };

  const keywords = await getKeyword();
  for (let i = keywords.length; i > 0; i--) {
    renderRecentKeyword(keywords[i]);
  }

  let positiveKeywords = 0;
  let negativeKeywords = 0;
  for (let i = 0; i < keywords.length; i++) {
    if (keywords[i].category.toLowerCase() === "positive") {
      positiveKeywords += 1;
    } else {
      negativeKeywords += 1;
    }
  }

  let pieChart = new Chart(myChart, {
    type: "pie",
    data: {
      labels: ["Positive", "Negative"],
      datasets: [
        {
          label: "",
          data: [positiveKeywords, negativeKeywords],
          backgroundColor: ["#60d6c5", "#ff6183"],
        },
      ],
    },
    options: {},
  });
  //   console.log(positiveKeywords, negativeKeywords)
})();
