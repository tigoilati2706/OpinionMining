import Models.Provider as Provider

from flask_sqlalchemy import SQLAlchemy


def Insert_Comment(content,dateCreate,ranked,idUser,idPost):
    query = "INSERT INTO Comments ('content','dateCreate',ranked,idUser,idPost) VALUES ('{}','{}','{}','{}','{}')".format(content,dateCreate,ranked,idUser,idPost)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Update_Comment(content,ranked,idComment):
    query = "UPDATE Comments SET content='{}',ranked='{}' WHERE idComment={}".format(content,ranked,idComment)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Delete_Comment(idComment):
    query = "DELETE FROM Comments WHERE idComment={}".format(idComment)
    msg = Provider.ExecuteNonQuery(query)
    return msg


def Get_Comment():
    query = "SELECT * FROM Comments"

    try : 
        record = Provider.ExecuteQuery(query)
        return record

    except:
        return None

def Get_Content():
    query = "SELECT content FROM Comments"

    try : 
        record = Provider.ExecuteQuery(query)
        return record

    except:
        return None

def Get_Comment_By_ID(idComment):
    query = "SELECT * FROM Comments WHERE idComment={}".format(idComment)

    try : 
        record = Provider.ExecuteQuery(query)
        return record

    except:
        return None


# Test 

# Insert_Comment('sadsa','2010-10-10',1,1)

Update_Comment('Yesadsadah',10,2)
# Delete_Comment(2)
# Get_Comment()





# @app.route('/api/get_post_byId/<idPost>', methods = ['GET'])
# @cross_origin(allow_headers=['Content-Type'])
# def get_post_byId(idPost):

#     posts_byID = Posts.GetPostById(idPost)

#     try:
#         PostById_List = []

#         for i in posts_byID:
#             postByIdDict = {
#              'idPost': i[0],
#             'content': i[1],
#             'dateCreate': i[2],
#             'idUser': i[3],
#             }
#             PostById_List.append(postByIdDict)
        
#             # convert to json data
#             jsonStr = json.dumps(PostById_List)

#     except Exception as e:
#         print(e)

#     return jsonify(jsonStr)




