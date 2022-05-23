from flask import request, jsonify, json
from nltk.tokenize import word_tokenize
from flask_cors import cross_origin

from init import app

from Models import Comments
from Models import Keywords
from Models import Posts
from Models import Images
from Models import Users



@app.route('/api/get_user', methods = ['GET'])
@cross_origin(allow_headers=['Content-Type'])
def get_user():

    users = Users.GetAllUser()

    try:
        UserList = []

        for i in users:
            userDict = {
            'idUser': i[0],
            'dateOfBirth': i[1],
            'address': i[2],
            'userName': i[3],
            'password': i[4],
            'email': i[5],
            'gender': i[6]
            }
            UserList.append(userDict)
        
            # convert to json data
            jsonStr = json.dumps(UserList)

    except Exception as e:
        print(e)

    return jsonify(jsonStr)


@app.route('/api/get_user_byId/<idUser>', methods = ['GET'])
@cross_origin(allow_headers=['Content-Type'])
def get_user_byId(idUser):

    users_by_id = Users.GetUserById(idUser)

    try:
        UserByIdList = []

        for i in users_by_id:
            userByIdDict = {
            'idUser': i[0],
            'dateOfBirth': i[1],
            'address': i[2],
            'userName': i[3],
            'password': i[4],
            'email': i[5],
            'gender': i[6]
            }
            UserByIdList.append(userByIdDict)
        
            # convert to json data
            jsonStr = json.dumps(UserByIdList)

    except Exception as e:
        print(e)

    return jsonify(jsonStr)


def ComputeCmtScore(content,dateCreate,ranked,idUser,idPost):

    score = 0 
 
    '''
        LISTKEYWORD:
            0 - idKeyword
            1 - category
            2 - score
            3 - content
    '''
    
    ListKeyword = Keywords.GetKeyword()
    
    '''
        ALLCMT:
            0 - idComment
            1 - idPost
            2 - idUser
            3 - content
            4 - dateCreate
            5 - ranked
    '''
    
    Listword = word_tokenize(content)

    for word in Listword:
        for keyword in ListKeyword:
            if word == keyword[3]:
                score = score + keyword[2]
                break
        
    ranked = 'GOOD' if score > 0 else 'BAD'
    status = Comments.Insert_Comment(content,dateCreate,ranked,idUser,idPost)

    return status
'''
    User 1: cmt vô post đó là ABC
    User 2: cmt vô tiếp thì gọi create trước [lúc này trên client vẫn chỉ có cmt của User 1]
            sau khi create trong db nó 2 cmt của bài post đó nhưng client vẫn 1
            lúc này mình gọi lại 1 hàm get thì nó mới lấy được cả 2 cmt rồi trả lên show lại
'''
# TinhDiemCmt('she is beautiful','1-2-3','bad',1,1)



