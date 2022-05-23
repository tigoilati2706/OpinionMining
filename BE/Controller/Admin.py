from flask import request, jsonify, json
from flask_cors import cross_origin
from nltk.tokenize import word_tokenize
# from ratelimit import limits

from init import app

from Models import Admin
from Models import Comments
from Models import Keywords

@app.route('/api/ad_create_keyword', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def ad_create_keyword():
    json_data = request.json

    category = json_data['category']
    content = json_data['content']
    score = json_data['score']

    try:
        status = Admin.Admin_InsertKeyword(category,content,score)
    except:  
        status = 'The Admin Insert Keyword successfully'
    return jsonify({'result':status})


@app.route('/api/ad_get_keyword_20', methods = ['GET'])
# @limits(calls=1, period=1) #max 1 call per second
@cross_origin(allow_headers=['Content-Type'])
def ad_get_keyword_20():

    ad_get_keyword_20 = Admin.AdminGetKeyword()[:20] 

    try:
        KeywordList_20 = []

        for i in ad_get_keyword_20:
            KeywordDict_20 = {
            'idKeyword': i[0],
            'category': i[1],
            'score': i[2],
            'content': i[3],
            }
            KeywordList_20.append(KeywordDict_20)
        
            # convert to json data
            jsonStr = json.dumps(KeywordList_20)

    except Exception as e:
        print(e)

    return jsonify(jsonStr)


@app.route('/api/ad_get_keyword', methods = ['GET'])
# @limits(calls=1000, period=1) #max 1 call per second
@cross_origin(allow_headers=['Content-Type'])
def ad_get_keyword():

    ad_get_keyword = Admin.AdminGetKeyword()

    try:
        KeywordList = []

        for i in ad_get_keyword:
            KeywordDict = {
            'idKeyword': i[0],
            'category': i[1],
            'score': i[2],
            'content': i[3],
            }
            KeywordList.append(KeywordDict)
        
            # convert to json data
            jsonStr = json.dumps(KeywordList)

    except Exception as e:
        print(e)

    return jsonify(jsonStr)

def ComputeAllKeyword():
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
    AllCmt = Comments.Get_Comment()
    
    for cmt in AllCmt:
        Listword = word_tokenize(cmt[3])

        for word in Listword:
            for keyword in ListKeyword:
                if word == keyword[3]:
                    score = score + keyword[2]
                    break
        
        ranked = 'GOOD' if score > 0 else 'BAD'
        status = Comments.Update_Comment(cmt[3], ranked, cmt[0])
        print(status + '\n')

@app.route('/api/ad_update_keyword', methods = ['PUT'])
@cross_origin(allow_headers=['Content-Type'])
def ad_update_keyword():
    
    json_data = request.json

    ad_update_keyword = Admin.Admin_UpdateKeyword(json_data['category'],json_data['content'],json_data['score'],json_data['idKeyword'])
    ComputeAllKeyword()
    return jsonify({'result':ad_update_keyword})


@app.route('/api/ad_delete_keyword/<idKeyword>', methods = ['DELETE'])
@cross_origin(allow_headers=['Content-Type'])
def ad_delete_keyword(idKeyword):

    ad_delete_keyword = Admin.Admin_DeleteKeyword(idKeyword)

    return jsonify({'result':ad_delete_keyword})

    
        






