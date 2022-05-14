function addFeed(post) {
    const newFeeds = document.querySelector(".feeds");
    let { content, dateCreate, idPost, idUser } = post;
    let commentsRendered = "";
    console.log(idPost);
    (async () => {
    const user = await getUser(idUser);
    commentsRendered = await getComment(post, user);
    // console.log( commentsRendered);
    if (newFeeds) {
        const feed = document.createElement("div");
        feed.classList.add("feed");
        feed.innerHTML = `
                        <div class="head">
                            <div class="user-${idUser} user">
                                <div class="profile-photo">
                                    <img src="https://i.pinimg.com/originals/0c/3b/3a/0c3b3adb1a7530892e55ef36d3be6cb8.png">
                                </div>
                                <div class="ingo">
                                    <h3>${user.userName}</h3>
                                    <small>${dateCreate}</small>
                                </div>
                            </div>
                            <span class="delete-post">
                                <span><i title="Delete Post" class="uil uil-minus-circle"></i></span>
                            </span>
                        </div>
                        <div class="photo">
                            <img src="https://images.pexels.com/photos/96622/pexels-photo-96622.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940">
                        </div>
                        <div class="caption">
                            <p>${content}</p>
                        </div>
                        <div class="comments text-muted view-commnents">
                            <p class="toggle-comments-${idPost} toggle-comments">View all comments</p>
                            <div class="comment-section-${idPost} comment-section">
                                <!-- comment -->
                                ${commentsRendered}
                                <!-- end of comment  -->
                            </div>
                        </div>
                        <div class="comment-input-section">
                            <div class="comment">
                                <i class="uil uil-comment-dots"></i>
                                <input class="comment-input-${idPost} comment-input" type="text" placeholder="What do you think?">
                            </div>
                            <button class="btn-create-comment-${idPost} btn btn-primary" type='submit'>Reply</button>
                        </div>
                    `;

        newFeeds.appendChild(feed);
        }
    })();
}

async function getComment(post) {
    let commentRendered = "";
    try {
    const res = await axios.get("http://localhost:5000/api/get_comment");
    const response = JSON.parse(res.data);
    // console.log(res.data);
    for (let i = 0; i < response.length; ++i) {
        if (response[i].idPost === post.idPost) {
            const user = await getUser(response[i].idUser);
            commentRendered += `<div class="user-comment">
                                    <img class="profile-photo"  src="https://i.pinimg.com/originals/0c/3b/3a/0c3b3adb1a7530892e55ef36d3be6cb8.png">
                                    <div class="user-comment-body">
                                        <div class="user-name-and-content">
                                            <h4 class="user-name">${user.userName} </h4>
                                            <p class="comment-content">${response[i].content}</p>
                                        </div>
                                        <h4 class="comment-ranking">Comment rating: ${response[i].ranked}</h4>
                                    </div>
                                </div>`;
        }
    }
    // return res.data;
    return commentRendered;
        } catch (error) {
    console.log(error);
    }
    console.log(commentRendered);
}

async function getUser(id){
    try {
        const response = await axios.get(
            `http://localhost:5000/api/get_user_byId/${id}`
        );
        // console.log(JSON.parse(response.data));
        return JSON.parse(response.data)[0];
    } catch (error) {
        console.log(error);
    }
}

export default addFeed;