@app.route('/api/user_create_cmt', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def user_create_cmt():
    json_data = request.json

            
    content = json_data['content']
    dateCreate = json_data['dateCreate']
    ranked = json_data['ranked']
    idUser = json_data['idUser']
    idPost = json_data['idPost']
            
    try:
        status = ComputeCmtScore(content,dateCreate,ranked,idUser,idPost)
    except Exception as e:  
        print(e)
        status = 'The Comment has already execute.'
    return jsonify({'result':status})
# with app.app_context():
# user_create_cmt('she is beautiful','01-09-2001','Bad',1,1)


# def TinhDiemCmt(content,dateCreate,ranked,idUser,idPost):

#     score = 0 
 
#     '''
#         LISTKEYWORD:
#             0 - idKeyword
#             1 - category
#             2 - score
#             3 - content
#     '''
    
#     ListKeyword = Keywords.GetKeyword()
    
#     '''
#         ALLCMT:
#             0 - idComment
#             1 - idPost
#             2 - idUser
#             3 - content
#             4 - dateCreate
#             5 - ranked
#     '''
#     AllCmt = Comments.Get_Comment()
    

#     for cmt in AllCmt:
#         Listword = word_tokenize(cmt[3])
#         for word in Listword:
#             for keyword in ListKeyword:
#                 if word == keyword[3]:
#                     score = score + keyword[2]
#                     break
        
#         ranked = 'GOOD' if score > 0 else 'BAD'
#         status = Comments.Insert_Comment(cmt[1],cmt[2],cmt[3],cmt[4],ranked)
#         # status = Comments.Insert_Comment(content,dateCreate,ranked,idUser,idPost)

#         return status
# TinhDiemCmt('she is beautiful','1-2-3','bad',1,1)

# '''
#     User 1: cmt vô post đó là ABC
#     User 2: cmt vô tiếp thì gọi create trước [lúc này trên client vẫn chỉ có cmt của User 1]
#             sau khi create trong db nó 2 cmt của bài post đó nhưng client vẫn 1
#             lúc này mình gọi lại 1 hàm get thì nó mới lấy được cả 2 cmt rồi trả lên show lại
# '''

# @app.route('/api/user_create_cmt', methods=['POST'])
# def user_create_cmt(content,dateCreate,ranked,idUser,idPost):
#     json_data = request.json

    
#     content = json_data['content']
#     dateCreate = json_data['dateCreate']
#     ranked = json_data['ranked']
#     idUser = json_data['idUser']
#     idPost = json_data['idPost']
    
#     try:
#         status = Comments.Insert_Comment(content,dateCreate,ranked,idUser,idPost)
#         TinhDiemCmt(content,ranked)
#     except:  
#         status = 'The Comment has already execute.'
#     return jsonify({'result':status})
# user_create_cmt('she is beautiful','01-09-2001','Bad',1,1)


# @app.route('/api/get_comment', methods = ['GET'])
# @cross_origin(allow_headers=['Content-Type'])
# def get_comment():


#     comments = Comments.Get_Comment()

#     try:
#         CommentList = []

#         for i in comments:
#             cmtDict = {
#             'idComment': i[0],    
#             'idPost': i[1],
#             'idUser': i[2],
#             'content': i[3],
#             'dateCreate': i[4],
#             'ranked': i[5]
#             }
#             CommentList.append(cmtDict)
        
#             # convert to json data
#             jsonStr = json.dumps(CommentList)
 
#     except Exception as e:
#         print(e)

#     return jsonify(jsonStr)


@app.route('/api/get_comment', methods = ['GET'])
@cross_origin(allow_headers=['Content-Type'])
def get_comment():

    comments = Comments.Get_Comment()

    try:
        CommentList = []

        for i in comments:
            cmtDict = {
            'idComment': i[0],    
            'idPost': i[1],
            'idUser': i[2],
            'content': i[3],
            'dateCreate': i[4],
            'ranked': i[5]
            }
            CommentList.append(cmtDict)
        
            # convert to json data
            jsonStr = json.dumps(CommentList)
 
    except Exception as e:
        print(e)

    return jsonify(jsonStr)

@app.route('/api/get_comment_by_ID/<idComment>', methods = ['GET'])
@cross_origin(allow_headers=['Content-Type'])
def get_comment_by_ID(idComment):

    commentsByID = Comments.Get_Comment_By_ID(idComment)

    try:
        CommentByIDList = []

        for i in commentsByID:
            cmtByIDDict = {
            'idComment': i[0],    
            'idPost': i[1],
            'idUser': i[2],
            'content': i[3],
            'dateCreate': i[4],
            'ranked': i[5]
            }
            CommentByIDList.append(cmtByIDDict)
        
            # convert to json data
            jsonStr = json.dumps(CommentByIDList)
 
    except Exception as e:
        print(e)

    return jsonify(jsonStr)


@app.route('/api/update_comment', methods = ['PUT'])
@cross_origin(allow_headers=['Content-Type'])
def update_comment():
    
    json_data = request.json

    update_comment = Comments.Update_Comment(json_data['content'],json_data['ranked'],json_data['idComment'])

    return jsonify({'result':update_comment})


@app.route('/api/delete_comment/<idComment>', methods = ['DELETE'])
@cross_origin(allow_headers=['Content-Type'])
def delete_comment(idComment):

    delete_comment = Comments.Delete_Comment(idComment)

    return jsonify({'result':delete_comment})

@app.route('/api/create_post', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def create_post():
    json_data = request.json

    content = json_data['content']
    dateCreate = json_data ['dateCreate']
    idUser = json_data['idUser']
    
    try:
        status = Posts.Insert_Post(content,dateCreate,idUser)
    except:
        status = 'The Post is already post'
    return jsonify({'result':status})
    

    
@app.route('/api/get_post', methods = ['GET'])
@cross_origin(allow_headers=['Content-Type'])
def get_post():


    posts = Posts.GetPost()

    try:
        PostList = []

        for i in posts:
            postDict = {
            'idPost': i[0],
            'content': i[1],
            'dateCreate': i[2],
            'idUser': i[3],
            }
            PostList.append(postDict)
        
            # convert to json data
            jsonStr = json.dumps(PostList)

    except Exception as e:
        print(e)

    return jsonify(jsonStr)


@app.route('/api/get_post_byId/<idPost>', methods = ['GET'])
@cross_origin(allow_headers=['Content-Type'])
def get_post_byId(idPost):

    posts_byID = Posts.GetPostById(idPost)

    try:
        PostById_List = []

        for i in posts_byID:
            postByIdDict = {
             'idPost': i[0],
            'content': i[1],
            'dateCreate': i[2],
            'idUser': i[3],
            }
            PostById_List.append(postByIdDict)
        
            # convert to json data
            jsonStr = json.dumps(PostById_List)

    except Exception as e:
        print(e)

    return jsonify(jsonStr)


@app.route('/api/update_post', methods = ['PUT'])
@cross_origin(allow_headers=['Content-Type'])
def update_post():
    
    json_data = request.json

    update_post = Posts.Update_Post(json_data['idPost'],json_data['content'])

    return jsonify({'result':update_post})



@app.route('/api/delete_post/<idPost>', methods = ['DELETE'])
@cross_origin(allow_headers=['Content-Type'])
def delete_post(idPost):

    delete_post = Posts.Delete_Post(idPost)

    return jsonify({'result':delete_post})

    
        
@app.route('/api/create_image', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def create_image():
    json_data = request.json

    idPost = json_data['idPost']
    path = json_data ['path']
    
    try:
        status = Images.Insert_Image(idPost,path)
    except:
        status = 'The Image is already post'
    return jsonify({'result':status})
    

    
@app.route('/api/get_image', methods = ['GET'])
@cross_origin(allow_headers=['Content-Type'])
def get_image():


    images = Images.Get_Image()

    try:
        ImageList = []

        for i in images:
            imageDict = {
            'idImage': i[0],
            'idPost': i[1],
            'path': i[2],
            }
            ImageList.append(imageDict)
        
            # convert to json data
            jsonStr = json.dumps(ImageList)

    except Exception as e:
        print(e)

    return jsonify(jsonStr)



@app.route('/api/update_image', methods = ['PUT'])
@cross_origin(allow_headers=['Content-Type'])
def update_image():
    
    json_data = request.json

    update_image = Images.Update_Image(json_data['path'],json_data['idImage'])
    
    return jsonify({'result':update_image})




@app.route('/api/delete_image/<idImage>', methods = ['DELETE'])
@cross_origin(allow_headers=['Content-Type'])
def delete_image(idImage):

    delete_image = Images.Delete_Image(idImage)

    return jsonify({'result':delete_image})

    
        